# Mandelbrot Set Coloring Test
# Kevin Xie CS550 

from PIL import Image
import math

imgx,imgy=2000,2000 # IMAGE DIMENSIONSd
tmax=35 # MAXIMUM ITERATIONS

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
		if t<=tmax//4: # COLORING
			image.putpixel((x,y),((255//tmax)*(t+tmax//2),(194//tmax)*(t+tmax//2),(0//tmax)*(t+tmax//2))) 
		elif t<=tmax//2:
			image.putpixel((x,y),((253//tmax)*(t+tmax//4),(95//tmax)*(t+tmax//4),(0//tmax)*(t+tmax//4))) 
		else:
			image.putpixel((x,y),((255//tmax)*t,(10//tmax)*t,(255//tmax)*t))

image.save("mandelbrottest.png") # SAVES IMAGE