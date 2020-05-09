n = int(input())

f=0
n+=1
while(f!=1):
    a = [int(x) for x in str(n)]
    if len(set(a))==4:
        f=1
        break
    n+=1
print(int("".join(map(str, a))))
