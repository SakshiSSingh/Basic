n, t = map(int, input().split())
s = str(input())
l = list(s)

for j in range(t):
    i=0
    while i<len(l)-1:
        if l[i]=='B' and l[i+1]=='G':
            l[i], l[i+1] = l[i+1], l[i]
            i+=2

        else:
            i+=1
print("".join(i for i in l))
