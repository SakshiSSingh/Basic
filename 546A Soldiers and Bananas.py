k, n, w = map(int, input().split())
c=0
for i in range(w+1):
   c += k*i 
print(c-n if c>n else 0)
