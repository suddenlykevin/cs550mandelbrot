# Mandelbrot Set
# Kevin Xie CS550 
#
# In this project, we used Mandelbrot and other fractal sets to visualize and
# colorize fractals. My first Mandelbrot set is colored as inspired by the album
# artwork of Tame Impala's Currents. My second Mandelbrot is based on the 
# "Buddhabrot" visualization of a Mandelbrot set, wherein instead of basing color
# on escape iteration #, color is based on the # of escapes that pass through a
# pixel. This creates a cool "spiritual" visualization of the Mandelbrot. 
# (https://en.wikipedia.org/wiki/Buddhabrot) I was not able to accurately replicate
# the formula fully, and I accidentally created the anti-buddhabrot. Still pretty. I
# may actually do a little bit more work on the side to see if I can get the buddhabrot.
# As of now, it looks like an alien cell in outer-space. Finally, the last visualization 
# is a Julia Set that I thought looked cool.
# (admittedly, I spent the most time tinkering with Buddhabrots)
# Estimated time for 1024x1024: 10-11min
#
# Sources:
# Mandelbrot Preview: https://www.atopon.org/mandel/#
# Buddhabrot: http://superliminal.com/fractals/bbrot/bbrot.htm and https://en.wikipedia.org/wiki/Buddhabrot
# colorsys: https://docs.python.org/2/library/colorsys.html
# various image related libraries/functions: https://pillow.readthedocs.io/en/3.1.x/reference/image.html
# 
# On My Honor, I have neither given nor received unauthorized aid.

from PIL import Image
import colorsys

# Image specs (Dimensions, Iterations, Coordinate Range)
imgx,imgy=1024,1024
tmax=256
bmax=1000 # for buddhabrot
xa,xb=-0.17866045556517698,-0.14019830536805222
ya,yb=-1.0544177227277811,-1.0159555725306564
xa2,xb2=-2.0,0.5
ya2,yb2=-1.25,1.25
xa3,xb3=-0.1475,-0.1425
ya3,yb3=0.255,0.26

# 2D lists for tracking the number of times each pixel is "passed" for escapes in buddhabrot
countsR=[[0]*imgy for x in range(imgx)]
countsG=[[0]*imgy for x in range(imgx)]
countsB=[[0]*imgy for x in range(imgx)]

# Creates "base" images
tame = Image.new("RGB",(imgx,imgy))
buddha = Image.new("RGB",(imgx,imgy))
julia = Image.new("RGB",(imgx,imgy))

# for loops to cycle through each pixel
for x in range(imgx): 
	# assigning C coordinates as discussed in class
	cx=(x*(xb-xa)/(imgx-1)+xa)
	cx2=(x*(xb2-xa2)/(imgx-1)+xa2)
	for y in range(imgy): 
		cy=(y*(yb-ya)/(imgy-1)+ya)
		cy2=(y*(yb2-ya2)/(imgy-1)+ya2)
# MANDELBROT 1: LAME IMPALA (based on https://wallpapercave.com/w/wp1901421)
		# Z always starts at 0
		zi,zx=0,0
		for t in range(tmax):
			# calculates absolute value of Z as specified in PDF
			absz=float(((zx**2)+(zi**2))**0.5)
			# checking if Z has escaped, and breaking if true
			if absz>=2.0: 
				break
			# calculates Zn+1 (which is assigned to Z)
			zx,zi=float((zx*zx-zi*zi)+cx),float((zi*zx+zx*zi)+cy)
		# if Z doesn't escape, pixel=gradient from orange to dark pink -- basically adds a fraction of a value based on x/y position
		if t==tmax-1:
			R,G,B=int(255-(80*x/imgx)),int(179-(179*x/imgx)),int(15+(75*x/imgx))
		# if Z does escape, when the escape iteration is even, then space is black, else space is a gradient from light pink to light purple
		else:
			R,G,B=int(190+(34*y/imgy))*(t%2),int(149+(50*y/imgy))*(t%2),int(192+(21*y/imgy))*(t%2)
			# as escape iteration gets closer to the limit, space cycles through rainbow starting at pink
			if t%2==1 and t>tmax/10:
				R,G,B=colorsys.hsv_to_rgb(0.9-(t-tmax/10)/(tmax/4),1,1)
				R,G,B=int(R*255),int(G*255),int(B*255)
		tame.putpixel((x,imgy-1-y),(R,G,B))
