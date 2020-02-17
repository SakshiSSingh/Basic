def has_cycle(head):
    s = set()
    while head:
        if head in s:
            return True
        s.add(head)
        head = head.next
    return False    

Link:https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
