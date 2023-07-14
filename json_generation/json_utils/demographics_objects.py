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
  box = (138, 97, 1118, 730)
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
  box = (586,38,661,54)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_paddle["mrn"] = "".join(text_paddle).strip()
  
  

# dob_top ****************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (717,37,786,58)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle =text_paddle.replace(" ", '')
  demographics_entities_paddle["patientdob"] = "".join(text_paddle).strip()
  
  
  
#mrn **************************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (85,111,198,138)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_paddle["mrn"] = "".join(text_paddle).strip()
  
  
  
# last name *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (83,94,204,109)
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
  demographics_entities_paddle["patientfirstname"] = "".join(text_paddle).strip()
  

# dob***************************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (648,94,728,109)
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
  box = (508,159,599,177)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_paddle["patientgender"] = "".join(text_paddle).strip()
  


# address *****************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (33,234,216,257)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle = re.sub("BQX","BOX",text_paddle)
  demographics_entities_paddle["addressstreet1"] = "".join(text_paddle.upper()).strip()
  


# city *****************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (223,235,334,259)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  demographics_entities_paddle["addressscity"] = "".join(text_paddle.upper()).strip()
  

  
  
# phone no *****************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (36,420,218,439)
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
  box = (157,510,347,540)
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
    box = (37,521,403,542)
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
  
  #print(demographics_entities_paddle)
  return(demographics_entities_paddle)
  
    

#demo_entities("/home/ubuntu/Advanced_classification/2023-03-22/BROSSARD_JANINE_06_20_1969/DEMO/Vision - Pleasant View Surgery Center (2023-03-22 11-00-11.726).tiff")
