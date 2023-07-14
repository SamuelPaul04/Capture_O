import re
from pathlib                   import Path
from PIL                       import Image,ImageOps
from paddle_ocr_function       import paddle_ocr

        


CROPPED_IMAGES_DIR = Path("/home/ubuntu/cropped_images/2022-05-19/")
CROPPED_IMAGES_DIR_FIRSTCROP = Path("/home/ubuntu/cropped_images/")


def casetab_entities(path):

  file_name = path.split('/')[-1]
  
  cropped_file_path = CROPPED_IMAGES_DIR / file_name
  cropped_file_path.touch()
  cropped_file_path_first = CROPPED_IMAGES_DIR_FIRSTCROP / file_name
  cropped_file_path_first.touch()

# IMAGE CROPPING ***************************************************************************************************************************************
  
  image=Image.open(path)
  box = (138, 97, 1118, 730)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path_first, dpi=(400,400) , )

  
# initialising dictionary ********************************************************************************************************************************
  
  
  casetab_entities_paddle={ }
  casetab=[]
  casetab_entities_paddle={
                              "mrn"                      :"",
                              "patientlastname"          :"",
                              "patientfirstname"         :"",
                              "servicetype"              :"",
                              "patientdob"               :"",
                              "patientgender"            :"",
                              "dateofservice"            :"",
                              "apptscheduledtime"        :"",   
                              "apptscheduledendtime"     :"",
                              "cleanuptime"              :"",
                              "anesthesiatype"           :"",
                              "providerlastname"         :"",
                              "providerfirstname"        :""                       
                          }



# mrn_top  ******************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (587,37,662,54)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )

  text_paddle= paddle_ocr(cropped_file_path)
  casetab_entities_paddle["mrn"] = "".join(text_paddle).strip()
  

# dob_top ****************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (716,37,788,54)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle_dob_top= paddle_ocr(cropped_file_path)
  text_paddle_dob_top =text_paddle_dob_top.replace(" ", '')
  casetab_entities_paddle["patientdob"] = "".join(text_paddle_dob_top).strip()
  
  
  
#mrn **************************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (64,89,146,108)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  casetab_entities_paddle["mrn"] = "".join(text_paddle).strip()
  
  
  
# last name *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (222,90,338,104)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle=re.sub('[^A-Za-z-]+', ' ', text_paddle)
  text_paddle = text_paddle.replace(" ","")
  casetab_entities_paddle["patientlastname"] = "".join(text_paddle.upper()).strip()
  
 
  
# first name ******************************************************************************************************************************************
  #box = (431,54,534,69)
  image=Image.open(cropped_file_path_first)
  box = (421,90,555,105)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle=re.sub('[^A-Za-z-]+', ' ', text_paddle)
  text_paddle = text_paddle.replace(" ","")
  text_paddle = text_paddle.replace("THTTWIY","TIMOTHY")
  text_paddle = text_paddle.replace("THTTTY","TIMOTHY")
  casetab_entities_paddle["patientfirstname"] = "".join(text_paddle.upper()).strip()
  

# dob***************************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (737,88,808,104)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle =text_paddle.replace(" ", '')
  if len(text_paddle_dob_top) < 10:
    casetab_entities_paddle["patientdob"] = "".join(text_paddle).strip()
  


# gender***************************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (804,6,899,17)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  #print(text_paddle)
  casetab_entities_paddle["patientgender"] = "".join(text_paddle).strip()
  
  


# dos *************************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (62,116,128,132)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle =text_paddle.replace(" ", '')
  casetab_entities_paddle["dateofservice"] = "".join(text_paddle).strip()
  

# start time ******************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (356,113,421,132)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle=  paddle_ocr(cropped_file_path)
  text_paddle = text_paddle.replace(".", '')
  text_paddle = text_paddle.replace(":", '')
  text_paddle = text_paddle[:2] + ":" + text_paddle[2:]
  casetab_entities_paddle["apptscheduledtime"] = "".join(text_paddle).strip()
  

