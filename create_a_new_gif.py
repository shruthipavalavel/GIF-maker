import imageio.v3 as iio
from PIL import Image 
import numpy as np    

TARGET_SIZE = (1000, 1000) 
filenames = ['3.png', '4.png', '5.png']
images = [ ]

for filename in filenames:
    
    img = Image.open(filename)
    
    
    resized_img = img.resize(TARGET_SIZE, Image.LANCZOS)
    
    
    images.append(np.array(resized_img))


iio.imwrite('bunny.gif', images, duration = 500, loop = 0)

print("Bunny.gif created successfully!")