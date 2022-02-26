# Author: Rudy Ravelin
# Date: 4/20/2020
# Description: This program will take a user inputted image and create a new image with the same dimensions
#              but with a new color.

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


# This is where the magic happens

for x in range(0, width): # This will go through the width of the first image
    for y in range(0, height): # This will go through the height of the first image
        (r, g, b) = pixel_beach[x, y] # This will store the RGB of the first image in the variables r, g and b
        (r2, g2, b2) = pixel_cactus[x, y] # This will store the RGB of the second image in the variables r2, g2 and b2
        if r2 <= 150 and g2 >= 215 and b2 <= 60: # This will check if the red value of the second image is less than 150 and the green value of the second image is greater than 215 and the blue value of the second image is less than 60
            pixel_cactus[x, y] = (r2, g2, b2) # This will set the RGB of the second image to the RGB of the first image
        else: # This will check if the red value of the second image is greater than 150 and the green value of the second image is less than 215 and the blue value of the second image is greater than 60
            pixel_cactus[x, y] = (r2, g2, b2) # This will set the RGB of the second image to the RGB of the first image
            r = r2 # This will set the red value of the first image to the red value of the second image
            g = g2 # This will set the green value of the first image to the green value of the second image
            b = b2 # This will set the blue value of the first image to the blue value of the second image
        image_combined.putpixel((x, y), (r, g, b)) # This will set the RGB of the first image to the new RGB values



image_beach.show() # This will show the first image
image_cactus.show() # This will show the second image
image_combined.save("combine_image.jpg") # This will save the new image
image_combined.show() # This will show the new image

