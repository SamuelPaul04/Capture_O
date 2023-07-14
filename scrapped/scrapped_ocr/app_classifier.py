import json
from PIL                       import Image
from paddleocr                 import PaddleOCR
from paddle_ocr_function       import paddle_ocr
from casetab_objects           import casetab_entities
from payers_objects            import payer_entities
from demographics_objects      import demo_entities
from demographics_zip_objects  import demo_zip_entities
from payment_objects           import payment
from copy                      import deepcopy
from pathlib                   import Path
#import time
import shutil
import os


CROPPED_IMAGES_DIR = Path("/home/ubuntu/cropped_images/2022-05-19/")
CROPPED_IMAGES_DIR_FIRSTCROP = Path("/home/ubuntu/cropped_images/")



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
  box = (120, 120, 920, 706)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path_first, dpi=(400,400) , )
  
  
# for case tab  
# Preference cards
  
  image=Image.open(cropped_file_path_first)
  box = (19,123,117,135)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_cards = paddle_ocr(cropped_file_path)
  #print(text_paddle_cards)
  
# description
  
  image=Image.open(cropped_file_path_first)
  box = (291,136,356,151)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_description = paddle_ocr(cropped_file_path)
  #print(text_paddle_description)
  

# upper icd 10
  
  image=Image.open(cropped_file_path_first)
  box = (565,287,629,299)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_upper_icd = paddle_ocr(cropped_file_path)
  #print(text_paddle_upper_icd)
  
  
  
  
# lower icd 10
  
  image=Image.open(cropped_file_path_first)
  box = (569,367,627,379)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_lower_icd = paddle_ocr(cropped_file_path)
  #print(text_paddle_lower_icd)


# upper #2
  
  image=Image.open(cropped_file_path_first)
  box = (701,343,738,356)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_upper_2 = paddle_ocr(cropped_file_path)
  #print(text_paddle_upper_2)
  
  
  
# lower #2
  
  image=Image.open(cropped_file_path_first)
  box = (701,344,738,357)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_lower_2 = paddle_ocr(cropped_file_path)
  #print(text_paddle_lower_2)


# upper asst
  
  image=Image.open(cropped_file_path_first)
  box = (381,255,411,267)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_upper_asst = paddle_ocr(cropped_file_path)
  #print("upper:   ",text_paddle_upper_asst)
  
  
# lower asst
  
  image=Image.open(cropped_file_path_first)
  box = (381,337,411,349)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_lower_asst = paddle_ocr(cropped_file_path)
  #print("lower:    ",text_paddle_lower_asst)




# for demo and zip
# Email
  
  image=Image.open(cropped_file_path_first)
  box = (42,467,88,480)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_email = paddle_ocr(cropped_file_path)
  #print(text_paddle_email)

# Home
  
  image=Image.open(cropped_file_path_first)
  box = (20,519,98,534)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_home = paddle_ocr(cropped_file_path)
  #print(text_paddle_home)


# code
  
  image=Image.open(cropped_file_path_first)
  box = (23,316,116,329)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_code = paddle_ocr(cropped_file_path)
  #print(text_paddle_code)


# zip_text
  
  image=Image.open(cropped_file_path_first)
  box = (168,312,211,327)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_zip_text = paddle_ocr(cropped_file_path)
  #print(text_paddle_zip_text)



# zip_value
  
  image=Image.open(cropped_file_path_first)
  box = (115,311,160,329)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_zip = paddle_ocr(cropped_file_path)
  

# payers 

  image=Image.open(path)
  box = (112,32,607,51)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_insurance = paddle_ocr(cropped_file_path)
  print("text_paddle_insurance",text_paddle_insurance)
  


# group no
  
  image=Image.open(path)
  box = (237,134,317,152)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_groupno = paddle_ocr(cropped_file_path)
  #print("text_paddle_groupno",text_paddle_groupno)

# unique
  
  image=Image.open(path)
  box = (231,114,325,131)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_unique = paddle_ocr(cropped_file_path)  
  #print("text_paddle_unique",text_paddle_unique)

# active
  
  image=Image.open(path)
  box = (361,399,409,412)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_active = paddle_ocr(cropped_file_path)
  #print("text_paddle_active",text_paddle_active)

# city
  
  image=Image.open(path)
  box = (333,504,367,515)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_city = paddle_ocr(cropped_file_path)
  #print("text_paddle_city",text_paddle_city)

# phone
  
  image=Image.open(path)
  box = (234,450,275,466)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_phone = paddle_ocr(cropped_file_path)
  #print("text_paddle_phone",text_paddle_phone)


# guarantors

  image=Image.open(cropped_file_path_first)
  box = (449,421,517,436)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_guarantors = paddle_ocr(cropped_file_path)
  #print(text_paddle_guarantors)
  
