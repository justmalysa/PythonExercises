from PIL import Image
import os

def get_current_path():
   return os.path.dirname(os.path.realpath(__file__))

im1 = Image.open(os.path.join(get_current_path(), 'IMG_2701.jpg'))
im1.save(os.path.join(get_current_path(), 'image1.png'))
