def insertNodeAtHead(llist, data):
    temp = SinglyLinkedListNode(data)
    temp.next = llist
    llist = temp
    return llist

   
Link: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
