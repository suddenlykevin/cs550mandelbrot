from PIL import Image


imgx,imgy=1024,1024 # IMAGE DIMENSIONS
image = Image.new("RGB",(imgx,imgy)) # CREATES IMAGE ACCORDING TO DIMENSIONS

for x in range(imgx):
	for y in range(imgy):
		R,G,B=int(255-(80*x/imgx)),int(179-(179*x/imgx)),int(15+(75*x/imgx))
		image.putpixel((x,y),(R,G,B)) # GLOWY MANDELBROT EFFECT
image.save("gradient.png") # SAVES IMAGE