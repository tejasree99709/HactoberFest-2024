class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def size(self):
        return len(self.items)

queue = Queue()
while True:
    action = input("Enter 'enqueue', 'dequeue', or 'exit': ")
    if action == 'enqueue':
        item = input("Enter an item to enqueue: ")
        queue.enqueue(item)
    elif action == 'dequeue':
        item = queue.dequeue()
        if item is not None:
            print(f"Dequeued: {item}")
        else:
            print("Queue is empty.")
    elif action == 'exit':
 
