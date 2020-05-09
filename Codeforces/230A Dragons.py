s, n = map(int, input().split())
l=[]
for i in range(0, n):
    l.extend([list(map(int, input().split()))])

for x,y in sorted(l):
    if x<s:
        s+=y
    else:
        print("NO")
        exit()

print("YES")
