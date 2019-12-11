c=0
for i in range(int(input())):
    s = str(input())
    print(s)
    if s=='Tetrahedron':c+=4
 
    elif s=='Cube':c+=6
  
    elif s=='Octahedron':c+=8
   
    elif s=='Dodecahedron':c+=12

    else:c+=20
    
print(c)
