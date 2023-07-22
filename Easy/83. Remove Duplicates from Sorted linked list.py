class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
        
def deleteDuplicates(self, head):
    """
    Removes duplicates from a sorted linked list which is strictly
    non-decreasing and returns the head of the linked list

    Arguments:
    head (ListNode): Head of a linked list (or None)

    Returns: 
    head (ListNode): Updated removing duplicates 

    """
    if head == None: 
        return head
    curr_node = head
    
    while curr_node.ext is not None:
        if curr_node.val == curr_node.next.val:
            curr_node.next = curr_node.next.next
        elif curr_node.val < curr_node.next.val:
            curr_node = curr_node.next
            
    return head