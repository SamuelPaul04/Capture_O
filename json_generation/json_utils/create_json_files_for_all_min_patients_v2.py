
import json
import sys
from copy import deepcopy
from pathlib import Path

# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, '/home/ubuntu/dheeraj_src_with_payer/new_ocr')

sys.path.insert(1, '/home/ubuntu/src/data-extraction')
sys.path.insert(1, '/home/ubuntu/src')

from app_classifier import image_classifier
from time_zone import get_current_date, get_yesterday_date

# target_date = '2022-07-15'

#today_date = get_current_date(tz = 'Asia/Kolkata')
#yesterday_date = get_yesterday_date(tz = 'Asia/Kolkata')

#print(f"today_date: {today_date}", f"yesterday_date: {yesterday_date}")

# target_date = yesterday_date
target_date = '2022-09-29' # On Monday we have to add the date manually

print("target_date: ", target_date)

images_folder_base_path = Path('/home/ubuntu/Advanced_classification') / target_date
download_json_base_path = Path('/home/ubuntu/Extracted-data')

def write_json(patient_dir: Path):
    for image_path in patient_dir.rglob('*.tiff'):
    # for image_path in :    
        ent_dict = image_classifier(str(image_path))
        with open(image_path.parent / (image_path.stem  + '.json'), 'w') as f:
            json.dump(ent_dict, f)

# write_json(images_folder_base_path)


def update_appnt_with_case_data(appnt_json, tab_dict):  

    print("tab_dict: ", json.dumps(tab_dict, indent = 4), sep ="\n")   

    patient_attributes = ["mrn", "patientlastname", "patientfirstname", "patientdob"]

    for i in patient_attributes:
        if not appnt_json[i]:
            print(f"i:  {i}, appnt_json[i]:   {appnt_json[i]}", "\n")              
            appnt_json[i] = tab_dict['data'][f'case_{i}']   
    
    case_attributes = ["servicetype", "dateofservice", "apptscheduledtime",
                        "apptscheduledendtime","cleanuptime", "anesthesiatype",
                        "providerlastname", "providerfirstname", "Procedures"]   

    for i in case_attributes:
        if not appnt_json["Case"][i]:
            print(f"i:  {i}, appnt_json[i]:   {appnt_json['Case'][f'case_{i}']}", "\n")              
            appnt_json["Case"][i] = tab_dict["data"][i]   
    

def update_appnt_with_demo_data(appnt_json, tab_dict):

    # appnt_json["patientsuffix"] = tab_dict['data']['patientsuffix']               
    # appnt_json["patientmi"] = tab_dict['data']['patientmi']
    # appnt_json["patientgender"] = tab_dict['data']["patientgender"]
    # appnt_json["addressstreet1"] = tab_dict['data']["addressstreet1"]
    # appnt_json["addressstreet2"] = tab_dict['data']["addressstreet2"]
    # appnt_json["addressscity"] = tab_dict['data']["addressscity"]
    # appnt_json["patientcellphone"] = tab_dict['data']["patientcellphone"]
    # appnt_json["patienthomephone"] =  tab_dict['data']["patienthomephone"]
    # appnt_json["patientemail"] = tab_dict['data']["patientemail"]
    # appnt_json["languagepreference"] = tab_dict['data']["languagepreference"]

    print("tab_dict: ", json.dumps(tab_dict, indent = 4), sep ="\n")    

    patient_attributes = ["mrn", "patientlastname", "patientfirstname", "patientdob"]

    for i in patient_attributes:
        if not appnt_json[i]:
            print(f"i:  {i}, appnt_json[i]:   {appnt_json[i]}", "\n")              
            appnt_json[i] = tab_dict['data'][i]

    attributes = ["mrn","patientsuffix","patientmi","patientgender",
                "addressstreet1", "addressstreet2","addressscity",
                "patientcellphone", "patienthomephone", "patientemail",
                "languagepreference"]
    for i in attributes:
        if not appnt_json[i]:
            print(f"i:  {i}, appnt_json[i]:   {appnt_json[i]}", "\n")              
            appnt_json[i] = tab_dict['data'][i]



def  update_appnt_with_demo_zip_data(appnt_json, tab_dict):
    print("tab_dict: ", json.dumps(tab_dict, indent = 4), sep ="\n")    
   
    appnt_json['addresssstate'] = tab_dict['data']['addresssstate']
    appnt_json['addressszip'] = tab_dict['data']['addressszip'] 



def  update_appnt_with_payers_data(appnt_json, tab_dict):
    print("tab_dict: ", json.dumps(tab_dict, indent = 4), sep ="\n") 

    appnt_json["Case"]['Payors'].append(tab_dict['data'])



