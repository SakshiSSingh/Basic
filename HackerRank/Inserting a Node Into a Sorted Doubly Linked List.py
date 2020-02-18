def sortedInsert(head, data):
    Node = DoublyLinkedListNode(data)
    temp = head
    if Node.data <= head.data:
        Node.next = head
        head = Node
        return head
    
    while temp:
    
        if temp.next == None:
            temp.next = Node
            return head
     
        if Node.data >= temp.data and Node.data < temp.next.data:
            next = temp.next
            temp.next = Node
            Node.next = next
            return head

        temp = temp.next
        
Link: https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem
