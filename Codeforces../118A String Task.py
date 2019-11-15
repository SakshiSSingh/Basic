s = str(input())
v = "aeiouyAEIOUY"
c = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
s1=""
for i in s:
   if i in c:
        s1 = s1+"."+i
print(s1.lower())