def  update_appnt_with_payment_data(appnt_json, tab_dict):
    print("tab_dict: ", json.dumps(tab_dict, indent = 4), sep ="\n")  

    patient_attributes = ["mrn", "patientdob"]

    for i in patient_attributes:
        if not appnt_json[i]:
            print(f"i:  {i}, appnt_json[i]:   {appnt_json[i]}", "\n")              
            appnt_json[i] = tab_dict['data'][i]

    appnt_json["Case"]['apptstatus'] = tab_dict['data']['apptstatus']



def  update_appnt_with_contact_data(appnt_json, tab_dict):
    print("tab_dict: ", json.dumps(tab_dict, indent = 4), sep ="\n")  

    # attributes = ["mrn", "patientdob", "apptstatus", "dateofservice"]
    appnt_json["Case"]['apptstatus'] = tab_dict['data']['apptstatus']


def create_appnt_json_all(patient_dir: Path):
    print ("call")
    p_folder_list = []
    p_names = set()
    p_appnts = {}

    with open("/home/ubuntu/src/server_inputV2.json", 'r') as json_template:
        appnt = json.load(json_template)
        # print("appnt: ", appnt, "\n")
        # print("appnt['patient'] original: ", appnt['Patient'], "\n")  
        #                 
    # appnt_json = appnt['Patient'].copy()
    appnt_json = {'Case': {}}

    # for image_path in patient_dir.rglob('*.json'):
    #     # print (image_path)
    #     # print (image_path.parent)
    #     p_folder_list.append(image_path)
    #     p_names.add(image_path.parent.parent.name)

    # for patient in p_names:
    #     p_appnts[patient] = deepcopy(appnt['Patient'])
    
    for image_path in patient_dir.rglob('*.json'):
        # appnt_json = p_appnts[image_path.parent.parent.name]              
        with open(image_path, 'r') as f:
            tab_dict = json.load(f)
                # print("image_path: ", image_path, "\n")  
            if tab_dict:              
                tab_type = tab_dict['tab']
                print("tab_dict type: ", tab_type, "\n")
                print("tab_dict: ", "\n")
                print(json.dumps(tab_dict, indent = 4), "\n")               

                if tab_type == "case":
                    update_appnt_with_case_data(appnt_json, deepcopy(tab_dict))                   
                    print('Updated appnt_json: ', "\n")
                    print(json.dumps(appnt_json, indent = 4))
                elif tab_type == "demo_zip": 
                    update_appnt_with_demo_zip_data(appnt_json, deepcopy(tab_dict))                   
                    print('Updated appnt_json: ', "\n")
                    print(json.dumps(appnt_json, indent = 4))
                elif tab_type == "payers":
                    update_appnt_with_payers_data(appnt_json, deepcopy(tab_dict))
                    # appnt_json["Case"]['Payors'].append(tab_dict['data'].copy())
                    print('Updated appnt_json: ', "\n")
                    print(json.dumps(appnt_json, indent = 4))
                elif tab_type == "payment":
                    update_appnt_with_payment_data(appnt_json, deepcopy(tab_dict))
                    # appnt_json["Case"]['Payors'].append(tab_dict['data'].copy())
                    print('Updated appnt_json: ', "\n")
                    print(json.dumps(appnt_json, indent = 4))
                elif tab_type == "demo":
                    update_appnt_with_demo_data(appnt_json, deepcopy(tab_dict))                   
                    print('Updated appnt_json: ', "\n")
                    print(json.dumps(appnt_json, indent = 4))
                elif tab_type == "contact":
                    update_appnt_with_contact_data(appnt_json, deepcopy(tab_dict))                   
                    print('Updated appnt_json: ', "\n")
                    print(json.dumps(appnt_json, indent = 4))
        print('--------------------------------------------------------------------------------------------')
        # print('--------------------------------------------------------------------------------------------')
        # print (image_path.parent.parent)

        # ent_dict = image_classifier(str(image_path))
        # with open(image_path.parent / (image_path.stem + '.json'), 'w') as f:
        #     json.dump(ent_dict, f)

    print(p_names)
    # print(p_appnts)
    print(json.dumps(p_appnts, indent = 4))

    with open(download_json_base_path / f'all_patients_{target_date}.json', 'w') as f:
        json.dump(p_appnts, f)


# create_appnt_json_all(images_folder_base_path)
create_appnt_json_all(Path('/home/ubuntu/Advanced_classification/2022-07-28/BORGEN_PATRICK_0005779_10_25_1968'))
