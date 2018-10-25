# Julia Set
# Kevin Xie CS550 

from PIL import Image, ImageFilter
import colorsys

imgx,imgy=512,512 # IMAGE DIMENSIONS
tmax=256 # MAXIMUM ITERATIONS
xa,xb=-0.1475,-0.1425
ya,yb=0.255,0.26

image = Image.new("RGB",(imgx,imgy)) # CREATES IMAGE ACCORDING TO DIMENSIONS

cx,cy=-.79,.15
for x in range(imgx): 
	for y in range(imgy): # CYCLE THROUGH EACH PIXEL
		zi, zx = (y*(yb-ya)/(imgy-1)+ya) , (x*(xb-xa)/(imgx-1)+xa) # RESETS VARIABLS (Zn and ITERATION NUM.)
		for t in range(tmax):
			absz=float(((zx**2)+(zi**2))**0.5) # CALCULATES abs(Zn+1) acc. PDF
			if absz>=2.0: # IF abs(Zn+1)>=2, THEN Z HAS ESCAPED
				break
			zx,zi=float((zx*zx-zi*zi)+cx),float((zi*zx+zx*zi)+cy) # CALCULATES Zn+1 acc. PDF
		if t!=tmax-1:
			R,G,B = int(colorsys.hsv_to_rgb((0.813333-(t/tmax))%1,1,1)[0]*255), int(colorsys.hsv_to_rgb((0.813333-(t/tmax))%1,1,1)[1]*255), int(colorsys.hsv_to_rgb((0.813333-(t/tmax))%1,1,1)[2]*255)
		image.putpixel((x,imgy-1-y),(R,G,B))

image.save("julia.png")