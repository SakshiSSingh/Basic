Learn more
c=[]
d=0
for i in range(int(input())):
    a = [int(x) for x in input().split()]
    d+=-a[0]+a[1]
    c.append(d)

print(max(c))
