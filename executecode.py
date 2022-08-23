import subprocess
from PIL import Image
import glob
image_list = []
for filename in glob.glob('image/*.jpg'): #assuming jpg
    im=Image.open(filename)
    
    print(im.filename)
    image_list.append(im)
    args="extracttableimage.py " +  im.filename
    subprocess.call(args, shell=True)
