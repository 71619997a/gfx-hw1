from random import randint

with open("cout.ppm", "w") as f:
    f.write("P3 512 512 255")
    for y in range(512):
        for x in range(512):
            r = int((x ** (1.5 - y / 1024.))) % 256
            g = int((x ** (1 + y / 1024.))) % 256
            b = 128 - x / 4
            f.write(' '+str(r)+' '+str(g)+' '+str(b))
    f.write('\n')
