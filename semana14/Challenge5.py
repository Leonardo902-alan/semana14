test_results = []

def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        # Add value maintaining max-heap property
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def delete_max(self):
        # Remove and return maximum element
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Store maximum value to return
        max_value = self.heap[0]
        
        # Replace root with last element
        self.heap[0] = self.heap.pop()
        
        # Restore heap property by bubbling down
        self._heapify_down(0)
        
        return max_value
    
    def build_heap(self, array):
        # Convert array to valid heap in O(n) time
        if not array:
            self.heap = []
            return
        
        # Copy array to heap
        self.heap = array.copy()
        
        # Start from last non-leaf node and heapify downward
        # Last non-leaf node is at index (n//2) - 1
        start_index = (len(self.heap) // 2) - 1
        
        for i in range(start_index, -1, -1):
            self._heapify_down(i)
    
    def _heapify_up(self, index):
        # Move element up for max-heap
        while index > 0:
            parent_idx = (index - 1) // 2
            
            # If parent is greater or equal, heap property is satisfied
            if self.heap[parent_idx] >= self.heap[index]:
                break
                
            # Swap with parent and continue up
            self.heap[parent_idx], self.heap[index] = self.heap[index], self.heap[parent_idx]
            index = parent_idx
    
    def _heapify_down(self, index):
        # Move element down for max-heap
        while True:
            largest = index
            left_idx = 2 * index + 1
            right_idx = 2 * index + 2
            
            # Check if left child exists and is larger than current largest
            if (left_idx < len(self.heap) and 
                self.heap[left_idx] > self.heap[largest]):
                largest = left_idx
            
            # Check if right child exists and is larger than current largest
            if (right_idx < len(self.heap) and 
                self.heap[right_idx] > self.heap[largest]):
                largest = right_idx
            
            # If no swap is needed, heap property is satisfied
            if largest == index:
                break
            
            # Swap with the larger child and continue down
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

def test_1_5():
    heap = MaxHeap()
    
    # 1.5.1 MaxHeap insertion
    heap.insert(3)
    heap.insert(1)
    heap.insert(5)
    record_test("1.5.1 MaxHeap insertion", heap.heap[0] == 5)
    
    # 1.5.2 MaxHeap deletion
    max_val = heap.delete_max()
    record_test("1.5.2 MaxHeap deletion", max_val == 5)
    
    # 1.5.3 Build heap from array
    heap.build_heap([3, 1, 4, 1, 5, 9, 2])
    record_test("1.5.3 Build heap from array", heap.heap[0] == max(heap.heap))
    
    # 1.5.4 Heap property verification
    valid_max_heap = all(
        heap.heap[i] >= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.5.4 Heap property verification", valid_max_heap)
    
    # 1.5.5 Empty array handling
    heap.build_heap([])
    record_test("1.5.5 Empty array handling", len(heap.heap) == 0)

# 🚀 Run tests
test_1_5()

# 📋 Summary
for r in test_results:
    print(r)