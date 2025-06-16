test_results = []

def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def delete_min(self):
        # Remove and return minimum element
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Store minimum value to return
        min_value = self.heap[0]
        
        # Replace root with last element
        self.heap[0] = self.heap.pop()
        
        # Restore heap property by bubbling down
        self._heapify_down(0)
        
        return min_value
    
    def _heapify_down(self, index):
        # Move element down to restore min-heap property
        while True:
            smallest = index
            left_idx = self._left_child_index(index)
            right_idx = self._right_child_index(index)
            
            # Check if left child exists and is smaller than current smallest
            if (self._has_left_child(index) and 
                self.heap[left_idx] < self.heap[smallest]):
                smallest = left_idx
            
            # Check if right child exists and is smaller than current smallest
            if (self._has_right_child(index) and 
                self.heap[right_idx] < self.heap[smallest]):
                smallest = right_idx
            
            # If no swap is needed, heap property is satisfied
            if smallest == index:
                break
            
            # Swap with the smaller child and continue down
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest
    
    def _left_child_index(self, index):
        return 2 * index + 1
    
    def _right_child_index(self, index):
        return 2 * index + 2
    
    def _has_left_child(self, index):
        return self._left_child_index(index) < len(self.heap)
    
    def _has_right_child(self, index):
        return self._right_child_index(index) < len(self.heap)
    
    def size(self):
        return len(self.heap)

def test_1_4():
    heap = MinHeap()
    
    # 1.4.1 Empty heap deletion
    result = heap.delete_min()
    record_test("1.4.1 Empty heap deletion", result is None)
    
    # 1.4.2 Single element deletion
    heap.heap = [5]
    result = heap.delete_min()
    record_test("1.4.2 Single element deletion", result == 5 and heap.size() == 0)
    
    # 1.4.3 Multiple deletions
    heap.heap = [1, 3, 2, 7, 4]
    first = heap.delete_min()
    second = heap.delete_min()
    record_test("1.4.3 Multiple deletions", first == 1 and second == 2)
    
    # 1.4.4 Heap property maintenance
    heap.heap = [1, 3, 2, 7, 4, 5]
    heap.delete_min()
    valid_heap = all(
        heap.heap[i] <= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.4.4 Heap property maintenance", valid_heap)
    
    # 1.4.5 Size tracking
    initial_size = heap.size()
    heap.delete_min()
    record_test("1.4.5 Size tracking", heap.size() == initial_size - 1)

# 🚀 Run tests
test_1_4()

# 📋 Summary
for r in test_results:
    print(r)