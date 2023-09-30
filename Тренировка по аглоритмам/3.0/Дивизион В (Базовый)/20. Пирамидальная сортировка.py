def main():
    def append_heap(heap : list, value: int):
        heap.append(value)
        position = len(heap) - 1
        while position > 0:
            parent = (position - 1) // 2
            if heap[parent] > heap[position]:
                heap[parent], heap[position] = heap[position], heap[parent]
                position = parent
            else:
                break
    
    def extract_heap(heap : list):
        if len(heap) == 1:
            return heap.pop()
        
        value = heap[0]
        heap[0] = heap.pop()
        position = 0
        while True:
            left = 2 * position + 1
            right = 2 * position + 2
            bigger = position
            if left < len(heap) and heap[bigger] > heap[left]:
                bigger = left
            if right < len(heap) and heap[bigger] > heap[right]:
                bigger = right
            if bigger == position:
                break
            heap[position], heap[bigger] = heap[bigger], heap[position]
            position = bigger
        return value
    
    N = int(input())
    array = list(map(int, input().split()))
    heap = []
    for i in range(N):
        append_heap(heap, array[i])
    
    sort_array = [0]*N
    for i in range(N):
        sort_array[i] = extract_heap(heap)
        
    print(" ".join(map(str, sort_array)))

    
    

if __name__ == '__main__':
	main()