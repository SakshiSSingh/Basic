n = int(input())
c=0
a = [7, 4, 47, 74, 477, 447]
for i in a:
    if (n%i==0):
        c=1
        break

print("YES" if c==1 else "NO")
