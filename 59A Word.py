s = str(input())
u, l = 0, 0
for i in s:
    if i.isupper():
        u+=1
    else:
        l+=1

print(s.upper() if l<u else s.lower())
