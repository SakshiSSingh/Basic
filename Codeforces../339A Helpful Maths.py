l=[",".join(x) for x in input().split()[0]]
i, j, = 0, 0
l1= sorted(list(filter(lambda a: a != '+', l)))

while(i<=len(l)):
    l[i] = l1[j]
    i+=2
    j+=1
print("".join([i for i in l]))
