a, b = map(int, input().split())
f, c = 0, 0
while f!=1:
    c+=1
    if a*3 > b*2:
        print("if")
        f=1
        break
    else:
        a, b = a*3, b*2
        
print(c)
