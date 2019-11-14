n = int(input())

print((int(n/2)*(int(n/2)+1)) - int(n/2)**2 if n%2==0 else (int(n/2)*(int(n/2)+1)) - (int(n/2)+1)**2)
