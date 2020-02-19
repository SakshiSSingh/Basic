def isBalanced(s):
    stack = []
    Dict_of_Brackets = {'}':'{', ')':'(', ']':'['}
    for i in s:
        if i in Dict_of_Brackets and stack and Dict_of_Brackets[i]==stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if stack:
        return 'NO'
    else:
        return 'YES'
        
Link: https://www.hackerrank.com/challenges/balanced-brackets/problem
