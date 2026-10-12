import math

x1=float(input("What is the value of x1?:"))
y1=float(input("What is the value of y1?:"))
x2=float(input("What is the value of x2?:"))
y2=float(input("What is the value of y2?:"))

d=math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))

print(d)