
def bubble(arr, i, n):
    for j in range(0, n-1):
        if arr[j+1] < arr[j]:
            arr[j+1], arr[j] = arr[j], arr[j+1]
    return (arr)

def bubbleSort(arr, n):
    for i in range(n-1):
        arr = bubble(arr, i, n)
        if arr == sorted(arr):break
    print(*arr)

arr = [ int(x) for x in input().split()]
bubbleSort(arr, len(arr))
