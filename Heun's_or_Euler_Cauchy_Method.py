x=float(input("Enter initial Value of x : "))
y=float(input("Enter initial Value of y : "))
h=input("Enter initial Value of h : ")
n=h[::-1].find('.')
f=x+y

g=float(input("Enter the value of x at which you want to find the value of y : "))
h=float(h)

k1=h*f

a = (x + (0.5*h))+(y + (0.5*k1))
k2= h*a

print(x,y)
while(x<g):
	y = y + k2
	x = x+h
	print(round(x,n),round(y,3))

print("y = ",y)