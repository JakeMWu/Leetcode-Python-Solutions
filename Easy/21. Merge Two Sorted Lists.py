class ListNode(object):
    
    def __init__ (self, val=0, next=None):
        self.val = val
        self.next = next
        
def mergeTwoLists(list1, list2):
    """
    Takes two sorted linked lists and returns a merged sorted link list in 
    strictly non-decreasing order
    
    Arguments:
    list1 (ListNode):
    list2 (ListNode):
        
    
    Returns: 
    dummy_head.next.next (ListNode): Head of the merged linked list
    """
    
    curr_node_1 = list1
    curr_node_2 = list2
    
    dummy_head = ListNode()
    curr_merged = dummy_head
    
    #### Add to merged until a list runs out
    while curr_node_1 is not None and curr_node_2 is not None:
        if curr_node_1.val <= curr_node_2.val:
            curr_merged.next = curr_node_1
            curr_merged = curr_merged.next
            curr_node_1 = curr_node_1.next
        elif curr_node_1.val > curr_node_2.val:
            curr_merged.next = curr_node_2
            curr_merged = curr_merged.next
            curr_node_2 = curr_node_2.next
    
    #### Add the rest of whichever list isn't empty
    if curr_node_1 is None:
        while curr_node_2 is not None:
            curr_merged.next = curr_node_2
            curr_merged = curr_merged.next
            curr_node_2 = curr_node_2.next

    elif curr_node_2 is None:
        while curr_node_1 is not None: 
            curr_merged.next = curr_node_1
            curr_merged = curr_merged.next
            curr_node_1 = curr_node_1.next

    return dummy_head.next  