#n = int(input())
c=0
for i in range(int(input())):
#    a = str(input())
    if "++" in str(input()):
        c+=1
    elif "--" in str(input()):
        c-=1
print(c)