# end time ***********************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (477,113,539,130)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle = text_paddle.replace(".", '')
  text_paddle = text_paddle.replace(":", '')
  text_paddle = text_paddle[:2] + ":" + text_paddle[2:]
  
  casetab_entities_paddle["apptscheduledendtime"] = "".join(text_paddle).strip()
  


# cleanup *****************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (728,112,762,129)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  casetab_entities_paddle["cleanuptime"] = "".join(text_paddle).strip()
  

  if (len(casetab_entities_paddle["cleanuptime"]) == 0):
    casetab_entities_paddle["cleanuptime"] = "".join("0").strip()
  


# surgeon *****************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (80,137,208,155)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle = ""
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle = re.sub(",", " ",  text_paddle)
  text_paddle = text_paddle.split()
  
  try:
    providerlastname = "".join(text_paddle[0]).strip()
    providerlastname = providerlastname.replace("SHBLEY","SHIBLEY")
    casetab_entities_paddle["providerlastname"] = "".join(providerlastname).strip()
    casetab_entities_paddle["providerfirstname"] = "".join(text_paddle[1]).strip()
  except:
    casetab_entities_paddle["providerlastname"] = "".join("").strip()
    casetab_entities_paddle["providerfirstname"] = "".join("").strip()
  
  
  
  
# service type *****************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (320,135,431,157)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  casetab_entities_paddle["servicetype"] = "".join(text_paddle).strip()
  
  
  
# PROCEDURE1 
  
  
# code ******************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (53,290,134,302)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  code = paddle_ocr(cropped_file_path)
  

 # description ***************************************************************************************************************************************
  #box = (57,271,524,293)
  image=Image.open(cropped_file_path_first)
  box = (53,310,414,325)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  
  description = paddle_ocr(cropped_file_path)
  

# dx codes ************************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (618,320,673,342)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  dxcodes_p_1 = paddle_ocr(cropped_file_path)

  
# dx codes *******************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (712,321,768,337)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  dxcodes_p_2 = paddle_ocr(cropped_file_path)

  
  
# dx codes **********************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (808,322,864,340)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  dxcodes_p_3 = paddle_ocr(cropped_file_path)

  
  
# bodyside
  bodyside = ""
  if "LT" in description:
          bodyside ="".join("L").strip()
  elif  "Left"   in description:
          bodyside ="".join("L").strip()
  elif  "Lt"   in description:
          bodyside ="".join("L").strip()
  elif  "LEFT"   in description:
          bodyside ="".join("L").strip()
  elif  "Leit"   in description:
          bodyside ="".join("L").strip()
  elif "left" in description:
          bodyside ="".join("L").strip()
  elif "leit" in description:
          bodyside ="".join("L").strip()
  elif "L)" in description:
          bodyside ="".join("L").strip()
  elif "Le" in description:
          bodyside ="".join("L").strip()
  elif "Right" in description:
          bodyside ="".join("R").strip()
  elif "RIGHT" in description:
          bodyside ="".join("R").strip()
  elif "RT" in description:
          bodyside ="".join("R").strip()
  elif "right" in description:
          bodyside ="".join("R").strip()
  elif "Bilateral" in description:
          bodyside ="".join("B").strip()
  elif "BILATERAL" in description:
          bodyside ="".join("B").strip()
  elif "Pight" in description:
          bodyside ="".join("R").strip()
  elif "Righ" in description:
          bodyside ="".join("R").strip()
  else :
          bodyside ="".join("NA").strip()
  
  
  dxcodes = [dxcodes_p_1,dxcodes_p_2,dxcodes_p_3]
  
  
  if (len(code) == 5):
    casetab.append({"code": code ,"description":description ,"bodyside":bodyside ,"Dxcodes":dxcodes})
  

