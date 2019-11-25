n = int(input())
d = [int(x) for x in input().split()]

mi = max([i for i, x in enumerate(d) if x == min(d)])
ma = min([i for i, x in enumerate(d) if x == max(d)])
ans = ma + (len(d) - mi -1)
if ma<mi:
    print(ans)
else:
    print(ans-1)
