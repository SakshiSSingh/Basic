wt = [10, 40, 20, 30] 
val = [60, 40, 100, 120] 
capacity = 50
d={}
wsum=0
vsum=0
for i in wt:
    for j in val:
        d[int(j/i)]=[j,i]
        val.remove(j)
        break

#{6: [60, 10], 1: [40, 40], 5: [100, 20], 4: [120, 30]}

dsort = sorted(d.keys(), reverse=True)

for i in dsort:
    if wsum!=capacity:
        
        if capacity-wsum >= d[i][1]:
            wsum+=d[i][1]
            vsum+=d[i][0]
        else:
            vsum+=int(d[i][0]/d[i][1])*(capacity-wsum)
            wsum+=capacity-wsum
        
print(vsum)


"""
Practice GFG Knapsack
"""


t = int(input())
dictt={}
v1 = []
for i in range(t):
    totalValue = 0
    dictt={}
    dsort=[]
    n, w = map(int, input().split())
    d = [int(x) for x in input().split()]

    for j in range(0, len(d),2):
        dictt['%.2f'%(d[j]/d[j+1])] = [d[j], d[j+1]]
#{6: [60, 10], 5: [100, 20], 4: [120, 30]}
    print(dictt)
    dsort = sorted(dictt.keys(), reverse = True)
    for k in dsort:
        if w-dictt[k][1] >=0:
            w -= dictt[k][1]
            totalValue += dictt[k][0]
        else:
            totalValue += float(k) * dictt[k][1]
            break
##v1.append('%.2f'%vsum)
##print(*v1, sep="\n")

print(totalValue)
