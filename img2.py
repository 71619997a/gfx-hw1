from random import randint, random
import math
import os


def imgOut(pixArray, name='wow.png'):
	ylen = len(pixArray)
	xlen = len(pixArray[0])
	with open('temp.ppm', 'w') as f:
		f.write('P3 %d %d 255\n' % (xlen, ylen))
		for row in pixArray:
			for rgb in row:
				f.write('%d %d %d ' % rgb)
			f.write('\n')  # unnecessary but looks good
	os.system('convert temp.ppm ' + name)
	os.system('rm temp.ppm')

xr512 = xrange(512)
pixels = []
for x in xr512:
	for y in xr512:
		if (x-256) ** 2 + (y-200) ** 2 <= 1600 \
			or (x - 200) ** 2 + (y - 312) ** 2 <= 1600 \
			or (x - 312) ** 2 + (y - 312) ** 2 <= 1600:
			shiftRad = randint(0, 160)
			xpart = random() * 2 - 1
			ypart = random() * 2 - 1
			xnorm = xpart / math.sqrt(xpart ** 2 + ypart ** 2)
			ynorm = ypart / math.sqrt(xpart ** 2 + ypart ** 2)
			r = x - 128
			g = y - 128
			b = math.sqrt((x - 256) ** 2 + (y - 256) ** 2) % 256
			pixels.append((int(x + shiftRad * xnorm), int(y + shiftRad * ynorm), (r, g, b)))

pArray = [[(0,0,0) for i in xr512] for j in xr512]
for x, y, col in pixels:
	pArray[y][x] = col

imgOut(pArray)
