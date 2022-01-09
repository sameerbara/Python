x=float(input("Enter initial Value of x : "))
y=float(input("Enter initial Value of y : "))
h=input("Enter Value of h : ")
n=h[::-1].find('.')
f=x**3+y

g=float(input("Enter the value of x at which you want to find the value of y : "))
h=float(h)

k1=h*f

a = (x + (0.5*h))**3+(y + (0.5*k1))
k2= h*a

b=((x+(0.5 * h))**3) + (y+(0.5*k2))
k3= h*b

c= ((x + h)**3)+ (y + k3)
k4=c*h

print(x,y)
while(x<g):
	y = y + ((1.0 / 6.0)*(k1 + (2 * k2) + (2 * k3) + k4))
	x = x+h
	print(round(x,n),round(y,3))

print("y = ",y)