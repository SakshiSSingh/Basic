n = int(input())
s, i = "", 1
while(i<=n):
    if i%2==0:
        s+= "I love that "
    else:
        s+= "I hate that "
    i+=1
print(s[:(len(s))-5]+"it")

    
    
