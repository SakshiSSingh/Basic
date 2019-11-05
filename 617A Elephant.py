x = int(input())
c=0
if x-5<=0:
    c=1
elif x%5==0:
    c = int(x/5)
else:
    c = int(x/5)+1
    
print(c)
