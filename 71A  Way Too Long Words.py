n = int(input())
#l=[]
for i in range(n):
    i = str(input())
    if len(i)>10:
  #      l.append(i[0] + str(len(i)-2) + i[len(i)-1])
          i=i[0] + str(len(i)-2) + i[len(i)-1]
#    else:
 #       l.append(i)
print(i)
#print("\n".join(l))
