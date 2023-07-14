import re
import os
from os                        import listdir
from paddleocr                 import PaddleOCR,draw_ocr
from pathlib import Path
from PIL                       import Image,ImageOps





CROPPED_IMAGES_DIR = Path("/home/ubuntu/cropped_images/2022-05-19/")
CROPPED_IMAGES_DIR_FIRSTCROP = Path("/home/ubuntu/cropped_images/")
ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)






def contact_entities(path):

  
  file_name = path.split('/')[-1]
  

  cropped_file_path = CROPPED_IMAGES_DIR / file_name
  cropped_file_path.touch()
  cropped_file_path_first = CROPPED_IMAGES_DIR_FIRSTCROP / file_name
  cropped_file_path_first.touch()



# IMAGE CROPPING **************************************************************************************************************************************
  
  image=Image.open(path)
  box = (138, 97, 1118, 730)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path_first, dpi=(400,400) , )

  
# Dictionary initialising*************************************************************************************************************************** 
  
  contact_entities_paddle = {}
  contact_entities_paddle = {
                                       "mrn"                   :"",
                                       "patientdob"            :"",
                                       "dateofservice"         :"",
                                       "apptstatus"            :""
                                       }



# mrn  ******************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (587,38,657,54)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
# PADDLE OCR
  
  result = ocr.ocr(str(cropped_file_path), cls=True)
  image = Image.open(str(cropped_file_path)).convert('RGB')
  txts = [line[1][0] for line in result]
  text_paddle=" ".join(txts)
  contact_entities_paddle["mrn"] = "".join(text_paddle).strip()
  
  

# dob ****************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (718,39,783,53)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
# PADDLE OCR
  
  result = ocr.ocr(str(cropped_file_path), cls=True)
  image = Image.open(str(cropped_file_path)).convert('RGB')
  txts = [line[1][0] for line in result]
  text_paddle=" ".join(txts)
  text_paddle =text_paddle.replace(" ", '')
  contact_entities_paddle["patientdob"] = "".join(text_paddle).strip()
  
  
  
# dos  **************************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (103,187,201,204)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  
# PADDLE OCR
  
  result = ocr.ocr(str(cropped_file_path), cls=True)
  image = Image.open(str(cropped_file_path)).convert('RGB')
  txts = [line[1][0] for line in result]
  text_paddle=" ".join(txts)
  text_paddle =text_paddle.replace(" ", '')
  contact_entities_paddle["dateofservice"] = "".join(text_paddle).strip()
  
  
  
# case status *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (59,208,158,227)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  # PADDLE OCR
  
  result = ocr.ocr(str(cropped_file_path), cls=True)
  image = Image.open(str(cropped_file_path)).convert('RGB')
  txts = [line[1][0] for line in result]
  text_paddle=" ".join(txts)
  contact_entities_paddle["apptstatus"] = "".join(text_paddle).strip()
  
 



#PRINTING AND RETURNING DICT**************************************************************************************************************************
  
  #print(contact_entities_paddle)
  return(contact_entities_paddle)
  
#contact_entities("/home/ubuntu/test_images/contact/Vision - Pleasant View Surgery Center (2023-03-15 15-15-51.375).tiff")