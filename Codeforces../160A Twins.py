n = int(input())
a = [int(x) for x in input().split()]
a = sorted(a, reverse=True)
s, c = 0, 0
for i in range(len(a)):
    s+=a[i]
    c+=1
    if s>sum(a[i+1:]):
        print(c)
        break