# payment profiles

  image=Image.open(cropped_file_path_first)
  box = (14,50,111,65)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle_payment_profiles = paddle_ocr(cropped_file_path)
  
  
  #end = time.time()
  #print(f"Total time for image loading and extraction for classification  {end - begin}")

  # tab classification ***************************************************************************************************************************************
  
  
  
  
  if ( ( ( "Cards" in text_paddle_cards ) and ( "IC" in text_paddle_upper_icd) and ("#" in text_paddle_lower_2) and ( "IC" in text_paddle_upper_icd) and                     ("Ass" in  text_paddle_upper_asst)  ) or 
      ( ( "Description" in text_paddle_description ) and ( "IC" in text_paddle_upper_icd) and ("#" in text_paddle_upper_2) and ( "IC" in text_paddle_upper_icd) and        ( "Ass" in text_paddle_lower_asst)  ) ) :
    
    #begin = time.time()
    #extracted_data = casetab_entities(path) 
    #output_dict["tab"] = "case"
    #output_dict["data"] =  deepcopy(extracted_data) 
    
    #print()
    #print("output_dict: ")
    #print()
    #print(json.dumps(output_dict, indent = 4))
    print("case")
    #shutil.move(path, "/home/ubuntu/testing_classified_images/case_2/")
    #end = time.time()
    #print(f"Total time for case extraction  {end - begin}")
    return output_dict
  
  elif ( ( ( "Email" in text_paddle_email) and ( "Code" in text_paddle_code ) ) or 
  ( ( "Home" in text_paddle_home) and ( "Zip" in text_paddle_zip_text ) ) )  :
    
    if (len(text_paddle_zip) > 4):
        #begin = time.time() 

        #extracted_data = demo_zip_entities(path)
        #output_dict["tab"] = "demo_zip"
        #output_dict["data"] =  deepcopy(extracted_data)

        #print()
        #print("output_dict: ")
        #print()
        #print(json.dumps(output_dict, indent = 4))
        print("Demo_zip")
        #shutil.move(path, "/home/ubuntu/testing_classified_images/demo_zip/")
        #end = time.time()
        #print(f"Total time for demo_zip extraction  {end - begin}")
        return output_dict
    
    else :
        #begin = time.time()
        
        #extracted_data = demo_entities(path)
        #output_dict["tab"] = "demo"
        #output_dict["data"] =  deepcopy(extracted_data)
          
        #print()
        #print("output_dict: ")
        #print()
        #print(json.dumps(output_dict, indent = 4))
        print("Demo")
        #shutil.move(path, "/home/ubuntu/testing_classified_images/demo/")
        #end = time.time()
        #print(f"Total time for demo extraction  {end - begin}")
        return output_dict
  
  elif ( ( ( ( "Active" in text_paddle_active) and ( "Group Number" in text_paddle_groupno ) ) or 
       ( ( "City" in text_paddle_city) and ( "Group Number" in text_paddle_groupno ) ) or 
       ( ( "Unique" in text_paddle_unique) and ( "Phone" in text_paddle_phone ) ) ) and 
       ("Pre-Admission" not in text_paddle_insurance) and ( "Extended" not in text_paddle_insurance) and ( "Extendedrcare" not in text_paddle_insurance ) )  :
    
    #begin = time.time()
      
    print("payers")
    #extracted_data = payer_entities(path)
    #output_dict["tab"] = "payers"
    #output_dict["data"] =  deepcopy(extracted_data)
      
    #print()
    #print("output_dict: ")
    #print()
    #print(json.dumps(output_dict, indent = 4))
    #shutil.move(path, "/home/ubuntu/test_images/payers/")
    #end = time.time()  
    #print(f"Total time for payers extraction  {end - begin}")
    return output_dict
    
  elif ( ( "Guarantors" in text_paddle_guarantors) or 
  ( "Payment Profiles" in text_paddle_payment_profiles ) ):

      #extracted_data = payment(path)
      
      #output_dict["tab"] = "payment"
      #output_dict["data"] = deepcopy(extracted_data)
      print("payment")
      #print()
      #print("output_dict: ")
      #print()
      #print(json.dumps(output_dict, indent = 4))
      #shutil.move(path, "/home/ubuntu/testing_classified_images/payment/")
      return output_dict
  
  else :
    #shutil.move(path, "/home/ubuntu/")
    print("unwanted")
    return None


#directory = "/home/ubuntu/Payor information/"
#for filename in os.scandir(directory):
    #if filename.is_file():
        #path = filename.path
        #image_classifier(path)





image_classifier("/home/ubuntu/Vision - Pleasant View Surgery Center (2023-01-17 13-32-27.592).tiff")
