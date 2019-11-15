n = int(input())
c=0
for i in range(n):
    x = [int(x) for x in input().split()] 
    if x.count(1)>=2:
        c+=1
print(c)
