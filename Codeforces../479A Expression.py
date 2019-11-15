d=[]
for i in range(3):
    d.append(int(input()))
print(max(d[0] + d[1] + d[2], d[0] * d[1] * d[2], (d[0] + d[1]) * d[2], d[0] * (d[1] + d[2])))



