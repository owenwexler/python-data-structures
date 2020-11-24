class Node:
  def __init__(self, val):
    self.value = val
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add(self, val):
    new_node = Node(val)

    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node

    self.tail.next = new_node
    self.tail = new_node

  def remove_head(self):
    if self.head is None:
      return None

    old_head = self.head

    if old_head.next is None:
      self.head = None
    else:
      self.head = old_head.next

    return old_head

  def contains(self, val):
    if self.head is None and self.tail is None:
      return False

    current_node = self.head

    while current_node:
      if current_node.value == val:
        return True

      current_node = current_node.next

    return False

  def length(self):
    if self.head is None and self.tail is None:
      return False

    result = 0
    current_node = self.head

    while current_node:
      result += 1
      current_node = current_node.next

    return result

  def log(self):
    if self.head is None and self.tail is None:
      return ""

    result = ""
    current_node = self.head

    while current_node:
      if current_node.next is None:
        result += str(current_node.value)
      else:
        result += str(current_node.value)
        result += " -> "
      current_node = current_node.next

    return result

  def remove(self, val):
    if self.head is None and self.tail is None:
      return None

    prev_node = self.head

    if not prev_node.next:
      if prev_node.value == val:
        self.head = None
        self.tail = None

      return None

    current_node = prev_node.next

    while current_node:
      if current_node.value == val:
        if not current_node.next:
          self.tail = prev_node
          self.tail.next = None
          return current_node
        else:
          prev_node.next = current_node.next
          return current_node
      prev_node = current_node
      current_node = current_node.next

    return None

llist = SinglyLinkedList()
llist.add(4)
llist.add(5)
llist.add(6)
llist.add(7)
llist.add(8)
llist.add(9)
print(llist.log())
print("contains 4: " + str(llist.contains(4)))
print("contains 7: " + str(llist.contains(7)))
print("contains 12: " + str(llist.contains(12)))
print("length: " + str(llist.length()))
llist.remove_head()
print(llist.log())
print("contains 4: " + str(llist.contains(4)))
print("length: " + str(llist.length()))
llist.remove(8)
print(llist.log())
print("contains 8: " + str(llist.contains(8)))
print("length: " + str(llist.length()))
llist.remove(9)
print(llist.log())
print("contains 9: " + str(llist.contains(9)))
print("length: " + str(llist.length()))