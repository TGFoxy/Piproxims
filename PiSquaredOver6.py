import math
n = 1
s = 0
for n in range(1, 99999999999999999999999999999999999999999999999999999999999999999):
    s  += 1/n**2
    print(s, end="\r")
x = s*6
pisquare = math.sqrt(x)
print("Pi is ", pisquare)
