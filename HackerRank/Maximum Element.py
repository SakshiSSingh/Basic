stack = []

n = int(input())
for i in range(n):
    a = list(map(int, input().split()))

    if a[0] == 1:
        if len(stack) == 0:
            stack.append(a[1])
        else:
            stack.append(a[1] if a[1] > stack[-1] else stack[-1])
    elif a[0] == 2:
        stack.pop()

    if a[0] == 3:
        print(stack[-1])

Link: https://www.hackerrank.com/challenges/maximum-element/problem
