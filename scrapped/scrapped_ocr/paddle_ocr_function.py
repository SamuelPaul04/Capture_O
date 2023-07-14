from paddleocr                 import PaddleOCR
from PIL                       import Image


ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)

def paddle_ocr(cropped_file_path):
  
  result = ocr.ocr(str(cropped_file_path), cls=True)
  #print(result)
  Image.open(str(cropped_file_path)).convert('L')
  txts = [line[1][0] for line in result]
  text_paddle =" ".join(txts).strip()
  
  return text_paddle