 s = str(input())
l=[]
l.append(s[0])
c=0
for j in range(1, len(s)):
    if s[j] not in l[c]:
        (l[c])+=((s[j]))
    else:
        
        c+=1
        indexx = l[c-1].index(s[j])
        l.insert(c, l[c-1][indexx+1:])
        l[c]+=s[j]
print(l)
print(len(max(l)))
