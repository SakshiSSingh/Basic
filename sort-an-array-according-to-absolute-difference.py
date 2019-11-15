from collections import defaultdict


def sortArray_accto_AbsDiff(a, val):
    d = defaultdict(list)
    
    for i in a:
        d[(abs(val-i))].append(i)


    for i in sorted(d.keys()):
        for j in range(len(d[i])):
            l.append(d[i][j])

        

l=[]
val = 6
a = [7, 12, 2, 4, 8, 0]
sortArray_accto_AbsDiff(a, val)

print(' '.join(map(str, l)))  
