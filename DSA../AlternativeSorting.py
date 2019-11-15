arr=[5,2,1,7,3,6,4]
arr.sort()
arr1=[]

i=0
j=len(arr)-1

while i<j:
    arr1.append(arr[j])
    j-=1
    arr1.append(arr[i])
    i+=1
    if i==j:
        arr1.append(arr[j])


print(arr1)
