from wand.image import Image
with Image(filename = 'img/example.jpg') as img:
    img.resize(300,300) # width, height
    img.save(filename = 'img/result1.png') # png, jpg, bmp, gif, tiff All OK