# PROCEDURE2
  
  
# code *********************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (53,368,117,389)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  code = paddle_ocr(cropped_file_path)

  

# description *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (54,392,509,408)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  description = paddle_ocr(cropped_file_path)

  


# dx codes ****************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (618,399,671,417)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  dxcodes_p2_1 = paddle_ocr(cropped_file_path)

  
  
# dx codes *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (716,400,764,417)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  
  dxcodes_p2_2 = paddle_ocr(cropped_file_path)

  
  
  
# dx codes *******************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (811,402,859,417)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  
  dxcodes_p2_3 = paddle_ocr(cropped_file_path)
  
  
  
  if "LT" in description:
          bodyside ="".join("L").strip()
  elif  "Left"   in description:
          bodyside ="".join("L").strip()
  elif  "LEFT"   in description:
          bodyside ="".join("L").strip()
  elif  "Leit"   in description:
          bodyside ="".join("L").strip()
  elif  "leit"   in description:
          bodyside ="".join("L").strip()
  elif "left" in description:
          bodyside ="".join("L").strip()
  elif "L)" in description:
          bodyside ="".join("L").strip()
  elif "Right" in description:
          bodyside ="".join("R").strip()
  elif "RIGHT" in description:
          bodyside ="".join("R").strip()
  elif "RT" in description:
          bodyside ="".join("R").strip()
  elif "right" in description:
          bodyside ="".join("R").strip()
  elif "Bilateral" in description:
          bodyside ="".join("B").strip()
  elif "BILATERAL" in description:
          bodyside ="".join("B").strip()
  elif "Pight" in description:
          bodyside ="".join("R").strip()
  else :
          bodyside ="".join(bodyside).strip()
  
  dxcodes = [ dxcodes_p2_1 , dxcodes_p2_2 , dxcodes_p2_3 ]
  
  
  if (len(code) == 5):
    casetab.append({"code": code ,"description":description ,"bodyside":bodyside ,"Dxcodes":dxcodes})
  
  


# PROCEDURE3
  
  
# code *********************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (63,471,107,486)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  code = paddle_ocr(cropped_file_path)

  

# description *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (287,471,795,486)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  description = paddle_ocr(cropped_file_path)

  


# bodyside
  image=Image.open(cropped_file_path_first)
  box = (795,469,866,485)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  body_side = paddle_ocr(cropped_file_path)
  
  
  
  if "LT" in body_side:
          body_side ="".join("L").strip()
  elif  "Left"   in body_side:
          body_side ="".join("L").strip()
  elif  "LEFT"   in body_side:
          body_side ="".join("L").strip()
  elif  "Leit"   in body_side:
          body_side ="".join("L").strip()
  elif  "leit"   in body_side:
          body_side ="".join("L").strip()
  elif "left" in body_side:
          body_side ="".join("L").strip()
  elif "L)" in body_side:
          body_side ="".join("L").strip()
  elif "Right" in body_side:
          body_side ="".join("R").strip()
  elif "RIGHT" in body_side:
          body_side ="".join("R").strip()
  elif "RT" in body_side:
          body_side ="".join("R").strip()
  elif "right" in body_side:
          bodyside ="".join("R").strip()
  elif "Bilateral" in body_side:
          body_side ="".join("B").strip()
  elif "BILATERAL" in body_side:
          body_side ="".join("B").strip()
  elif "Pight" in body_side:
          body_side ="".join("R").strip()
  else :
          body_side ="".join("").strip()
  
  
  dxcodes = [ "" , "" , "" ]
  
  if (len(code) == 5):
    casetab.append({"code": code ,"description":description ,"bodyside":body_side ,"Dxcodes":dxcodes})
  



# PROCEDURE4
  
  
# code *********************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (61,490,105,504)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  code = paddle_ocr(cropped_file_path)
  print(code)
  

# description *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (286,487,796,504)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  description = paddle_ocr(cropped_file_path)

  


