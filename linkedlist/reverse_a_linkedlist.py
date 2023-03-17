def reverse(head):
    #initialize the three pointers
    prev = None
    current = head
    nxt = head.next
    while current != None:
        nxt = current.next
        # change the direction of the nodes
        current.next = prev
        # shifting the nodes
        prev = current
        current = nxt
    head = prev
    return head



