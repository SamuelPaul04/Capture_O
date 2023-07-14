import re
from pathlib                   import Path
from PIL                       import Image,ImageOps
from paddle_ocr_function       import paddle_ocr




#"/home/ubuntu/cropped_images/2022-05-19/"

CROPPED_IMAGES_DIR = Path("/home/ubuntu/cropped_images/")



def payer_entities(path):

  file_name = path.split('/')[-1]
  
  cropped_file_path = CROPPED_IMAGES_DIR / file_name
  cropped_file_path.touch()
  


# initialising dictionary **************************************************************************************************************************
  
  

  payers_entities_paddle={ }
  payers_entities_paddle = { 
                                      "name"                             : "",
                                      "policynumber"                     : "",
                                      "role"                             : "",
                                      "coinsurancepercentage"            : "",
                                      "subscriberlastname"               : "",
                                      "subscriberfirstname"              : "",
                                      "subscriberdob"                    : "",
                                      "subscriberrelationshiptopatient"  : "",
                                      "subscribergender"                 : "",
                                      "groupnumber"                      : "",            
                                      "groupname"                        : "", 
                              
                              }


# name  ******************************************************************************************************************************
  #box = (117,32,345,50)
  image=Image.open(path)
  box = (112,32,607,51)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  #print("hello")
  text_paddle=re.sub('[^A-Za-z0-9-]+', ' ', text_paddle)
  #print(text_paddle)
  payers_entities_paddle["name"] = "".join(text_paddle).strip()
  
  
   
# role ****************************************************************************************************************************************
  image=Image.open(path)
  box = (116,85,190,106)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle=re.sub('[^A-Za-z]+', ' ', text_paddle)
  payers_entities_paddle["role"] = "".join(text_paddle).strip()
  
  
  
#policy no **************************************************************************************************************************************************
  #box = (117,109,216,127)
  image=Image.open(path)
  box = (38,109,214,126)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle=re.sub('[^A-Za-z0-9-]+', ' ', text_paddle)
  text_paddle=re.sub('Insurance ID', ' ', text_paddle)
  text_paddle=re.sub('InsuranceID', ' ', text_paddle)
  text_paddle = text_paddle.replace("|","")
  text_paddle = text_paddle.replace("[","")
  text_paddle = text_paddle.replace(" ","")
  payers_entities_paddle["policynumber"] = "".join(text_paddle).strip()
  
  
  
#group no **************************************************************************************************************************************************
  image=Image.open(path)
  box = (324,132,412,150)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle=re.sub('[^A-Za-z0-9-]+', ' ', text_paddle)
  payers_entities_paddle["groupnumber"] = "".join(text_paddle).strip()
  


# dob *************************************************************************************************************************************
  
  image=Image.open(path)
  box = (640,238,702,254)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle = re.sub('[^0-9/]+','', text_paddle)
  payers_entities_paddle["subscriberdob"] = "".join(text_paddle.upper()).strip()
  
 

# first name ******************************************************************************************************************************************
  
  image=Image.open(path)
  box = (364,236,473,253)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle=re.sub('[^A-Za-z]+', ' ', text_paddle)
  text_paddle =text_paddle.replace(" ", '')
  payers_entities_paddle["subscriberfirstname"] = "".join(text_paddle.upper()).strip()
  


# last name ******************************************************************************************************************************************
  
  image=Image.open(path)
  box = (117,233,279,254)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle=re.sub('[^A-Za-z]+', ' ', text_paddle)
  text_paddle =text_paddle.replace(" ", '')
  payers_entities_paddle["subscriberlastname"] = "".join(text_paddle.upper()).strip()
  

# gender *************************************************************************************************************************************************
  
  image=Image.open(path)
  box = (631,262,692,279)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle=re.sub('[^A-Za-z]+', ' ', text_paddle)
  payers_entities_paddle["subscribergender"] = "".join(text_paddle).strip()
  


# subscriber relationship ******************************************************************************************************************************
  
  image=Image.open(path)
  box = (179,181,292,201)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle=re.sub('[^A-Za-z0-9-]+', ' ', text_paddle)
  payers_entities_paddle["subscriberrelationshiptopatient"] = "".join(text_paddle).strip()
  


# group name ******************************************************************************************************************************
  
  image=Image.open(path)
  box = (113,135,214,151)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle=re.sub('[^A-Za-z0-9-]+', ' ', text_paddle)
  payers_entities_paddle["groupname"] = "".join(text_paddle).strip()
  









#PRINTING AND RETURNING DICT**************************************************************************************************************************
  
  
  return(payers_entities_paddle)
  



