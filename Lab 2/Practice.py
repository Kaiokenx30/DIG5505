#%%
twod = (42, 17)
threed = (7, 6, 14)

alist = [1, 2, 3]
alist[0] = 17

alist
# %%
#iterating a tuple
for i in range(5):
    print((i, 2, 3))

# %%

import PIL
from PIL import Image

ourimage = Image.new('RGBA', (100, 100), 'black')

ourimage


# %%
mode = 'RGBA'
size = (100, 100)
color = 'black'
ourimage = Image.new(mode, size, color)

ourimage

#ourimage.save('allblack.png')

# %%
help(Image.new)

# %%
allblack = Image.new('RGB', (100, 100), (50, 0, 0, 255))

allblack
# %%
allblack.putpixel((50, 50), (255, 255, 255, 255))

allblack

#print verticle line
for y in range(allblack.size[0]):
    allblack.putpixel((30, y), (255, 255, 255, 255))
allblack

#%%
for y in range(ourimage.size[0]):
    ourimage.putpixel((20, y), (255,255,255,255))
ourimage
# %%
rectangle = Image.new('RGB', (150, 100))

rectangle

#%%
for x in range(150):
    for y in range(100):
        rectangle.putpixel((x, y), (127, 127, 127, 255))

rectangle

# %%
for x in range(150):
    for y in range(100):
        rectangle.putpixel((x, y), (x, x, x))

rectangle

# %%
#find redness value of an image
def redness(square):
    all_red = 0
    others = 0
    for x in range(100):
        for y in range(100):
            red, green, blue, alpha = square.getpixel((x, y))
            all_red = all_red + red
            others = others + green + blue
    return all_red - (others / 2)

# %%
rectangle.size

# %%
test = Image.new('RGB', (150, 100))

#runthrough image of any size changing the color of it
def grayout(pngimage):
    for x in range(pngimage.size[0]):
        for y in range(pngimage.size[1]):
         pngimage.putpixel((x, y), (127, 127, 127, 255))

grayout(test)

test

# %%
test2 = Image.new('RGB', (300,500))

grayout(test2)

test2

# %%

luigi = Image.open('example.png')

luigi

# %%
grayout(luigi)

luigi

# %%
luigi = Image.open('example.png')

luigi.getpixel((0,0))

def modify(pngimage):
    for x in range(pngimage.size[0]):
        for y in range(pngimage.size[1]):
            (r, g, b) = pngimage.getpixel((x, y))[:3]
            new_color = (r + 64, g + 64, b + 64)
            new_color = new_color + pngimage.getpixel((x, y))[3:]
            pngimage.putpixel((x, y), new_color)

modify(luigi)

luigi
# %%
luigi = Image.open('example.png')

def contrast(pngimage):
    for x in range(pngimage.size[0]):
        for y in range(pngimage.size[1]):
            (r, g, b) = pngimage.getpixel((x, y))[:3]
            new_color = (r + 64, g + 64, b + 64)
            new_color = new_color + pngimage.getpixel((x, y))[3:]
            if r + g + b < 382.5:
                pngimage.putpixel((x, y), (r - 32, g - 32, b - 32))
            else:
                pngimage.putpixel((x, y), (r + 32, g + 32, b + 32))

contrast(luigi)

luigi


# %%
a = 17
b = 2

temp = a
a = b
b = temp

(a, b)

# %%
luigi = Image.open('example.png')

def flip(pngimage):
    width = pngimage.size[0]
    for y in range(pngimage.size[1]):
        for x in range(width):
            left = pngimage.getpixel((x, y))
            right = pngimage.getpixel((width - 1 - x, y))
            pngimage.putpixel((width - 1 - x, y), left)
            pngimage.putpixel((x, y), right)

flip(luigi)

luigi
# %%
#CHAPTER 11
luigi = Image.open('example.png')

#x,y = (460, 395)

around = luigi.getpixel((x - 1, y - 1))[0] + \
luigi.getpixel((x, y - 1))[0] + \
luigi.getpixel((x + 1, y - 1))[0] + \
luigi.getpixel((x - 1, y))[0] + \
luigi.getpixel((x + 1, y))[0] + \
luigi.getpixel((x - 1, y + 1))[0] + \
luigi.getpixel((x, y + 1))[0] + \
luigi.getpixel((x + 1, y + 1))[0]

around = around / 8

around


# %%
around = 0

for c in [0, 1, 2]:
    around = around + \
    luigi.getpixel((x - 1, y - 1))[c] + \
    luigi.getpixel((x, y - 1))[c] + \
    luigi.getpixel((x + 1, y - 1))[c] + \
    luigi.getpixel((x - 1, y))[c] + \
    luigi.getpixel((x + 1, y))[c] + \
    luigi.getpixel((x - 1, y + 1))[c] + \
    luigi.getpixel((x, y + 1))[c] + \
    luigi.getpixel((x + 1, y + 1))[c]

#%%
#function to do above 
def nearby(img, x, y):
    around = 0
    for c in [0, 1, 2]:
        around = around + \
        img.getpixel((x - 1, y - 1))[c] + \
        img.getpixel((x, y - 1))[c] + \
        img.getpixel((x + 1, y - 1))[c] + \
        img.getpixel((x - 1, y))[c] + \
        img.getpixel((x + 1, y))[c] + \
        img.getpixel((x - 1, y + 1))[c] + \
        img.getpixel((x, y + 1))[c] + \
        img.getpixel((x + 1, y + 1))[c]
    return around / 24.0

def differ(img, x, y):
    current = 0
    around = 0
    for c in [0, 1, 2]:
        current = current + img.getpixel((x, y))[c]
        around = around + \
        img.getpixel((x - 1, y - 1))[c] + \
        img.getpixel((x, y - 1))[c] + \
        img.getpixel((x + 1, y - 1))[c] + \
        img.getpixel((x - 1, y))[c] + \
        img.getpixel((x + 1, y))[c] + \
        img.getpixel((x - 1, y + 1))[c] + \
        img.getpixel((x, y + 1))[c] + \
        img.getpixel((x + 1, y + 1))[c]
    return (around / 24.0) - (current / 3.0)

# %%
#blur an image
luigi = Image.open('example.png')

def blur(img):
    blurred = Image.new('RGB', img.size)
    for x in range(1, img.size[0] - 1):
        for y in range(1, img.size[1] - 1):
            (r, g, b) = img.getpixel((x, y))
            change = differ(img, x, y) / 2.0
            change = int(round(change))
            blurred.putpixel((x, y), (r + change, g + change, b + change))
    return blurred


# %%
from PIL import Image
import PIL.ImageOps
#%%
img = Image.open('example.png')

inverted = PIL.ImageOps.invert(img)

inverted
#inverted.save('inverted.png')

# %%
mode = 'RGBA'
size = (100,100)
color = (100,255,255,255)
testimage = Image.new(mode, size, color)

def line(imagename, x, r,g,b,a):
    for y in range(imagename.size[0]):
        imagename.putpixel((x,y),(r,g,b,a))
    
    return imagename


# %%

def thumbnail(img):
    shrink = (img.size[0]/3, img.size[1]/3)

    img.thumbnail(shrink)

    return img

# %%

def bw(img):
    grey = img.convert('L')

    return grey

# %%
