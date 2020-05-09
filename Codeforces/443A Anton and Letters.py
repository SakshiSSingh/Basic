import re
s = set()
for i in re.sub("{|}", "", str(input().split(","))):
    if i.isalpha():
        s.add(i)
print(len(s)) 
