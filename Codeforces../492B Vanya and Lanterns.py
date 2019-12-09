n, l = map(int, input().split())
d = sorted([int(x) for x in input().split()])
m = 0
for i in range(0, n-1):
    m = d[i+1] - d[i] if d[i+1] - d[i] > m else m
m = m/2

if d[0] > m:
    print("d[o]")
    m = d[0]
if l - d[n-1] > m:
    print("d[n-1]")
    m = l - d[n-1]
   
print("{0:.10f}".format(m))
