# Hello World program in Python
    
from PIL import Image
import pickle

image = Image.open('dice.png')
size = width, height = image.size

thelist = list(image.getdata())
with open("output.txt", "wb") as my_file:
    for item in thelist:
        my_file.write(str(item) + "\n")

output = open('out.dump', 'wb')
pickle.dump(thelist, output)

output.close
file.close
del image
