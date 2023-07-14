import re
from pathlib                   import Path
from PIL                       import Image,ImageOps
from paddle_ocr_function       import paddle_ocr



CROPPED_IMAGES_DIR = Path("/home/ubuntu/cropped_images/2022-05-19/")
CROPPED_IMAGES_DIR_FIRSTCROP = Path("/home/ubuntu/cropped_images/")



def demo_zip_entities(path):

  file_name = path.split('/')[-1]
  
  cropped_file_path = CROPPED_IMAGES_DIR / file_name
  cropped_file_path.touch()
  cropped_file_path_first = CROPPED_IMAGES_DIR_FIRSTCROP / file_name
  cropped_file_path_first.touch()



# IMAGE CROPPING **************************************************************************************************************************************
  
  image=Image.open(path)
  box = (120, 120, 920, 706)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path_first, dpi=(400,400) , )

  
# Dictionary initialising ****************************************************************************************************************************
  
  demographics_entities_zip_paddle = {}
  demographics_entities_zip_paddle = {
                                       "mrn"                   :"",
                                       "patientlastname"       :"",
                                       "patientfirstname"      :"",
                                       "patientdob"            :"",
                                       "addresssstate"         :"",
                                       "addressszip"           :""
                                       
                                       }



# mrn_top  ******************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (544,1,602,19)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_zip_paddle["mrn"] = "".join(text_paddle).strip()
  
  

# dob_top ****************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (662,1,721,18)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle = re.sub('[^0-9/]+','', text_paddle)
  text_paddle =text_paddle.replace(" ", '')
  demographics_entities_zip_paddle["patientdob"] = "".join(text_paddle).strip()
  
  
  
#mrn **************************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (91,80,150,94)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle = re.sub('[^0-9]+','', text_paddle)
  demographics_entities_zip_paddle["mrn"] = "".join(text_paddle).strip()
  
  
  
# last name *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (91,54,199,76)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle=re.sub('[^A-Za-z]+', ' ', text_paddle)
  text_paddle = text_paddle.replace(" ","")
  demographics_entities_zip_paddle["patientlastname"] = "".join(text_paddle.upper()).strip()
  
 

# first name ******************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (229,55,422,73)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle=re.sub('[^A-Za-z]+', ' ', text_paddle)
  text_paddle =text_paddle.replace(" ", '')
  text_paddle = text_paddle.upper()
  text_paddle = text_paddle.replace("FIRSTNAME","")
  demographics_entities_zip_paddle["patientfirstname"] = "".join(text_paddle.upper()).strip()
  

# dob***************************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (655,56,716,75)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_zip_paddle["patientdob"] = "".join(text_paddle).strip()
  

# zip code *************************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (114,311,164,326)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_zip_paddle["addressszip"] = "".join(text_paddle).strip()
  


# address state *************************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (382,288,418,304)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_zip_paddle["addresssstate"] = "".join(text_paddle.upper()).strip()
  

#PRINTING AND RETURNING DICT**************************************************************************************************************************
  
  
  return(demographics_entities_zip_paddle)
  



