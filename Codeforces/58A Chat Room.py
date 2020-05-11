s = str(input())
word="hello"
index=0

for i in range(len(s)):
    if s[i]==word[index]:
        index+=1
    if index==5:
        break
print("Yes" if index==5 else "NO")
