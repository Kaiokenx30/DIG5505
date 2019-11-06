#%%
import numpy
import PIL
from PIL import Image
import random
#found at https://www.programcreek.com/python/example/89902/PIL.Image.fromarray
def salt_pepper(density):
    imarray = numpy.random.rand(density,density,3) * 255
    return Image.fromarray(imarray.astype('uint8')).convert('L')

salt_pepper(50)

# %%
#runthrough image of any size changing the color of it
def greyout(width,height):
    example = Image.new('RGB', (width, height), (50, 0, 0, 255))
    for x in range(width):
        for y in range(height):
         example.putpixel((x, y), (random.randint(0,255), random.randint(0,255), random.randint(0,255), 255))
    return example

greyout(50,200)
# %%
