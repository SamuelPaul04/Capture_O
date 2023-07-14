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
  box = (120, 120, 920, 706)
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
  box = (542,3,606,20)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  payment["mrn"] = "".join(text_paddle).strip()
  
  

# last name and first name *************************************************************************************************************************************
  
  #image=Image.open(cropped_file_path_first)
  #box = (78,0,244,21)
  #cropped_image = image.crop(box)
  #img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  #text_paddle= paddle_ocr(cropped_file_path)
  #print(text_paddle)
  #try:
    #text_paddle = text_paddle.replace("."," ")
    #text_paddle = text_paddle.replace(","," ")
    #text_paddle = re.split(" ",text_paddle)
    #print(text_paddle)
    #payment["patientlastname"] = "".join(text_paddle[0].upper()).strip()
    #payment["patientfirstname"] = "".join(text_paddle[1].upper()).strip()
  #except:
    
    #payment["patientlastname"] = "".join("").strip()
    #payment["patientfirstname"] = "".join("").strip()  
  


# dob  ****************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (661,4,725,18)
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
  box = (205,460,268,474)
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
  box = (286,459,338,474)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle = re.sub("Perform","Performed",text_paddle)
  text_paddle = re.sub("Periorm","Performed",text_paddle)
  text_paddle = re.sub("Cancele","Canceled",text_paddle)
  text_paddle = re.sub("PartiallN","Partial/Not Billable",text_paddle)
  payment["apptstatus"] = "".join(text_paddle).strip()


# first payer  ****************************************************************************************************************************************
  #image=Image.open(cropped_file_path_first)
  #box = (450,281,680,293)
  #cropped_image = image.crop(box)
  #img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  #text_paddle= paddle_ocr(cropped_file_path)
  #payment["first_payer"] = "".join(text_paddle).strip()



# second payer  ****************************************************************************************************************************************
  #image=Image.open(cropped_file_path_first)
  #box = (450,297,680,310)
  #cropped_image = image.crop(box)
  #img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  #text_paddle= paddle_ocr(cropped_file_path)
  #payment["second_payer"] = "".join(text_paddle).strip()


# third payer  ****************************************************************************************************************************************
  #image=Image.open(cropped_file_path_first)
  #box = (450,314,680,327)
  #cropped_image = image.crop(box)
  #img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  #text_paddle= paddle_ocr(cropped_file_path)
  #payment["third_payer"] = "".join(text_paddle).strip()


# fourth payer  ****************************************************************************************************************************************
  #image=Image.open(cropped_file_path_first)
  #box = (450,331,680,345)
  #cropped_image = image.crop(box)
  #img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  #text_paddle= paddle_ocr(cropped_file_path)
  #payment["fourth_payer"] = "".join(text_paddle).strip()



# first role  ****************************************************************************************************************************************
  #image=Image.open(cropped_file_path_first)
  #box = (718,280,793,294)
  #cropped_image = image.crop(box)
  #img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  #text_paddle= paddle_ocr(cropped_file_path)
  #payment["first_role"] = "".join(text_paddle).strip()



# second role  ****************************************************************************************************************************************
  #image=Image.open(cropped_file_path_first)
  #box = (718,295,793,312)
  #cropped_image = image.crop(box)
  #img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  #text_paddle= paddle_ocr(cropped_file_path)
  #payment["second_role"] = "".join(text_paddle).strip()


# third role  ****************************************************************************************************************************************
  #image=Image.open(cropped_file_path_first)
  #box = (718,314,793,329)
  #cropped_image = image.crop(box)
  #img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  #text_paddle= paddle_ocr(cropped_file_path)
  #payment["third_role"] = "".join(text_paddle).strip()



# fourth role  ****************************************************************************************************************************************
  #image=Image.open(cropped_file_path_first)
  #box = (718,331,793,346)
  #cropped_image = image.crop(box)
  #img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  #text_paddle= paddle_ocr(cropped_file_path)
  #payment["fourth_role"] = "".join(text_paddle).strip()



#PRINTING AND RETURNING DICT**************************************************************************************************************************
  
  return(payment)
 
 
 
