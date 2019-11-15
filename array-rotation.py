def arrRotate(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
def LeftarrRotate(arr, n , d):
    for i in range(d):
        arrRotate(arr, n)





arr=[1,2,3,4,5,6,7]
n=7
d=2
LeftarrRotate(arr, n, d)
print(arr)
