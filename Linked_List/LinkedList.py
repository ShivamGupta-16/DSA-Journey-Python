#Creating a Node 
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

#Creating a Linked List
 
class LinkedList:
    def __init__(self):
        self.head= None

    #Adding nodes to linked list
    def add_node(self,value):
        new_node = Node(value)

        #Creating head Node
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node



l1 = LinkedList()
l1.add_node(value = 10)
l1.add_node(value= 20)
l1.add_node(value=30)
l1.add_node(40)
# print(l1.head.data)   output = 10

#Display a linked list

def print_linked_list(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

print_linked_list(l1.head)

# Recursive way to print linked list

def print_recursively(head):
    if head is None:
        return
    print(head.data)
    print_recursively(head.next)

print_recursively(l1.head)



# *******************************

# Finding Length of a Linked List

def find_length(head):
    length =0
    while head is not None:
        length+=1
        head = head.next
    return length


print(find_length(l1.head))



#Recursive way to find length of the Linked List

def find_len_recursively(head):
    if head is None:
        return 0
    return 1+ find_len_recursively(head.next)


print(find_len_recursively(l1.head))