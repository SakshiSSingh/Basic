n = int(input())
a = [int(x) for x in str(n)]
l, f=0, 0
for i in a:
    if i==4 or i==7:
        l+=1
k = [int(i) for i in str(l)]
for j in k:
    if j!=4:
        if j!=7:
            f=1
print("YES" if f==0 else "NO")
