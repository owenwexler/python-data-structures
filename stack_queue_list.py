class Stack:
  def __init__(self):
    self._data = []

  def push(self, val):
    self._data.insert(0, val)
    return

  def pop(self):
    removed_item = self._data[0]
    self._data.remove(self._data[0])
    return removed_item

  def length(self):
    return len(self._data)

  def log(self):
    return self._data

class Queue():
  def __init__(self):
    self._data = []

  def enqueue(self, val):
    self._data.append(val)
    return

  def dequeue(self):
    removed_item = self._data[0]
    self._data.remove(self._data[0])
    return removed_item

  def length(self):
    return len(self._data)

  def log(self):
    return self._data

# test_queue = Queue()
# test_queue.enqueue(1)
# test_queue.enqueue(2)
# test_queue.enqueue(3)
# test_queue.enqueue(4)
# print("current queue: ", test_queue.log())
# print("length: ", test_queue.length())
# print(test_queue.dequeue())
# print("current queue: ", test_queue.log())
# print("length: ", test_queue.length())
# test_queue.enqueue(5)
# test_queue.enqueue(6)
# print("current queue: ", test_queue.log())
# print("length: ", test_queue.length())
# print(test_queue.dequeue())
# print("current queue: ", test_queue.log())
# print("length: ", test_queue.length())

# test_stack = Stack()
# test_stack.push(4)
# test_stack.push(3)
# test_stack.push(2)
# test_stack.push(1)
# print("current stack: ", test_stack.log())
# popped_item = test_stack.pop()
# print("popped_item: ", popped_item)
# print("current stack: ", test_stack.log())