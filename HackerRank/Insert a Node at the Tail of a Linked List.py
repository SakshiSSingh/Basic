def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if head == None:
        head = node
    else:
        temp = head 
        while temp.next:
            temp = temp.next
        temp.next = node
    return head

Link: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem?h_r=next-challenge&h_v=zen
