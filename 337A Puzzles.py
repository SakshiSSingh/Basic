n, m = map(int, input().split())
d = [int(x) for x in input().split()]
d=sorted(d)
print(d[n-1]-d[0])
