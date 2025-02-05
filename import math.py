import math

a=int(input("give number a: "))

b=int(input("give number b: "))

c=int(input("give number c: "))

if a == 0:
    print("prwtoba8mia :")
else:
    d= b*b-4*a*c
    if d < 0:
        print("impsible")
    elif d == 0:
        r= -b/(2*a)
        print("only one root and its ",r)
    elif d > 0:
        r1= (-b+ math.sqrt(d))/(2*a)
        r2= (-b- math.sqrt(d))/(2*a)
        print("it has two roots r1=", r1, " and r2=", r2)
