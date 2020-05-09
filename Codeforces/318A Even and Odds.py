n, k = map(int, input().split())
if n%2==0:
    print( (k-(int(n/2)))*2 if k>(n/2) else(k*2-1) )
else:
    print( (k-(int(n/2)+1))*2 if k>(n/2+1) else (k*2-1))
