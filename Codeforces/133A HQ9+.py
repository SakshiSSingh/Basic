s = str(input())
if 'H' in s or 'Q' in s or '9' in s:
    print("YES")
elif '+' in s and ('H' in s or 'Q' in s or '9' in s):
    print("YES")

else:
    print("NO")
