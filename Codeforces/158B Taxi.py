n=int(input())
a = [int(x) for x in input().split()]
d, d3=[], 0
d.append(a[0])
j=1
sorted(a, reverse=True)
for i in range(1, len(a)):
    if a[i]==1:
        if 3 in d:
            d[d.index(3)]+=1
            
    if 4-d[j-1]>=a[i]:
        print("if",d[j], i, a[i])
        d[j-1]+=a[i]
    else:
        j+=1
        print("else", d[j], i, a[i])
        d.append(a[i])
    if a[i]==1:
        if 3 in d:
            d3 = d.count(3)
        

print(j-1)












##n=int(input())
##a = [int(x) for x in input().split()]
##a1=a.count(1)
##a2=a.count(2)
##a3=a.count(3)
##a4=a.count(4)
## 
##d1, d2 = 0, 0
##
##d2 = (int(a2/2)+1 if a2%2!=0 else int(a2/2)) if a2!=1 else 1
###d1 = (int(a1/4) if a1%4==0 else int(a1/4)+1) if (a1>a3) else 0
##        
##if a1>a3:
##    if a1-a3>d2:
##        if a1-a3>=2:
##            if (a1-a3)%4==0:
##                if a1-a3<4:
##                    d1=1
##                else:
##                    d1=int((a1-a3)/4)
##            else:
##                if a1-a3<4:
##                    d1=1
##                else:
##                    d1=int((a1-a3)/4)+1
##            
##        else :
##            d1=1
##            
##
##    else:
##        d1=0
##else:
##    d1=0
##print(d2, a3+a4+d1+d2)
##    






##a = int(raw_input())
##b = raw_input()
##c = (b.split())
##c = map(int,c)
##c.sort(reverse = True)
##x = len(c)
##count = 0
##i=0
##j=len(c)-1
##while(i<=j):
##	count=count+1
##	s = 4 - c[i]
##	while (c[j]<=s and i<=j):
##		s = s-c[j]
##		j=j-1	
##	i=i+1 
##print count
##
##
##
##
##


