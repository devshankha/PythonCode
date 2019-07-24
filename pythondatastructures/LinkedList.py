class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

    def getNextNode(self):
        return self.next

class LinkedList:
    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_end(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                return
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node;

    def addNode(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return True

    def traverse_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, " ")
                n = n.next

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()

L = LinkedList()
L.insert_at_end(1)
L.insert_at_end(2)
L.insert_at_end(3)
L.traverse_list()









