class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  


class Queue:
    def __init__(self):
        self.front = None  
        self.rear = None   

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)  # Create a new node
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node  # Link the new node with the last node
        self.rear = new_node  # Move the rear to the new node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front  # Store the front node
        self.front = temp.next  # Move front to the next node
        if self.front is None:
            self.rear = None  # If queue becomes empty, set rear to None
        return temp.data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def print_queue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Example usage:
if __name__ == '__main__':
    queue = Queue()

    # Enqueue some elements
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print("Queue:")
    queue.print_queue()

    # Dequeue elements and print
    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())

    print("Queue after dequeue:")
    queue.print_queue()

    # Peek at the front element
    print("Front of the queue:", queue.peek())