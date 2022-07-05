# #creating root 
# class Node:
#        def __init__(self, data):
#            self.left = None
#            self.right = None
#            self.data = data
#        def PrintTree(self):
#            print(self.data)

# root = Node(10)
# root.PrintTree()



#def binary_search(list1, n):
 #   low = 0
 #   high = len(list1) - 1
 #   mid = 0

 #   while low <= high:
 # for get integer result
  #   mid = (high + low) // 2
 # Check if n is present at mid
  #  if list1[mid] < n:
  #   low = mid + 1

# If n is greater, compare to the right of mid
  #  elif list1[mid] > n:
  #   high = mid - 1

 # If n is smaller, compared to the left of mid
   # else:
   #   return mid
 # element was not present in the list, return -1
  #    return -1
 # Initial list1
#list1 = [12, 24, 32, 39, 45, 50, 54]
#n = 45
 # Function call
#result = binary_search(list1, n)

#if result != -1:
 #  print("Element is present at index", str(result))
#else:
 #   print("Element is not present in list1")
 
 
 
#list1 = [12, 24, 32, 39, 45, 50, 54]
#n = 32

 # Function call
#res = (list1, 0, len(list1)-1, n)
#if res != -1:
# print("Element is present at index", str(res))
#else:
#print("Element is not present in list1")



#def binary_search(list1, low, high, n):   
  
   # Check base case for the recursive function  
  # if low <= high:  
  
     # mid = (low + high) // 2  
  
      # If element is available at the middle itself then return the its index  
     # if list1[mid] == n:   
       #  return mid   
  
      # If the element is smaller than mid value, then search moves  
      # left sublist1  
     # elif list1[mid] > n:   
     #    return binary_search(list1, low, mid - 1, n)   
  
      # Else the search moves to the right sublist1  
     # else:   
       #  return binary_search(list1, mid + 1, high, n)   
  
   #else:   
      # Element is not available in the list1  
     # return -1  
  
# Test list1ay   
#list1 = [12, 24, 32, 39, 45, 50, 54]  
#n = 32  
  
# Function call   
#res = binary_search(list1, 0, len(list1)-1, n)   
  
#if res != -1:   
 #  print("Element is present at index", str(res))  
#else:   
  # print("Element is not present in list1") 
  
  
  
  
  #find the longest substring without repeating
#class Solution(object):
  #  def lengthOfLongestSubstring(self, s):
  #     i =0
  #     j = 0
   #    d={}
   #    ans = 0
    #   while j < len(s):
      #  if s[j] not in d or i>d[s[j]]:
     #    ans = max(ans,(j-i+1))
      #  d[s[j]] = j
     #  else:
     #   i = d[s[j]]+1
      #  ans = max(ans,(j-i+1))
     #   j-=1
#print(ans)
     #  j+=1
     #  return ans
#ob1 = Solution()
#print(ob1.lengthOfLongestSubstring("ABCABCBB"))

# # inserting a tree
# class Node:
#        def __init__(self, data):
#           self.left = None
#           self.right = None
#           self.data = data

#        def insert(self, data):
# # Compare the new value with the parent node
#           if self.data:
#            if data < self.data:
#             if self.left is None:
#                self.left = Node(data)
#             else:
#                self.left.insert(data)
#            elif data > self.data:
#                if self.right is None:
#                   self.right = Node(data)
#                else:
#                   self.right.insert(data)
#           else:
#                     self.data = data

# # Print the tree
#           def PrintTree(self):
#             if self.left:
#              self.left.PrintTree()
#             print( self.data),
#             if self.right:
#              self.right.PrintTree()

# # Use the insert method to add nodes
# root = Node(12)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.PrintTree()