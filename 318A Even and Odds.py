n, k = map(int, input().split())

if k>int(n/2):
    print((int(n/2)-k)*2)
else:
    print(k*2-1)
