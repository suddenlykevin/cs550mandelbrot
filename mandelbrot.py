from PIL import Image
import math

imgx,imgy=2000,2000 # IMAGE DIMENSIONSd
tmax=120 # MAXIMUM ITERATIONS
R,G,B=255,255,255

image = Image.new("RGB",(imgx,imgy)) # CREATES IMAGE ACCORDING TO DIMENSIONS

for x in range(imgx): 
	for y in range(imgy): # CYCLE THROUGH EACH PIXEL
		t, zi, zx = 0, 0, 0 # RESETS VARIABLS (Zn and ITERATION NUM.)
		while True:
			zx,zi=float((zx*zx-zi*zi)+(x-imgx/2)/(imgx/4)),float((zi*zx+zx*zi)+(y-imgy/2)/(imgy/4)) # CALCULATES Zn+1 acc. PDF
			absz=float(math.sqrt((zx**2)+(zi**2))) # CALCULATES abs(Zn+1) acc. PDF
			t+=1 # COUNTS ITERATIONS (NUM OF TRIES)
			if absz>=2.0: # IF abs(Zn+1)>=2, THEN Z HAS ESCAPED
				break
			elif t==tmax: # IF MAX. ITERATIONS REACHED AND Z HAS NOT ESCAPED
				break
		image.putpixel((x,y),((R//tmax)*t,(G//tmax)*t,(B//tmax)*t)) # GLOWY MANDELBROT EFFECT

image.save("mandelbrot.png") # SAVES IMAGE