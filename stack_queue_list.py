class Stack:
  def __init__(self):
    self._data = []

  def push(self, val):
    self._data.insert(0, val)
    return

  def pop(self):
    return self._data.pop()

  def length(self):
    return len(self._data)

