class Solution: 
    def isPalindrome(self, head: ListNode) -> bool:
        my_list = [] 
        while head != None:
            val = head.val 
            my_list.append(val) 
            head = head.next 
        if my_list == my_list[::-1]: return True 
        return False