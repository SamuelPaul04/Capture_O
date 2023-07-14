import re
from pathlib                   import Path
from PIL                       import Image,ImageOps
from paddle_ocr_function       import paddle_ocr



CROPPED_IMAGES_DIR = Path("/home/ubuntu/cropped_images/2022-05-19/")
CROPPED_IMAGES_DIR_FIRSTCROP = Path("/home/ubuntu/cropped_images/")


def payment(path):

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
  
  payment = {}
  payment = {
                "mrn"                   :"",
                #"patientlastname"       :"",
                #"patientfirstname"      :"",
                "patientdob"            :"",
                "dateofservice"         :"",        
                "apptstatus"            :"",
                #"first_payer"           :"",
                #"second_payer"          :"",
                #"third_payer"           :"",
                #"fourth_payer"          :"",
                #"first_role"            :"",
                #"second_role"           :"",
                #"third_role"            :"",
                #"fourth_role"            :"",
            
            }



# mrn ******************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (587,38,657,52)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  payment["mrn"] = "".join(text_paddle).strip()
  
  

  


# dob  ****************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (717,38,781,52)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle = re.sub('[^0-9/]+','', text_paddle)
  text_paddle =text_paddle.replace(" ", '')
  payment["patientdob"] = "".join(text_paddle).strip()
  
  
  
# dos  ****************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (199,494,271,510)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle = re.sub('[^0-9/]+','', text_paddle)
  text_paddle =text_paddle.replace(" ", '')
  payment["dateofservice"] = "".join(text_paddle).strip()
  
  
  
  
  
# case status  ****************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (279,493,342,508)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle = re.sub("Perform","Performed",text_paddle)
  text_paddle = re.sub("Periorm","Performed",text_paddle)
  text_paddle = re.sub("Cancele","Canceled",text_paddle)
  text_paddle = re.sub("PartiallN","Partial/Not Billable",text_paddle)
  payment["apptstatus"] = "".join(text_paddle).strip()



  #print(payment)
  return(payment)
 
 
#payment("/home/ubuntu/test_images/payment/Vision - Pleasant View Surgery Center (2023-03-15 15-13-31.131).tiff")
