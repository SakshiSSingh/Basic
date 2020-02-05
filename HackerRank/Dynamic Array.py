n, q = map(int, input().split())
lastAns = 0
seqList = [[] for _ in range(n)]
for i in range(q):
    que, x, y = map(int, input().split())
    seq = (x ^ lastAns)%n
    if que==1:
        seqList[seq].append(y)
    else:
        lastAns = seqList[seq][y % len(seqList[seq])]
        print(lastAns)
     
Link: https://www.hackerrank.com/challenges/dynamic-array/problem
