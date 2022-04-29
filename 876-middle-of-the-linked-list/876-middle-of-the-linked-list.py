# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0,next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]):
        cur=head
        cur1=head#assigning head to cur
        len_list=0
        while cur:# if current node is not empty
            len_list+=1
            cur=cur.next # cur is set to pointer bt cur.next
        print(len_list)
        count=0
        while cur1:
            if (len_list//2) == count: 
                return cur1
            else:
                count+=1
                cur1=cur1.next
            
        