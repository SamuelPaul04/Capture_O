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
  box = (138, 97, 1118, 730)
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
  box = (589,39,661,54)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_zip_paddle["mrn"] = "".join(text_paddle).strip()
  
  

# dob_top ****************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (717,39,787,52)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle = re.sub('[^0-9/]+','', text_paddle)
  text_paddle =text_paddle.replace(" ", '')
  demographics_entities_zip_paddle["patientdob"] = "".join(text_paddle).strip()
  
  
  
#mrn **************************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (82,115,203,132)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle = re.sub('[^0-9]+','', text_paddle)
  demographics_entities_zip_paddle["mrn"] = "".join(text_paddle).strip()
  
  
  
# last name *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (83,94,204,109)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle=re.sub('[^A-Za-z]+', ' ', text_paddle)
  text_paddle = text_paddle.replace(" ","")
  demographics_entities_zip_paddle["patientlastname"] = "".join(text_paddle.upper()).strip()
  
 

# first name ******************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (283,94,421,110)
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
  box = (648,93,726,108)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_zip_paddle["patientdob"] = "".join(text_paddle).strip()
  

# zip code *************************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (108,345,149,364)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_zip_paddle["addressszip"] = "".join(text_paddle).strip()
  


# address state *************************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (374,324,423,340)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_zip_paddle["addresssstate"] = "".join(text_paddle.upper()).strip()
  

#PRINTING AND RETURNING DICT**************************************************************************************************************************
  
  #print(demographics_entities_zip_paddle)
  return(demographics_entities_zip_paddle)
  

#demo_zip_entities("/home/ubuntu/test_images/demo/Vision - Pleasant View Surgery Center (2023-03-15 15-12-33.955).tiff")

