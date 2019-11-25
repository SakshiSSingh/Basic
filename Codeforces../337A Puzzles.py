n, m = map(int, input().split())
d = [int(x) for x in input().split()]
i, l = 0, []
d=sorted(d)
while i + n <= len(d):
	l.append(d[i+n-1] - d[i])
	i+=1
print(min(l))
