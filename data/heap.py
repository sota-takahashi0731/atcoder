import heapq

def heap_sort(array):
    heap = []
    for v in array:
        heapq.heappush(heap, v)
        return [heapq.heappop(heap) for i in range(len(heap))]
