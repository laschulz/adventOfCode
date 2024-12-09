import re
import numpy as np
f=open("day3.txt","r")
s = f.read()
mult = re.findall(r"mul\((\d+),(\d+)\)", s)
sum = np.array([int(x)*int(y) for (x,y) in mult]).sum()
print(sum)
f.close()