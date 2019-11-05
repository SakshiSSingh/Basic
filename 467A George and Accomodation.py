c=0
for i in range(int(input())):
    x = [int(x) for x in input().split()]
    if x[0]<=x[1]-2:
        c+=1
print(c)
