#def enqueue(q, e):
  #  q.append(e)
  #  return q
#def dequeue(q):
   # del q[0]
    #return q
#q = []
#enqueue(q,1)
#enqueue(q,5)
#enqueue(q,6)
#print(q)

#def firstNonRepeatingChar(str1):
 #   char_order = []
  #  counts = {}
   # for c in str1:
   #  if c in counts:
    #  counts[c] += 1
    #else:
   #   counts[c] = 1
   # char_order.append(c)
  #  for c in char_order:
   #  if counts[c] == 1:
   #   return c
  #  return None
#print(firstNonRepeatingChar('PythonforallPythonMustforall'))
#print(firstNonRepeatingChar('tutorialspointfordeveloper'))
#print(firstNonRepeatingChar('AABBCC'))

#Given an array of integers nums.
#A pair (i,j) is called good if nums[i] == nums[j]
#and i < j. Return the number of good pairs.
#Example 1:
#Input: nums =
#[1,2,3,1,1,3] Output: 4
#Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexe
#Out". It is also known as "first come first severed". The queue has the two ends front
#and rear. The next element is inserted from the rear end and removed from
#the front end.
#def solve(nums):
 #count=0
# n=len(nums)
# for i in range(n):
 #  for j in range(i+1,n):
  #  if nums[i] == nums[j]:
  #   count+=1
 #return count
#nums = [5,6,7,5,5,7]
#print(solve(nums))


# Longest Substring Without Repeating Characters

#class Solution(object):
 #   def lengthOfLongestSubstring(self, s):
 #    i =0
 #    j = 0
  #   d={}
   #  ans = 0
  #   while j < len(s): 
   #     if s[j] not in d or i>d[s[j]]:
   #          ans = max(ans,(j-i+1))
    #         d[s[j]] = j
    # else:
     #    i = d[s[j]]+1
      #   ans = max(ans,(j-i+1))
      #   j-=1
 #print(ans)
       #  j+=1
       #  return ans
#ob1 = Solution()
#print(ob1.lengthOfLongestSubstring("bbBB"))

#Two Sum
#class Solution(object):
   #  def twoSum(self, nums, target):
      #   """
    #     :type nums: List[int]
      #   :type target: int
      #  :rtype: List[int]
       #  """
       #  required = {}
       #  for i in range(len(nums)):
        #   if target - nums[i] in required:
       #     return [required[target - nums[i]],i]
       #  else:
       #     required[nums[i]]=i
#input_list = [2,8,12,15]
#ob1 = Solution()
#print(ob1)




# #adding of Elementclass Queue:
# class Queue:
#    def __init__(self):
#       self.queue = list()

#    def addtoq(self,dataval):
# # Insert method to add element
#     if dataval not in self.queue:
#          self.queue.insert(0,dataval)
#          return True
#     return False

#    def size(self):
#       return len(self.queue)

# TheQueue = Queue()
# TheQueue.addtoq("Mon")
# TheQueue.addtoq("Tue")
# TheQueue.addtoq("Wed")
# print(TheQueue.size())


   