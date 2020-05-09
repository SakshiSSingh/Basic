d=[]
for i in range(int(input())):
    d.append(input())
i=0
c=1
for j in range(1, len(d)):
    if d[j]!=d[i]:
        c+=1
        i=j
        j+=1
print(c)
            
