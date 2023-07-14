import json
from PIL                       import Image
from paddleocr                 import PaddleOCR
from paddle_ocr_function       import paddle_ocr
from casetab_objects           import casetab_entities
from payers_objects            import payer_entities
from demographics_objects      import demo_entities
from demographics_zip_objects  import demo_zip_entities
from payment_objects           import payment
from contact_objects           import contact_entities
from copy                      import deepcopy
from pathlib                   import Path
import os
#import time


CROPPED_IMAGES_DIR = Path("/home/ubuntu/cropped_img_new/second_crop/")
CROPPED_IMAGES_DIR_FIRSTCROP = Path("/home/ubuntu/cropped_img_new/")



# image classifier function 


def image_classifier(path): 
  #begin = time.time()
  file_name = path.split('/')[-1]
  

  cropped_file_path = CROPPED_IMAGES_DIR / file_name
  cropped_file_path.touch()
  cropped_file_path_first = CROPPED_IMAGES_DIR_FIRSTCROP / file_name
  cropped_file_path_first.touch()


  output_dict = {
                    "tab": "",
                    "file_name": "",
                    "data": {}
                }

  output_dict["file_name"] = file_name 

  

# IMAGE CROPPING 
  
  image=Image.open(path)
  box = (138, 97, 1118, 730)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path_first, dpi=(400,400) , )
  
  
# for case tab  
# room
  
  image=Image.open(cropped_file_path_first)
  box = (175,119,215,133)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_room = paddle_ocr(cropped_file_path)
  print(text_paddle_room)
  
  
# start
  
  image=Image.open(cropped_file_path_first)
  box = (322,118,355,130)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_start = paddle_ocr(cropped_file_path)
  print(text_paddle_start)
  


# for demo and zip
# account id
  
  image=Image.open(cropped_file_path_first)
  box = (217,118,283,131)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_account = paddle_ocr(cropped_file_path)
  print(text_paddle_account)

# religion
  
  image=Image.open(cropped_file_path_first)
  box = (230,185,285,198)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_religion = paddle_ocr(cropped_file_path)
  print(text_paddle_religion)



# zip
  
  image=Image.open(cropped_file_path_first)
  box = (108,345,149,364)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle_zip = paddle_ocr(cropped_file_path)
  print(text_paddle_zip)

# payers 

# payers 

  image=Image.open(path)
  box = (445,69,661,81)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_insurance = paddle_ocr(cropped_file_path)
  print("text_paddle_insurance",text_paddle_insurance)
  


# group no
  
  image=Image.open(path)
  box = (240,140,327,155)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_groupno = paddle_ocr(cropped_file_path)
  print("text_paddle_groupno",text_paddle_groupno)

# unique
  
  image=Image.open(path)
  box = (233,118,327,133)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_unique = paddle_ocr(cropped_file_path)  
  print("text_paddle_unique",text_paddle_unique)

# active
  
  image=Image.open(path)
  box = (340,297,392,312)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_active = paddle_ocr(cropped_file_path)
  print("text_paddle_active",text_paddle_active)

# city
  
  image=Image.open(path)
  box = (337,507,388,524)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_city = paddle_ocr(cropped_file_path)
  print("text_paddle_city",text_paddle_city)

# phone
  
  image=Image.open(path)
  box = (238,456,277,469)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_phone = paddle_ocr(cropped_file_path)
  print("text_paddle_phone",text_paddle_phone)

  
# guarantors

  image=Image.open(cropped_file_path_first)
  box = (442,458,515,474)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_guarantors = paddle_ocr(cropped_file_path)
  print(text_paddle_guarantors)
  
# payment profiles

  image=Image.open(cropped_file_path_first)
  box = (5,83,108,99)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_payment_profiles = paddle_ocr(cropped_file_path)
  print(text_paddle_payment_profiles)
# contact


# emergency contact

  image=Image.open(cropped_file_path_first)
  box = (25,406,138,422)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_contact = paddle_ocr(cropped_file_path)
  print(text_paddle_contact)
  
  
  
