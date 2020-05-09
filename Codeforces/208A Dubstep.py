s = str(input())
s=s.replace("WUB", " ")
s2=""
for i in range(len(s)):
    if s[i]==" " and s[i-1]!=" ":
        s2+=s[i]
    elif s[i] != " ":
        s2+=s[i]

print(s2.strip())

