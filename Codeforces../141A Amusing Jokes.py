twoMen = input() + input()
jumbledMen = input()
if len(twoMen) != len(jumbledMen):
    print("NO")
    exit()
else:
    
    for i in twoMen:
        if twoMen.count(i) != jumbledMen.count(i):
            print("NO")
            exit()

print("YES")
