import re
from pathlib                   import Path
from PIL                       import Image,ImageOps
from paddle_ocr_function       import paddle_ocr


CROPPED_IMAGES_DIR = Path("/home/ubuntu/cropped_images/2022-05-19/")
CROPPED_IMAGES_DIR_FIRSTCROP = Path("/home/ubuntu/cropped_images/")




def demo_entities(path):

  file_name = path.split('/')[-1]
  

  cropped_file_path = CROPPED_IMAGES_DIR / file_name
  cropped_file_path.touch()
  cropped_file_path_first = CROPPED_IMAGES_DIR_FIRSTCROP / file_name
  cropped_file_path_first.touch()



# IMAGE CROPPING ****************************************************************************************************************************
  
  image=Image.open(path)
  box = (120, 120, 920, 706)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path_first, dpi=(400,400) , )

  
# dictionary initialising *************************************************************************************************************************
  
  
  demographics_entities_paddle={ }
  demographics_entities_paddle={
                                "mrn"                       :"",
                                "patientlastname"           :"",
                                "patientfirstname"          :"",
                                "patientdob"                :"",
                                "patientmi"                 :"",
                                "patientsuffix"             :"",
                                "patientgender"             :"",
                                "addressstreet1"            :"",
                                "addressstreet2"            :"",
                                "addressscity"              :"",
                                "patientcellphone"          :"",
                                "patienthomephone"          :"",
                                "patientemail"              :"",
                                "languagepreference"        :""
                                
                                }




# mrn_top  ******************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (544,1,602,19)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_paddle["mrn"] = "".join(text_paddle).strip()
  
  

# dob_top ****************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (662,1,721,18)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle =text_paddle.replace(" ", '')
  demographics_entities_paddle["patientdob"] = "".join(text_paddle).strip()
  
  
  
#mrn **************************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (91,80,150,94)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_paddle["mrn"] = "".join(text_paddle).strip()
  
  
  
# last name *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (91,54,199,76)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle=re.sub('[^A-Za-z]+', ' ', text_paddle)
  text_paddle = text_paddle.replace(" ","")
  
  demographics_entities_paddle["patientlastname"] = "".join(text_paddle.upper()).strip()
  
 
  #box = (228,58,406,74)
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
  demographics_entities_paddle["patientfirstname"] = "".join(text_paddle).strip()
  

# dob***************************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (655,56,716,75)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle =text_paddle.replace(" ", '')
  demographics_entities_paddle["patientdob"] = "".join(text_paddle).strip()
  

# mi *************************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (519,60,542,72)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_paddle["patientmi"] = "".join(text_paddle).strip()
  

# suffix ******************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (553,57,620,71)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle = re.sub("Suffix","",text_paddle)
  demographics_entities_paddle["patientsuffix"] = "".join(text_paddle).strip()
  
# gender ***********************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (518,121,592,143)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_paddle["patientgender"] = "".join(text_paddle).strip()
  


# address *****************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (46,201,225,219)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle = re.sub("BQX","BOX",text_paddle)
  demographics_entities_paddle["addressstreet1"] = "".join(text_paddle.upper()).strip()
  


# city *****************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (231,202,337,218)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_paddle["addressscity"] = "".join(text_paddle.upper()).strip()
  

  
  
# phone no *****************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (44,387,257,398)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  #print(text_paddle)
  #print(len(text_paddle))
  #print(text_paddle)
  if ("Mobile" in text_paddle) or ("Mobie" in text_paddle ) or ("Hobie" in text_paddle) or ("Hobile" in text_paddle) or ("Wobile" in text_paddle) :
    text_paddle = re.sub("Mobile.|Mobile|Mobie|Hobie|Hobile|Wobile","",text_paddle)
    demographics_entities_paddle["patientcellphone"] = "".join(text_paddle).strip()
  elif ("Home" in text_paddle) or ("Hone." in text_paddle ):
    text_paddle = re.sub("Hone.|Home.|Home","",text_paddle)
    demographics_entities_paddle["patienthomephone"] = "".join(text_paddle).strip()
  else :
    demographics_entities_paddle["patientcellphone"] = "".join("").strip()
    demographics_entities_paddle["patienthomephone"] = "".join("").strip()
  
  
  
  
  
# email ******************************************************************************************************************************************
  
  
  image=Image.open(cropped_file_path_first)
  box = (157,517,347,535)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  #print(text_paddle)
  text_paddle =text_paddle.replace(" ", '')
  text_paddle = re.sub("EmailI|Email|/","",text_paddle)
  text_paddle = re.sub(".con",".com",text_paddle)
  text_paddle =text_paddle.replace("Home", '')
  text_paddle =text_paddle.replace(".COMA", '.COM')
  text_paddle =text_paddle.replace(".COMV", '.COM')
  text_paddle =text_paddle.replace(".comV", '.com')
  text_paddle =text_paddle.replace(".comY", '.com')
  text_paddle =text_paddle.replace(".netV", '.net')
  text_paddle =text_paddle.replace("Hone", '')
  text_paddle =text_paddle.replace(".comWOH", '.com')
  text_paddle =text_paddle.replace(".comHo", '.com')
  #print(text_paddle)
  text_paddle = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text_paddle)
  demographics_entities_paddle["patientemail"] = "".join(text_paddle).strip()
  
  
  #box = (40,487,338,503)
  if ((len(demographics_entities_paddle["patientemail"])) == 0):
    
    image=Image.open(cropped_file_path_first)
    box = (38,487,338,505)
    cropped_image = image.crop(box)
    img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
    img = Image.open(str(cropped_file_path)).convert('L')
    img = img.save(str(cropped_file_path))
    
    text_paddle= paddle_ocr(cropped_file_path)
    #print(text_paddle)
    text_paddle =text_paddle.replace(" ", '')
    text_paddle =text_paddle.replace(".COMHoneV", '.COM')
    text_paddle =text_paddle.replace("Home", '')
    text_paddle =text_paddle.replace(".COMA", '.COM')
    text_paddle =text_paddle.replace(".COMV", '.COM')
    text_paddle =text_paddle.replace(".comV", '.com')
    text_paddle =text_paddle.replace(".comY", '.com')
    text_paddle =text_paddle.replace(".netV", '.net')
    text_paddle =text_paddle.replace("Hone", '')
    text_paddle =text_paddle.replace(".comWOH", '.com')
    text_paddle =text_paddle.replace(".comHo", '.com')
    text_paddle = re.sub(".con",".com",text_paddle)
    #text_paddle = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-.]+)", text_paddle)
    demographics_entities_paddle["patientemail"] = "".join(text_paddle).strip()
    



  

#PRINTING AND RETURNING DICT**************************************************************************************************************************
  
  
  return(demographics_entities_paddle)
  
    


