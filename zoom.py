from PIL import Image

infile = 'D:\\original_img.jpg'
outfile = 'D:\\adjust_img.jpg'
im = Image.open(infile)
(x,y) = im.size #read image size
x_s = 512 #define standard width
y_s = y * x_s / x #calc height based on standard width
out = im.resize((x_s,y_s),Image.ANTIALIAS) #resize image with high-quality
out.save(outfile)