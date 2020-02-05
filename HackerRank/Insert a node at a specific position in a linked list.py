
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(str(node.data))

        node = node.next


def insertNodeAtPosition(head, data, position):
    counter = 0
    temp = head
    while temp.next:
        if counter==position-1:
            current = SinglyLinkedListNode(data)
            current.next = temp.next
            temp.next = current
        temp = temp.next
        counter += 1
    return head

llist_count = int(input())

llist = SinglyLinkedList()

for _ in range(llist_count):
    llist_item = int(input())
    llist.insert_node(llist_item)

data = int(input())
position = int(input())

llist_head = insertNodeAtPosition(llist.head, data, position)

print_singly_linked_list(llist_head, ' ')

Link: https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
