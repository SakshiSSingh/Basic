class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    temp = SinglyLinkedListNode(data)
    temp.next = llist
    llist = temp
    return llist
    
llist_count = int(input())

llist = SinglyLinkedList()

for _ in range(llist_count):
    llist_item = int(input())
    llist_head = insertNodeAtHead(llist.head, llist_item)
    llist.head = llist_head
    
print_singly_linked_list(llist.head, '\n')
   
Link: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
