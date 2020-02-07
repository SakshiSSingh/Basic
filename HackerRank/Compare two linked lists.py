def compare_lists(llist1, llist2):
    while llist1 and llist2 and llist1.data==llist2.data:
        llist1 = llist1.next
        llist2 = llist2.next
    return llist1==llist2
    
Link: https://www.hackerrank.com/challenges/compare-two-linked-lists/problem
