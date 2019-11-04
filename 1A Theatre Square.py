import math
m, n = map(int,input().split(" "))
a = int(input())
 
if m%a==0 and n%a==0:
    print("1")
    print ((math.floor(m/a))*(math.floor(n/a)))
 
elif m%a==0 and n%a>0:
    print("2")
    print((math.floor(m/a))*(math.floor(n/a+1)))
 
elif m%a>0 and n%a==0:
    print("3")
    print((math.floor(m/a+1))*(math.floor(n/a)))
 
elif m%a>0 and n%a>0:
    print("4",m/a+1, n/a+1 )
 
    print((math.floor(m/a)+1)*(math.floor(n/a)+1))
