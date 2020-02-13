import sys
sys.setrecursionlimit(10**6) //in case maximum recursion depth exceeds

def mergeLists(head1, head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    if head1.data < head2.data:
        head1.next = mergeLists(head1.next, head2)
        return head1
    else:
        head2.next = mergeLists(head1, head2.next)
        return head2
        
Link: https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem 
