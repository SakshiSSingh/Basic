d=[]

for i in range(int(input())):
    d.append(input())
print(d)
i=0
c=1
for j in range(1, len(d)):
    print(i, j, d[i], d[j])
    if d[j]!=d[i]:
        print("if")
        c+=1
        i=j
        j+=1
        print(c,i,j,j-1)
print(c)
            
