
x, y, z = 0, 0, 0
for i in range(int(input())):
    a = [int(x) for x in input().split()]
    x+=a[0]
    y+=a[1]
    z+=a[2]
print("YES" if (x==0 and y==0 and z==0) else "NO" )
