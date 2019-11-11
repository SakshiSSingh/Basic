s = str(input())
l = []
if len(s)==1 and s.islower():
    print(s.upper())
elif s.isupper() or s[1:].isupper():
    l = list(s)
    for i in range(len(l)):
        if l[i].isupper():            
            l[i] = l[i].lower()
        else:
            l[i] = l[i].upper()          
    print("".join(i for i in l))
else:
    print(s)
