
#class Stack:
 # def __init__(self):
  #  self.stack = []
  #  def add(self, dataval):
    # Use list append method to add element
#     if dataval not in self.stack:
#      self.stack.append(dataval)
 #     return True
  #   else:
  #    return False
# Use peek to look at the top of the stack
  #  def peek(self):
  #   return self.stack[-1]
#AStack = Stack()
#AStack.add("Mon")
#AStack.add("Tue")
#AStack.peek()
#print(AStack.peek())
#O/P = TUE,THUR

#class Stack:
   #  def __init__(self):
  #    self.stack = []
  #   def add(self, dataval):
# Use list append method to add element
     # if dataval not in self.stack:
    #   self.stack.append(dataval)
     #  return True
     # else:
       #   return False

# Use list pop method to remove element
     #def remove(self):
     # if len(self.stack) <= 0:
     #  return ("No element in the Stack")
     # else:
     #  return self.stack.pop()
#AStack = Stack()
#AStack.add("Mon")
#AStack.add("Tue")
#AStack.add("Wed")
#AStack.add("Thu")
#print(AStack.remove())
#print(AStack.remove())


#poping stack

#stack=[]
#stack.append(1)
#stack.append(2)
#stack.append(3)
#print("Intial Stack",stack)
#print("Element popped from the stack")
#print(stack.pop())
#print(stack.pop())
#print("Stack after popping some elements",stack)


# Function to print element and NGE pair for all elements of list
def printNGE(arr):
 for i in range(0, len(arr), 1):
  next = -1
 for j in range(i+1, len(arr), 1):
  if arr[i] < arr[j]:
   next = arr[j]
  break

 print(str(arr[i]) + " -- " + str(next))
# Driver program to test above function
arr = [11,13,21,3]
printNGE(arr)
