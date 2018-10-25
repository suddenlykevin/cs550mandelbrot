# Mandelbrot Set
# Kevin Xie CS550 

from PIL import Image

imgx,imgy=512,512 # IMAGE DIMENSIONS
tmax=256 # MAXIMUM ITERATIONS
xa,xb=-0.7499824459876544,-0.7495954089506173
ya,yb=0.02517525077160492,0.025562287808641955

image = Image.new("RGB",(imgx,imgy)) # CREATES IMAGE ACCORDING TO DIMENSIONS

for x in range(imgx): 
	cx=(x*(xb-xa)/(imgx-1)+xa)
	for y in range(imgy): # CYCLE THROUGH EACH PIXEL
		cy=(y*(yb-ya)/(imgy-1)+ya)
		zi, zx = 0, 0 # RESETS VARIABLS (Zn and ITERATION NUM.)
		for t in range(tmax):
			absz=float(((zx**2)+(zi**2))**0.5) # CALCULATES abs(Zn+1) acc. PDF
			if absz>=2.0: # IF abs(Zn+1)>=2, THEN Z HAS ESCAPED
				break
			zx,zi=float((zx*zx-zi*zi)+cx),float((zi*zx+zx*zi)+cy) # CALCULATES Zn+1 acc. PDF
		R,G,B=(t*24)%256,(t*35)%256,t
		image.putpixel((x,y),(R,G,B)) # GLOWY MANDELBROT EFFECT

image.save("mandelbrot.png") # SAVES IMAGE