# MANDELBROT 2: BUDDHABROT
		zx,zi=0,0
		# Tracks the coordinates (trail) of each step of the escape
		sequence=[]
		for t in range(bmax):
			sequence.append([zx,zi])
			absz=float(((zx**2)+(zi**2))**0.5)
			# If coordinate escapes, function adds 1 to each coordinate that was "used" in each step of the escape
			if absz>=2.0: 
				for coord in range(len(sequence)-1):
					# converting x-y axis coordinates into PIL python coordinates
					xf=int((sequence[coord][0]-xa2)*(imgx-1)/(xb2-xa2))
					yf=int((sequence[coord][1]-ya2)*(imgy-1)/(yb2-ya2))
					if 0<=yf<=imgy-1 and 0<=xf<=imgx-1:
						# this alters the red channel only
						countsR[yf][xf] += 1
				break
			# same function with a lower escape/max iteration for the G channel
			if t == tmax//10:
				for coord in range(len(sequence)-1):
					xf=int((sequence[coord][0]-xa2)*(imgx-1)/(xb2-xa2))
					yf=int((sequence[coord][1]-ya2)*(imgy-1)/(yb2-ya2))
					if 0<=yf<=imgy-1 and 0<=xf<=imgx-1:
						countsG[yf][xf] += 1
			# same function with a lower escape/max iteration for the B channel
			if t == tmax//100:
				for coord in range(len(sequence)-1):
					xf=int((sequence[coord][0]-xa2)*(imgx-1)/(xb2-xa2))
					yf=int((sequence[coord][1]-ya2)*(imgy-1)/(yb2-ya2))
					if 0<=yf<=imgy-1 and 0<=xf<=imgx-1:
						countsB[yf][xf] += 1
			zx,zi=float((zx*zx-zi*zi)+cx2),float((zi*zx+zx*zi)+cy2)

# sets initial minimal and maximum values
minv,maxv=countsR[0][0],countsR[0][0]

# goes through the 2D list looking for lower minimums or higher maxes (these maximum and minimums are used as the relative RGB range)
for x in range(imgx):
	for y in range(imgy):
		if countsR[y][x]<minv:
			minv = countsR[y][x]
		if countsR[y][x]>maxv:
			if countsR[y][x]<=bmax*10:
				maxv = countsR[y][x]

# BUDDHABROT pixel placement, calculates relative "color strength" based on frequency of being in escape path
for x in range(imgx):
	for y in range(imgy):
		R=int(((countsR[y][x]-minv)/(maxv-minv))*255)*2
		G=int(((countsG[y][x]-minv)/(maxv-minv))*255)//2 # arbitrary constants for cosmetic changes
		B=int(((countsB[y][x]-minv)/(maxv-minv))*255)*bmax//100
		buddha.putpixel((x,imgy-1-y),(R,G,B))

# JULIA set starting, constant C
cx,cy=-.79,.15
for x in range(imgx): 
	for y in range(imgy):
		R,G,B=0,0,0
		# Z starts at X,Y instead of 0,0
		zi, zx = (y*(yb2-ya2)/(imgy-1)+ya2) , (x*(xb2-xa2)/(imgx-1)+xa2) 
		for t in range(tmax):
			# same equations as Mandelbrot
			absz=float(((zx**2)+(zi**2))**0.5) 
			if absz>=2.0: 
				break
			zx,zi=float((zx*zx-zi*zi)+cx),float((zi*zx+zx*zi)+cy)
		# cycles through HSV
		if t!=tmax-1:
			R,G,B = int(colorsys.hsv_to_rgb((0.594444-(t/tmax))%11,1)[0]*255), int(colorsys.hsv_to_rgb((0.594444-(t/tmax))%1,1,1)[1]*255), int(colorsys.hsv_to_rgb((0.594444-(t/tmax))%1,1,1)[2]*255)
		julia.putpixel((x,imgy-1-y),(R,G,B))

# saves images
tame.save("tamelbrotimpactal.png") 
buddha.rotate(270).save("buddha.png") # rotate 270 degrees because it looks cooler :)
julia.save("julia.png")