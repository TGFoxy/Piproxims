import math
n = 1
s = 0
Range = int(input("Range"))
f = open("Data Revised.txt","a+")
for n in range(1, Range):
    s  += 1/n**2
x = s*6
pisquare = math.sqrt(x)
f.write("Pi is " + str(pisquare) + "\n")
f.close()
