from PIL import Image, ImageEnhance
import colorsys
import random

# Image specs (Dimensions, Iterations, Coordinate Range)
imgx,imgy=1024,1024
tmax=1000
xa,xb=-2.0,0.5
ya,yb=-1.25,1.25

# for tracking the number of times each pixel is 
countsR=[[0]*imgy for x in range(imgx)]
countsG=[[0]*imgy for x in range(imgx)]
countsB=[[0]*imgy for x in range(imgx)]

image = Image.new("RGB",(imgx,imgy))

for x in range(imgx):
	cx=(x*(xb-xa)/(imgx-1)+xa)
	for y in range (imgy):
		cy=(y*(yb-ya)/(imgy-1)+ya)
		zx,zi=0,0
		sequence=[]
		for t in range(tmax):
			sequence.append([zx,zi])
			absz=float(((zx**2)+(zi**2))**0.5)
			if absz>=2.0: 
				for coord in range(len(sequence)-1):
					xf=int((sequence[coord][0]-xa)*(imgx-1)/(xb-xa))
					yf=int((sequence[coord][1]-ya)*(imgy-1)/(yb-ya))
					if 0<=yf<=imgy-1 and 0<=xf<=imgx-1:
						countsR[yf][xf] += 1
				break
			if t == tmax//10:
				for coord in range(len(sequence)-1):
					xf=int((sequence[coord][0]-xa)*(imgx-1)/(xb-xa))
					yf=int((sequence[coord][1]-ya)*(imgy-1)/(yb-ya))
					if 0<=yf<=imgy-1 and 0<=xf<=imgx-1:
						countsG[yf][xf] += 1
			if t == tmax//100:
				for coord in range(len(sequence)-1):
					xf=int((sequence[coord][0]-xa)*(imgx-1)/(xb-xa))
					yf=int((sequence[coord][1]-ya)*(imgy-1)/(yb-ya))
					if 0<=yf<=imgy-1 and 0<=xf<=imgx-1:
						countsB[yf][xf] += 1
			zx,zi=float((zx*zx-zi*zi)+cx),float((zi*zx+zx*zi)+cy)

minv,maxv=countsR[0][0],countsR[0][0]

for x in range(imgx):
	for y in range(imgy):
		if countsR[y][x]<minv:
			minv = countsR[y][x]
		if countsR[y][x]>maxv:
			if countsR[y][x]<=tmax:
				maxv = countsR[y][x]

for x in range(imgx):
	for y in range(imgy):
		R=int(((countsR[y][x]-minv)/(maxv-minv))*255)
		G=int(((countsG[y][x]-minv)/(maxv-minv))*255)//2
		B=int(((countsB[y][x]-minv)/(maxv-minv))*255)*5
		image.putpixel((x,imgy-1-y),(R,G,B))

# ImageEnhance.Contrast(image).enhance(10)

image.rotate(270).save("antibuddha.png")