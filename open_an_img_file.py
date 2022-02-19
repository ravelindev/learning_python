from PIL import Image

image_beach = Image.open("beach.jpg")
# image_beach.show()
print(image_beach.format, image_beach.size, image_beach.mode) # With this I print 3 things the format , size and mode

pixel_beach = image_beach.load() # this will store the pixel of the image in this variable called pixel_beach
# print(pixel_beach[0, 0]) # this will print the pixel of the image at the position 0,0

# Retrieve and print out the numbers corresponding to the pixel RGB values for 5 different pixels.
print(pixel_beach[200, 300]) # this will print the pixel of the image at the position 200,300
print(pixel_beach[100, 100]) # this will print the pixel of the image at the position 100,100
print(pixel_beach[300, 200]) # this will print the pixel of the image at the position 300,200
print(pixel_beach[400, 400]) # this will print the pixel of the image at the position 400,400
print(pixel_beach[500, 500]) # this will print the pixel of the image at the position 500,500


# Set a new color value for 5 different pixels.
pixel_beach[200, 300] = (0, 0, 0) # this will change the pixel of the image at the position 200,300 to black
pixel_beach[100, 100] = (255, 255, 255) # this will change the pixel of the image at the position 100,100 to white
pixel_beach[300, 200] = (255, 0, 0) # this will change the pixel of the image at the position 300,200 to red
pixel_beach[400, 400] = (0, 255, 0) # this will change the pixel of the image at the position 400,400 to green
pixel_beach[500, 500] = (0, 0, 255) # this will change the pixel of the image at the position 500,500 to blue


image_beach.show()
































