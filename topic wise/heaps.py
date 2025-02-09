#heaps
import heapq

minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

print(heapq[0])

while len(minHeap):
    print(heapq.heappop(minHeap))


# python doesnot have the max heap workarround is 
# to multiply the value by -1 and then use the min heap

maxHeap = []
heapq.heappush(maxHeap, -1 * 3)
heapq.heappush(maxHeap, -1 * 2)
heapq.heappush(maxHeap, -1 * 4)

while len(maxHeap):
    print( - 1* heapq.heappop(maxHeap))


arr = [1,2,3,4,5,6]
heapq.heapify(arr)

while arr:
    print(heapq.heappop(arr))