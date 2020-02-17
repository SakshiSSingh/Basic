def getNode(head, positionFromTail):
    index = 0
    current = head
    tail = head
    while current.next != None:
        if index >= positionFromTail:
            tail = tail.next
        current = current.next
        index += 1
    return tail.data
    
 Link: https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem
