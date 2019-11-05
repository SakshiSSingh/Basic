s1 = str(input()).lower()
s2 = str(input()).lower()
f = 0
for i in range(len(s1)):
    
    if s1[i] == s2[i]:
        f=0
    elif s1[i] < s2[i]:
        f=-1
        break

    elif s1[i] > s2[i]:
        f=1
        break
print(f)
