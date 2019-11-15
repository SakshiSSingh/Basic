n = int(input())
s=""
f=0
for i in range(1, n+1):
    if i%2==0:
        s+= "I Love "
        f+=1

    else:
        s+= "I Hate "
        f+=1
    if(f<n):
        s+= "that "
print(s + "it")
            
