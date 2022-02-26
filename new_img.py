# This program will take two images and create a green screen of the first image on the second image.
from PIL import Image


image_beach = Image.open("beach.jpg")
image_cactus = Image.open("cactus.jpg")


print(image_beach.format, image_beach.size, image_beach.mode) # With this I print 3 things the format , size and mode
print(image_cactus.format, image_cactus.size, image_cactus.mode) # With this I print 3 things the format , size and mode

image_combined = Image.new("RGB", image_beach.size) # This will create a new image with the same size as the first image
(width, height) = image_beach.size # This will store the width and height of the first image in the variables width and height
print(f"Width is: {width}, Height is: {height}") # This will print the width and height of the first image

pixel_beach = image_beach.load() # this will store the pixel of the image in this variable called pixel_beach
pixel_cactus = image_cactus.load() # this will store the pixel of the image in this variable called pixel_cactus


# This is the for loop that will go through the width and height of the first image and will create a new image with the same size.


image_beach.show()
image_cactus.show()
#image_beach.save("combine_image_green.jpg")
# image_combined.show()