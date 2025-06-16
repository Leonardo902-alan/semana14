test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add item to rear."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return front item or None if empty."""
        if self.items:
            return self.items.pop(0)
        return None

    def peek(self):
        """Return front item without removing or None if empty."""
        if self.items:
            return self.items[0]
        return None

def test_o5_1():
    q = Queue()
    record_test("o5.1.1 empty behavior",
        q.dequeue() is None and q.peek() is None)

    q.enqueue(1); q.enqueue(2); q.enqueue(3)
    record_test("o5.1.2 FIFO order",
        q.dequeue() == 1 and q.dequeue() == 2 and q.dequeue() == 3)

    q.enqueue("x")
    record_test("o5.1.3 peek preserves",
        q.peek() == "x" and q.dequeue() == "x")

    q.enqueue(None); q.enqueue("y")
    record_test("o5.1.4 mixed types",
        q.peek() is None and q.dequeue() is None)

    val1 = q.dequeue(); val2 = q.peek()
    record_test("o5.1.5 return types",
        isinstance(val1, (int,str,type(None))) and isinstance(val2, (int,str,type(None))))

# 🚀 Run tests
test_o5_1()

# 📋 Summary
for r in test_results:
    print(r)
