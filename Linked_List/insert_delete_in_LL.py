class Node():
    def __init__(self,value):
        self.data = value
        self.next = None
class LinkedList():
    def __init__(self):
        self.head= None

    def add_node(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

# Printing Linked List
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

# Recursive print Linked List
def print_recursively(head):
    if head is None:
        return head
    print(head.data)
    print_recursively(head.next)


#delete a particular node in linked list

def delete_node(head, value):
    if head is None:
        print("no element")
        return None
    if head.data== value:
        new_head = head.next
        head.next = None
        return new_head
    
    current = head
    while current.next is not None and current.next.data != value:
        current = current.next

    if current.next is None:
        print("value not found")
        return head
    
    temp = current.next 
    current.next = current.next.next
    temp.next = None
    return head

#sort the given linked list using merge sort

def get_middle(head):
    if not head:
        return head
    slow,fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast.next.next
    return slow

def merge_sort(head):
    if not head or not head.next:
        return head
    
    mid = get_middle(head)
    next_to_mid = mid.next
    mid.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_mid)

    sorted_list= mergeTwoLists(left,right)
    return sorted_list

def mergeTwoLists(left, right):
    dummy = LinkedList()
    tail = dummy
    while left and right:
        if left.data < right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    if left is not None:
        tail.next= left
    
    else:
        tail.next = right
    return dummy.next

l1 = LinkedList()
l1.add_node(10)
l1.add_node(20)
l1.add_node(30)
l1.add_node(40)
# print_linked_list(l1.head)

delete_node(l1.head,value = 30)
print_recursively(l1.head)

head = l1.head
merge_sort(head)