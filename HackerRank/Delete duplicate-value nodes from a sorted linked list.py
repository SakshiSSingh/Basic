def removeDuplicates(head):
    temp = head
    while temp:
        if temp.next == None:
            return head
        if temp.data != temp.next.data:
            temp = temp.next
        else:
            temp.next = temp.next.next
    return head
    
Link: https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem
