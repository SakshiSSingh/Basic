
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next



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



llist_count = int(input())

llist = SinglyLinkedList()

for i in range(llist_count):
    llist_item = int(input())
    llist_head = insertNodeAtTail(llist.head, llist_item)
    llist.head = llist_head

print_singly_linked_list(llist.head, '\n')

Link: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem?h_r=next-challenge&h_v=zen
