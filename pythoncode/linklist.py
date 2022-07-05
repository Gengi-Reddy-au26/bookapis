# traversing of list 
# #class Node:
#        def __init__(self, dataval=None):
#           self.dataval = dataval
#           self.nextval = None

# class SLinkedList:
#    def __init__(self):
#       self.headval = None

#    def listprint(self):
#       printval = self.headval
#       while printval is not None:
#          print (printval.dataval)
#          printval = printval.nextval

# list = SLinkedList()
# list.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")

# # Link first Node to second node
# list.headval.nextval = e2

# # Link second Node to third node
# e2.nextval = e3

# list.listprint()

# # insertion of item from start
# class Node:
#        def __init__(self, dataval=None):
#           self.dataval = dataval
#           self.nextval = None

# class SLinkedList:
#    def __init__(self):
#       self.headval = None
# # Print the linked list
#    def listprint(self):
#       printval = self.headval
#       while printval is not None:
#          print (printval.dataval)
#          printval = printval.nextval
#    def AtBegining(self,newdata):
#       NewNode = Node(newdata)

# # Update the new nodes next val to existing node
#       NewNode.nextval = self.headval
#       self.headval = NewNode

# list = SLinkedList()
# list.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")

# list.headval.nextval = e2
# e2.nextval = e3

# list.AtBegining("Sun")
# list.listprint()

# node removeing from end 
#class Node:
  #     def __init__(self, data=None):
  #      self.data = data
  #      self.next = None
# # class SLinkedList:
#        def __init__(self):
#           self.head = None

#    def Atbegining(self, data_in):
#       NewNode = Node(data_in)
#       NewNode.next = self.head
#       self.head = NewNode

# # Function to remove node
#    def RemoveNode(self, Removekey):
#       HeadVal = self.head
         
#       if (HeadVal is not None):
#          if (HeadVal.data == Removekey):
#             self.head = HeadVal.next
#             HeadVal = None
#             return
#       while (HeadVal is not None):
#          if HeadVal.data == Removekey:
#             break
#          prev = HeadVal
#          HeadVal = HeadVal.next

#       if (HeadVal == None):
#          return

#       prev.next = HeadVal.next
#       HeadVal = None

#    def LListprint(self):
#       printval = self.head
#       while (printval):
#          print(printval.data),
#          printval = printval.next

# llist = SLinkedList()
# llist.Atbegining("Mon")
# llist.Atbegining("Tue")
# llist.Atbegining("Wed")
# llist.Atbegining("Thu")
# llist.RemoveNode("Tue")
# llist.LListprint()

# #code to inserting between two node
 
# class Node:
#        def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None
# class SLinkedList:
#    def __init__(self):
#       self.headval = None

# # Function to add node
#    def Inbetween(self,middle_node,newdata):
#       if middle_node is None:
#          print("The mentioned node is absent")
#          return

#       NewNode = Node(newdata)
#       NewNode.nextval = middle_node.nextval
#       middle_node.nextval = NewNode

# # Print the linked list
#    def listprint(self):
#       printval = self.headval
#       while printval is not None:
#          print (printval.dataval)
#          printval = printval.nextval

# list = SLinkedList()
# list.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Thu")

# list.headval.nextval = e2
# e2.nextval = e3

# list.Inbetween(list.headval.nextval,"Fri")

# list.listprint()


# #removeing an item
# class Node:
#        def __init__(self, data=None):
#         self.data = data
#         self.next = None
# class SLinkedList:
#    def __init__(self):
#       self.head = None

#    def Atbegining(self, data_in):
#       NewNode = Node(data_in)
#       NewNode.next = self.head
#       self.head = NewNode

# # Function to remove node
#    def RemoveNode(self, Removekey):
#       HeadVal = self.head
         
#       if (HeadVal is not None):
#          if (HeadVal.data == Removekey):
#             self.head = HeadVal.next
#             HeadVal = None
#             return
#       while (HeadVal is not None):
#          if HeadVal.data == Removekey:
#             break
#          prev = HeadVal
#          HeadVal = HeadVal.next

#       if (HeadVal == None):
#          return

#       prev.next = HeadVal.next
#       HeadVal = None

#    def LListprint(self):
#       printval = self.head
#       while (printval):
#          print(printval.data),
#          printval = printval.next

# llist = SLinkedList()
# llist.Atbegining("Mon")
# llist.Atbegining("Tue")
# llist.Atbegining("Wed")
# llist.Atbegining("Thu")
# llist.RemoveNode("Tue")
# llist.LListprint()



# # advanced linklist
# class Node:
#    def __init__(self, data):
#       self.data = data
#       self.next = None
#       self.prev = None

# class doubly_linked_list:
#    def __init__(self):
#       self.head = None

# # Adding data elements		
#    def push(self, NewVal):
#       NewNode = Node(NewVal)
#       NewNode.next = self.head
#       if self.head is not None:
#          self.head.prev = NewNode
#       self.head = NewNode

# # Print the Doubly Linked list		
#    def listprint(self, node):
#       while (node is not None):
#          print(node.data),
#          last = node
#          node = node.next

# dllist = doubly_linked_list()
# dllist.push(12)
# dllist.push(8)
# dllist.push(62)
# dllist.listprint(dllist.head)