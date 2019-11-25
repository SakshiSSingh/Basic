n = int(input())
d = [int(x) for x in input().split()]
e, o = [], []
for i in range(len(d)):
    if d[i] % 2==0:
        e.append(i+1)
    else:
        o.append(i+1)

print(e[0] if len(e)==1 else o[0])

