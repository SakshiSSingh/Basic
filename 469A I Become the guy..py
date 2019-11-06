n = int(input())
p = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]
print("I become the guy." if (n == len(set(p[1:] + q[1:]))) else "Oh, my keyboard!")
