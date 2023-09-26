class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

head = Node('head')

node1 = Node(90)
node2 = Node(2)
node3 = Node(77)
node4 = Node(35)
node5 = Node(21)

node1.next= node2
node2.next = node3
node3.next  = node4
node4.next = node5

head.next =node1

head.next.next.next.data