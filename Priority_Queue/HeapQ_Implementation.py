import heapq
heap =[]
heapq.heappush(heap, 10)
heapq.heappush(heap, 100)
heapq.heappush(heap, 5)
heapq.heappop(heap)
print(heap)
heapq.heappop(heap)
print(heap)


# Giving priority to the elements.
list =[]
list.append((3, "Greater Noida"))
list.append((1, "Shivam"))
list.append((2,"Varanasi"))
list.sort()
print(list)
print(list.pop(0))