# bodyside
  image=Image.open(cropped_file_path_first)
  box = (796,487,865,504)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  body_side = paddle_ocr(cropped_file_path)
  
  
  
  if "LT" in body_side:
          body_side ="".join("L").strip()
  elif  "Left"   in body_side:
          body_side ="".join("L").strip()
  elif  "LEFT"   in body_side:
          body_side ="".join("L").strip()
  elif  "Leit"   in body_side:
          body_side ="".join("L").strip()
  elif  "leit"   in body_side:
          body_side ="".join("L").strip()
  elif "left" in body_side:
          body_side ="".join("L").strip()
  elif "L)" in body_side:
          body_side ="".join("L").strip()
  elif "Right" in body_side:
          body_side ="".join("R").strip()
  elif "RIGHT" in body_side:
          body_side ="".join("R").strip()
  elif "RT" in body_side:
          body_side ="".join("R").strip()
  elif "right" in body_side:
          bodyside ="".join("R").strip()
  elif "Bilateral" in body_side:
          body_side ="".join("B").strip()
  elif "BILATERAL" in body_side:
          body_side ="".join("B").strip()
  elif "Pight" in body_side:
          body_side ="".join("R").strip()
  else :
          body_side ="".join("").strip()
  
  
  dxcodes = [ "" , "" , "" ]
  
  if (len(code) == 5):
    casetab.append({"code": code ,"description":description ,"bodyside":body_side ,"Dxcodes":dxcodes})



# PROCEDURE5
  
  
# code *********************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (61,507,111,522)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  code = paddle_ocr(cropped_file_path)

  

# description *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (283,506,798,519)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  description = paddle_ocr(cropped_file_path)

  


# bodyside
  image=Image.open(cropped_file_path_first)
  box = (798,505,866,521)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  body_side = paddle_ocr(cropped_file_path)
  
  
  
  if "LT" in body_side:
          body_side ="".join("L").strip()
  elif  "Left"   in body_side:
          body_side ="".join("L").strip()
  elif  "LEFT"   in body_side:
          body_side ="".join("L").strip()
  elif  "Leit"   in body_side:
          body_side ="".join("L").strip()
  elif  "leit"   in body_side:
          body_side ="".join("L").strip()
  elif "left" in body_side:
          body_side ="".join("L").strip()
  elif "L)" in body_side:
          body_side ="".join("L").strip()
  elif "Right" in body_side:
          body_side ="".join("R").strip()
  elif "RIGHT" in body_side:
          body_side ="".join("R").strip()
  elif "RT" in body_side:
          body_side ="".join("R").strip()
  elif "right" in body_side:
          bodyside ="".join("R").strip()
  elif "Bilateral" in body_side:
          body_side ="".join("B").strip()
  elif "BILATERAL" in body_side:
          body_side ="".join("B").strip()
  elif "Pight" in body_side:
          body_side ="".join("R").strip()
  else :
          body_side ="".join("").strip()
  
  
  dxcodes = [ "" , "" , "" ]
  
  if (len(code) == 5):
    casetab.append({"code": code ,"description":description ,"bodyside":body_side ,"Dxcodes":dxcodes})
  






# anesthesia type **************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (97,535,214,554)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle = paddle_ocr(cropped_file_path)
  text_paddle =re.sub("AnesthesiaType|Anesthesia Type", '',  text_paddle)
  casetab_entities_paddle["anesthesiatype"] = "".join(text_paddle.upper()).strip()
  
  




#PRINTING AND RETURNING DICT**************************************************************************************************************************
  
  casetab_entities_paddle["Procedures"]=casetab.copy()
  
  #print(casetab_entities_paddle)
  return(casetab_entities_paddle)
  
  
  
  
  
#casetab_entities("/home/ubuntu/test_images/case/Vision - Pleasant View Surgery Center (2023-03-15 10-09-01.478) (1).tiff")
  
  