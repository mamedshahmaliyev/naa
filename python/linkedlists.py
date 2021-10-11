class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


node0 = Node(1)

head = node0

node1 = Node(4)
head.next = node1

node2 = Node(-5)
node1.next = node2