# date of service

  image=Image.open(cropped_file_path_first)
  box = (22,188,104,201)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_service = paddle_ocr(cropped_file_path)
  print(text_paddle_service)

  
  #end = time.time()
  #print(f"Total time for image loading and extraction for classification  {end - begin}")

  # tab classification
  
  
  if ( ( "Room" in text_paddle_room ) or ( "Start" in text_paddle_start) ) :
    
    #begin = time.time()
    extracted_data = casetab_entities(path) 
    output_dict["tab"] = "case"
    output_dict["data"] =  deepcopy(extracted_data) 
    
    print()
    print("output_dict: ")
    print()
    print(json.dumps(output_dict, indent = 4))
    
    #end = time.time()
    #print(f"Total time for case extraction  {end - begin}")
    return output_dict
  
  elif ( ( "Account" in text_paddle_account) or ( "Religion" in text_paddle_religion ) ) :
    
    if (len(text_paddle_zip) > 4):
        #begin = time.time() 

        extracted_data = demo_zip_entities(path)
        output_dict["tab"] = "demo_zip"
        output_dict["data"] =  deepcopy(extracted_data)

        print()
        print("output_dict: ")
        print()
        print(json.dumps(output_dict, indent = 4))
        
        #end = time.time()
        #print(f"Total time for demo_zip extraction  {end - begin}")
        return output_dict
    
    else :
        #begin = time.time()
        
        extracted_data = demo_entities(path)
        output_dict["tab"] = "demo"
        output_dict["data"] =  deepcopy(extracted_data)
          
        print()
        print("output_dict: ")
        print()
        print(json.dumps(output_dict, indent = 4))
        
        #end = time.time()
        #print(f"Total time for demo extraction  {end - begin}")
        return output_dict
  
  elif ( ( ( ( "Active" in text_paddle_active) and ( "Group Number" in text_paddle_groupno ) ) or 
       ( ( "City" in text_paddle_city) and ( "Group Number" in text_paddle_groupno ) ) or 
       ( ( "Unique" in text_paddle_unique) and ( "Phone" in text_paddle_phone ) ) ) and 
       ("Pre-Admission" not in text_paddle_insurance) and ( "Extended" not in text_paddle_insurance) and ( "Extendedrcare" not in text_paddle_insurance ) )  :
    #begin = time.time()
      

    extracted_data = payer_entities(path)
    output_dict["tab"] = "payers"
    output_dict["data"] =  deepcopy(extracted_data)
      
    print()
    print("output_dict: ")
    print()
    print(json.dumps(output_dict, indent = 4))
    
    #end = time.time()  
    #print(f"Total time for payers extraction  {end - begin}")
    return output_dict

  elif ( ( "Guarantors" in text_paddle_guarantors) or ( "Payment Profiles" in text_paddle_payment_profiles ) ):

      extracted_data = payment(path)
      
      output_dict["tab"] = "payment"
      output_dict["data"] = deepcopy(extracted_data)
      
      print()
      print("output_dict: ")
      print()
      print(json.dumps(output_dict, indent = 4))
      return output_dict
  
  elif ( ( "Contact" in text_paddle_contact) or ( "Service" in text_paddle_service ) ):

      extracted_data = contact_entities(path)
      
      output_dict["tab"] = "contact"
      output_dict["data"] = deepcopy(extracted_data)
      
      print()
      print("output_dict: ")
      print()
      print(json.dumps(output_dict, indent = 4))
      return output_dict
  
  
  
  else :
    print("unwanted")
    return None


#directory = "/home/ubuntu/advance_classified_images_bydate/2022-09-20/"
#for filename in os.scandir(directory):
    #if filename.is_file():
        #path = filename.path
        #image_classifier(path)

image_classifier("/home/ubuntu/Vision - Pleasant View Surgery Center (2023-03-24 05-31-20.771).tiff")