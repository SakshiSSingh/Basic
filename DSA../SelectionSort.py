
def select(arr):
    for i in range(len(arr)):
        minElem=arr[i]
        for j in range(i+1, len(arr)):
            if arr[j]<minElem:
                minElem, arr[j] = arr[j], minElem 
        arr[i] = minElem
    return arr
    
    
arr = [int(x) for x in input().split()]
print(*select(arr))
