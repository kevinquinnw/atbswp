import Image

image = Image.open('personal.jpg')
image.thumbnail(200,200)
newImage.save('personal_200.jpg')