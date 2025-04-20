import queue
# Smallest job first
q = queue.PriorityQueue()
q.put(10)
q.put(50)
q.put(100)
q.put(101)
q.put(105)
print(q.get())
print(q.get())