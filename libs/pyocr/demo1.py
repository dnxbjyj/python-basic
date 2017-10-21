# coding:utf-8
# 识别一个图片中的数字
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import pytesseract
from PIL import Image

print pytesseract.image_to_string(Image.open('./img1.png'))