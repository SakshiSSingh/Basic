n, h = map(int, input().split())
d = [int(x) for x in input().split()]
a,c = 0, 0
for i in d:
    if i>h:
        a+=1
        if i%h!=0:
            c+=int(i/h)+1
        else:
            c+=int(i/h)

print(c+len(d)-a)
