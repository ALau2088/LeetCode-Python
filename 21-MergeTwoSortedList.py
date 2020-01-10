# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
#IOCE
I: 2 linked lists
O: merged linked list
C: none
E: one linked list empty, two linked lists are empty

#EXAMPLES
I: 1->2->4, 1->3->4
O: 1->1->2->3->4->4

I: 1->3->4, 1->2->4
O: 

Step1: Compare 1st node of each list. Whichever node is less value is head. If equal, first node of first linked list
1->1

Step2: Compare node that has not been added versus next node

Step3: Repeat Step1-2 ntil no more nodes null values
1->1 ->2->3 ->4->4



#PSEUDOCODE
F mergeTwoLists (linkedlist1(l1), linkedlist2(l2)):
    currentNode1(cn1) = l1
    currentNode2(cn2) = l2
    
  # Edge Case-one or two empty linked list
  if l1 = empty and l2 = empty:
    return empty
  else if l1 = empty:
    return l2
  else if l2 = empty:
    return l1
  
  IF l1.val <= l2.val:
    listToReturn(ltr) = l1
    currentNode1(cn1) = l1.next
  ELSE:
    listToReturn(ltr) = l2
    currentNode2(cn2) = l2.next
    
  currentNode3(cn3) = ltr.next  
  WHILE cn1 AND cn2 != null:
    IF cn1.val <= cn2.val:
        cn1 = cn1.next
        cn.next = cn1
    ELSE:
        cn3 = cn2
        cn2 = cn2.next
    cn3 = cn3.next    
  RETURN ltr

"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cn1 = l1
        cn2 = l2
        
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        if l1.val <= l2.val:
            ltr = l1
            cn1 = l1.next
        else:
            ltr = l2
            cn2 = l2.next
            
        cn3 = ltr
        while cn1 != None and cn2 != None:
            if cn1.val <= cn2.val:
                cn3.next = cn1
                cn1 = cn1.next
            else:
                cn3.next = cn2
                cn2 = cn2.next
            cn3 = cn3.next
        
        if cn1 != None:
            cn3.next = cn1
        
        if cn2 != None:
            cn3.next = cn2
        
        return ltr
    
        