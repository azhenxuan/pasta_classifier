import os
from PIL import Image,ImageFilter,ImageOps
import PIL

os.chdir("./projects/scraper/google_image_downloader/dataset/macaroni")
print("Current working directory at:",os.getcwd())
new_path = "./reshapedImages"
if not os.path.exists(new_path):
    os.makedirs(new_path)

size = 128,128

for file in os.listdir(os.getcwd()):
    if (file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png")):
        name,ext = os.path.splitext(file)
        img = Image.open(file) # open the image file for editting
        img = ImageOps.grayscale(img) # grayscale image
        new_img = img.resize(size) # resize
        new_img.save("./reshapedImages/"+name+".png") # save under reshapedImages folder
        print("{0} processing done".format(file))
    else:
        continue
