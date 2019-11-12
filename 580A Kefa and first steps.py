n = int(input())
a = [int(x) for x in input().split()]
d, c = [], 1
for i in range(len(a)-1):
    if a[i]<=a[i+1]:
        c+=1
    else:
        d.append(c)
        c=1
d.append(c)   
print(max(d) if (d) else 1)
