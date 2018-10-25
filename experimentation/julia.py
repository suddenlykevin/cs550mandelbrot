# Julia Set
# Kevin Xie CS550 

from PIL import Image, ImageFilter
import colorsys

imgx,imgy=512,512 # IMAGE DIMENSIONS
tmax=256 # MAXIMUM ITERATIONS
xa3,xb3=-0.1475,-0.1425
ya3,yb3=0.255,0.26

image = Image.new("RGB",(imgx,imgy)) # CREATES IMAGE ACCORDING TO DIMENSIONS

cx,cy=-.79,.15
for x in range(imgx): 
	for y in range(imgy):
		# Z starts at X,Y instead of 0,0
		zx = (x*(xb3-xa3)/(imgx-1)+xa3) 
		zi = (y*(yb3-ya3)/(imgy-1)+ya3)
		for t in range(tmax):
			# same equations as Mandelbrot
			absz=float(((zx**2)+(zi**2))**0.5) 
			if absz>=2.0: 
				break
			zx,zi=float((zx*zx-zi*zi)+cx),float((zi*zx+zx*zi)+cy)
		# cycles through HSV starting from yellow
		R,G,B = int(colorsys.hsv_to_rgb((0.297222-(t/tmax))%1,1,1.36)[0]*255), int(colorsys.hsv_to_rgb((0.297222-(t/tmax))%1,1,1.36)[1]*255), int(colorsys.hsv_to_rgb((0.297222-(t/tmax))%1,1,1.36)[2]*255)
		image.putpixel((x,imgy-1-y),(R,G,B))

image.save("julia.png")