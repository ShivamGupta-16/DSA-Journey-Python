class Node:
    def __init__(self, data= None):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError("Stack is already empty")
        popped_value = self.head.data
        self.head = self.head.next
        # return popped_value

        
        

    def print(self):
        while self.head is not None:
            print(self.head.data, end=" ")
            self.head = self.head.next


if __name__ =="__main__":
    
    s= stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.pop()
    s.print()