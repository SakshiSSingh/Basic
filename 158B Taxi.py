n = int(input())
a = [int(x) for x in input().split()]
print(int(sum(a)/4 )if int(sum(a)%4)==0 else int(sum(a)/4)+1)
