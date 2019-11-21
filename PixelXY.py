#%%
from PIL import Image
import os

print("Current Working Directory " , os.getcwd())

# %%
#change directory to where you are staoring your images
os.chdir("c:/Users/alexb/DIG5505/XYImages")

print("Current Working Directory " , os.getcwd())

# %%
test = Image.open('Face1.png')

test

# %%
found_pixels = []
for i, pixel in enumerate(Image.Image.getdata(test)):
    if pixel == (255,255,255):
        found_pixels.append(i)

width, height = test.size
x,y = divmod(width, height)

found_pixels_coords = [divmod(width, height) for index in found_pixels]

found_pixels_coords



# %%
