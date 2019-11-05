n, k = map(int, input().split(" "))
a = [int(x) for x in input().split()]
c=0
for i in a:
    print(i, a[k-1])
    if(i>0 and i>=a[k-1]):
        c+=1

print(c)
