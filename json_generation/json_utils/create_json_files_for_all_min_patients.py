
import json
import os
import sys
from copy import deepcopy
from pathlib import Path

#from ..s3_utils.s3_utils import upload_file_to_S3

# sys.path.insert(1, '/home/ubuntu/src/data_extraction')
# sys.path.insert(1, '/home/ubuntu/src/utils/time')
# sys.path.insert(1, '/home/ubuntu/src/utils/json')
sys.path.insert(1, '/home/ubuntu/src')
# sys.path.remove(os.path.dirname(__file__))


# from .time.time_zone import get_current_date, get_yesterday_date
# from data_extraction.app_classifier import image_classifier
#from data_extraction.app_classifier import image_classifier
from app_classifier import image_classifier
# target_date = '2022-08-02's

# today_date = get_current_date(tz = 'Asia/Kolkata')
# yesterday_date = get_yesterday_date(tz = 'Asia/Kolkata')

# print(f"today_date: {today_date}", f"yesterday_date: {yesterday_date}")

# target_date = yesterday_date
target_date = '2023-03-22' # On Monday we have to add the date manually
print("target_date: ", target_date)

images_folder_base_path = Path('/home/ubuntu/Advanced_classification') / target_date
download_json_base_path = Path('/home/ubuntu/Extracted-data')

def write_json(patient_dir: Path):
    for image_path in patient_dir.rglob('*.tiff'):
        ent_dict = image_classifier(str(image_path))
        with open(image_path.parent / (image_path.stem  + '.json'), 'w') as f:
            json.dump(ent_dict, f)

write_json(images_folder_base_path)


def update_appnt_with_case_data(appnt_json, tab_dict):    

    print("tab_dict: ", json.dumps(tab_dict, indent = 4), sep ="\n")   

    patient_attributes = ["mrn", "patientdob"]

    # We shall take patientlastname and patientfirstname from Case tab, as they are not getting extracted 
    # properly in Demo tab
    appnt_json['patientlastname'] = tab_dict['data']['patientlastname']
    appnt_json['patientfirstname'] = tab_dict['data']['patientfirstname']
    
    for i in patient_attributes:
        if not appnt_json[i]:
            print(f"i:  {i}, appnt_json[i]:   {appnt_json[i]}", "\n")              
            appnt_json[i] = tab_dict['data'][i]   
    
    case_attributes = ["servicetype", "dateofservice", "apptscheduledtime",
                        "apptscheduledendtime","cleanuptime", "anesthesiatype",
                        "providerlastname", "providerfirstname", "Procedures"]   

    for i in case_attributes:
        if not appnt_json["Case"][i]:
            print(f"i:  {i}, appnt_json[i]:   {appnt_json['Case'][i]}", "\n")              
            appnt_json["Case"][i] = tab_dict["data"][i]    
    

def update_appnt_with_demo_data(appnt_json, tab_dict):  

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
    appnt_json["Case"]['dateofservice'] = tab_dict['data']['dateofservice']



def  update_appnt_with_contact_data(appnt_json, tab_dict):
    print("tab_dict: ", json.dumps(tab_dict, indent = 4), sep ="\n")  

    # attributes = ["mrn", "patientdob", "apptstatus", "dateofservice"]
    patient_attributes = ["mrn", "patientdob"]

    for i in patient_attributes:
        if not appnt_json[i]:
            print(f"i:  {i}, appnt_json[i]:   {appnt_json[i]}", "\n")              
            appnt_json[i] = tab_dict['data'][i]
            
    appnt_json["Case"]['apptstatus'] = tab_dict['data']['apptstatus']
    appnt_json["Case"]['dateofservice'] = tab_dict['data']['dateofservice']


def create_appnt_json_all(patient_dir: Path):
    print ("call")
    p_folder_list = []
    p_names = set()
    p_appnts = {}

    with open("/home/ubuntu/src/utils/api_utils/server_inputV2.json", 'r') as json_template:
        appnt = json.load(json_template)
        # print("appnt: ", appnt, "\n")
        # print("appnt['patient'] original: ", appnt['Patient'], "\n")                  
    # appnt_json = appnt['Patient'].copy()
    for image_path in patient_dir.rglob('*.json'):
        # print (image_path)
        # print (image_path.parent)
        p_folder_list.append(image_path)
        p_names.add(image_path.parent.parent.name)

    for patient in p_names:
        p_appnts[patient] = deepcopy(appnt['Patient'])
    
    for image_path in patient_dir.rglob('*.json'):
        appnt_json = p_appnts[image_path.parent.parent.name]              
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

    #upload_file_to_S3('/home/ubuntu/Extracted-data/all_patients_2022-08-08.json', f"pleasantview/{TARGET_DATE}//summary.json"
#', 'extracte')

    #upload_file_to_S3()

create_appnt_json_all(images_folder_base_path)

