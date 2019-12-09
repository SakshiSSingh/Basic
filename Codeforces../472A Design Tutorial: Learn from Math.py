n = int(input())
a, b = 4, n-4

def isComposite(k):

    for i in range(2, k):

        if k%i==0:
            return 1
    return 0


for i in range(1, n):
    if isComposite(a) and isComposite(b):
        print(a, b)
        exit()
    a+=1
    b-=1




