arr = []

def hourglassSum(arr):
    summ, l = 0, []
    for i in range(0, 4):
        for j in range(0, 4):
            summ = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            l.append(summ)
            print(l)
    return max(l)


for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

result = hourglassSum(arr)
print(result)

Link: https://www.hackerrank.com/challenges/2d-array/problem
