#%%
import random
from PIL import Image

mode = 'RGBA'
size = (100,100)
color = (100,255,255,255)
ourimage = Image.new(mode, size, color)
ourimage

#%% 


for x in range(ourimage.size[0]):
    for y in range(ourimage.size[1]):
        value = float(x)/ourimage.size[0]
        value = int(value*255.0)
        ourimage.putpixel((x,y),(value, value, value, 255))
ourimage


#%%

ourimage.getpixel((59,50))

#%%

def flip(pngimage):
    width = pngimage.size[0]
    for y in range(pngimage.size[1]):
        for x in range(width):
            left = pngimage.getpixel((x, y))
            right = pngimage.getpixel((width - 1 - x, y))
            pngimage.putpixel((width - 1 - x, y), left)
            pngimage.putpixel((x, y), right)

testimage = Image.open('flipme.png')
flip(testimage)
testimage

#%%
mode = 'RGBA'
size = (100,100)
color = (100,255,255,255)
testimage = Image.new(mode, size, color)

testimage

def line(imagename, value, r,g,b,a):
    for y in range(imagename.size[1]):
        imagename.putpixel((0,y),(r,g,b,a))
    
    imagename

# %%
