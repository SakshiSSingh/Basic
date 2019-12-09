n, m = map(int, input().split())
o=0
for i in range(0, n):
    if i%2==0:
        print("#"*m)
    else:
        if o==0:
            print("."*(m-1)+"#")
            o=1
        else:
            print("#" + "."*(m-1))
            o=0
