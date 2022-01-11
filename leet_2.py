# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s,i = 0, 0
        while l1 != None or l2 != None:
            if l1 == None:
                s+=l2.val*(10**i)
                l2=l2.next
            elif l2 == None:
                s+=l1.val*(10**i)
                l1=l1.next
            else:
                s+=(l1.val+l2.val)*(10**i)
                l1,l2=l1.next,l2.next
            i+=1
        myList = ListNode()
        my = myList
        r = list(map(int,reversed(str(s))))
        count = 0
        for each in r:
            count+=1
            myList.val = each
            if count != len(r):
                myList.next = ListNode()
                myList = myList.next

        return my
            