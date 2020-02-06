def reversePrint(head):
    if head == None:
        return
    l=[]
    temp = head
    while temp:
        l.append(temp.data)
        temp = temp.next
    print(*l[::-1], sep="\n")
    
Link: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem
