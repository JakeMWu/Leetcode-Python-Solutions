class ListNode:
    def __init__(self, val=0, next=None):
                 self.val = val
                 self.next = next
                
def addTwoNumbers(l1, l2):
    """
    Takes two linked lists each of which have nodes representing a single digit of a larger number in reverse order 
    and returns the sum of the two numbers in the same format. 
    
    Arguments:
    l1 (ListNode): Head of a linked list of a number with reversed digits
    l2 (ListNode): Head of a linked list of a number with reversed digits
    
    Returns: 
    dummy_head.next (ListNode): Head of the sum linked list 
    """
    curr_node = l1
    num1 = ''
    num2 = ''
    
    while curr_node is not None:
        num1 += str(curr_node.val)
        curr_node = curr_node.next
    
    curr_node = l2
    while curr_node is not None:
        num2 += str(curr_node.val)
        curr_node = curr_node.next 
    
    sum_num = int(num1[::-1]) + int(num2[::-1])
    sum_num = str(sum_num)[::-1]
    
    dummy_head = ListNode()
    curr_node = dummy_head
    
    for digit in sum_num:
        curr_node.next = ListNode(int(digit))
        curr_node = curr_node.next
        
    return dummy_head.next