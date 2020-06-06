s = 0
t = 0
Range = int(input("Input Range "))
f = open("Evaluation.txt","a+")
for n in range(1, Range, 4):
    s += 1/n
for n in range(3, Range, 4):
    t += 1/n
total = s - t    
pi = total*4
f.write("Pi is " + str(pi) + "\n")
f.close()

    
