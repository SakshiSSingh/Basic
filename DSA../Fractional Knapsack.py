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
