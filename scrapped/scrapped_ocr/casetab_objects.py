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
  box = (120, 120, 1020, 706)
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
  box = (544,4,610,18)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )

  text_paddle= paddle_ocr(cropped_file_path)
  casetab_entities_paddle["mrn"] = "".join(text_paddle).strip()
  

# dob_top ****************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (665,3,724,19)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle_dob_top= paddle_ocr(cropped_file_path)
  text_paddle_dob_top =text_paddle_dob_top.replace(" ", '')
  casetab_entities_paddle["patientdob"] = "".join(text_paddle_dob_top).strip()
  
  
  
#mrn **************************************************************************************************************************************************
  image=Image.open(cropped_file_path_first)
  box = (69,51,144,71)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  casetab_entities_paddle["mrn"] = "".join(text_paddle).strip()
  
  
  
# last name *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (233,52,344,70)
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
  box = (429,54,542,68)
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
  box = (749,52,807,71)
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
  box = (73,79,140,98)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle =text_paddle.replace(" ", '')
  casetab_entities_paddle["dateofservice"] = "".join(text_paddle).strip()
  

# start time ******************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (362,78,436,95)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle=  paddle_ocr(cropped_file_path)
  text_paddle = text_paddle.replace(".", '')
  text_paddle = text_paddle.replace(":", '')
  text_paddle = text_paddle[:2] + ":" + text_paddle[2:]
  casetab_entities_paddle["apptscheduledtime"] = "".join(text_paddle).strip()
  

# end time ***********************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (486,79,553,95)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  text_paddle = text_paddle.replace(".", '')
  text_paddle = text_paddle.replace(":", '')
  text_paddle = text_paddle[:2] + ":" + text_paddle[2:]
  
  casetab_entities_paddle["apptscheduledendtime"] = "".join(text_paddle).strip()
  


# cleanup *****************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (739,77,777,93)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  casetab_entities_paddle["cleanuptime"] = "".join(text_paddle).strip()
  

  if (len(casetab_entities_paddle["cleanuptime"]) == 0):
    casetab_entities_paddle["cleanuptime"] = "".join("0").strip()
  


# surgeon *****************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (90,100,220,119)
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
  box = (329,103,444,121)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle= paddle_ocr(cropped_file_path)
  casetab_entities_paddle["servicetype"] = "".join(text_paddle).strip()
  
  
  
# PROCEDURE1 
  
  
# code ******************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (63,252,139,268)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  code = paddle_ocr(cropped_file_path)
  

 # description ***************************************************************************************************************************************
  #box = (57,271,524,293)
  image=Image.open(cropped_file_path_first)
  box = (60,269,524,291)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  
  description = paddle_ocr(cropped_file_path)
  

# dx codes ************************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (625,284,684,298)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  dxcodes_p_1 = paddle_ocr(cropped_file_path)

  
# dx codes *******************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (722,284,779,299)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  img = Image.open(str(cropped_file_path)).convert('L')
  img = img.save(str(cropped_file_path))
  
  dxcodes_p_2 = paddle_ocr(cropped_file_path)

  
  
# dx codes **********************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (818,286,866,296)
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
  box = (64,331,121,351)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  code = paddle_ocr(cropped_file_path)

  

# description *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (60,354,524,372)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  description = paddle_ocr(cropped_file_path)

  


# dx codes ****************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (627,365,678,382)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  dxcodes_p2_1 = paddle_ocr(cropped_file_path)

  
  
# dx codes *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (724,364,772,384)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  
  dxcodes_p2_2 = paddle_ocr(cropped_file_path)

  
  
  
# dx codes *******************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (818,363,868,383)
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
  box = (71,435,110,450)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  code = paddle_ocr(cropped_file_path)

  

# description *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (290,436,806,450)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  description = paddle_ocr(cropped_file_path)

  


# bodyside
  image=Image.open(cropped_file_path_first)
  box = (805,439,854,452)
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
  box = (71,455,110,470)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  code = paddle_ocr(cropped_file_path)
  print(code)
  

# description *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (290,455,806,468)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  description = paddle_ocr(cropped_file_path)

  


# bodyside
  image=Image.open(cropped_file_path_first)
  box = (806,455,853,469)
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
  box = (71,474,110,488)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  code = paddle_ocr(cropped_file_path)

  

# description *************************************************************************************************************************************
  
  image=Image.open(cropped_file_path_first)
  box = (290,472,806,485)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  description = paddle_ocr(cropped_file_path)

  


# bodyside
  image=Image.open(cropped_file_path_first)
  box = (806,475,853,489)
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
  box = (15,499,227,515)
  cropped_image = image.crop(box)
  img=cropped_image.save(cropped_file_path, dpi=(400,400) , )
  
  text_paddle = paddle_ocr(cropped_file_path)
  text_paddle =re.sub("AnesthesiaType|Anesthesia Type", '',  text_paddle)
  casetab_entities_paddle["anesthesiatype"] = "".join(text_paddle.upper()).strip()
  
  




#PRINTING AND RETURNING DICT**************************************************************************************************************************
  
  casetab_entities_paddle["Procedures"]=casetab.copy()
  
  #print(casetab_entities_paddle)
  return(casetab_entities_paddle)
  
  
  
  
  
#casetab_entities("/home/ubuntu/Vision - Pleasant View Surgery Center (2023-03-13 13-40-46.971).tiff")
  