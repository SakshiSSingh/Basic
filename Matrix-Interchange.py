def swaprow(mat):

    temp = 0
    
    for i in range(r):
        temp = mat[i][0]
        mat[i][0] = mat[i][c-1]
        mat[i][c-1] = temp

mat = [[1,2,3,4],
       [4,3,2,1],
       [6,7,8,9]]
r=3
c=4

for i in mat:
    print(i)
    
swaprow(mat)
print("*****After Swapping*****")
for i in mat:
    print(i)
