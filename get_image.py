import base64
from utils import uploadStorage, base64_split
import io
import os

uploadStorage('kaos.jpg', 'kaos.jpg')
if os.path.exists("image.png"):
  os.remove("image.png")
else:
  print("The file does not exist")
