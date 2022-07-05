#Create a Tuple:
#tuple = (1,2,3,4,5)
#print(tuple)

#Print the number of items in the tuple:
#tuple = ("apple", "banana", "cherry")
#print(len(tuple))

#Create Tuple with One ItemTo create a tuple with only one item, you have to add a comma after the
#item, otherwise Python will not recognize it as a tuple.One item tuple, remember the comma:
#tuple = ("apple",)

#Print the second item in the tuple: 
#thistuple = ("apple", "banana", "cherry")
#print(thistuple[1])

#Print the last item of the tuple:
#thistuple = ("apple", "banana", "cherry")
#print(thistuple[-1])

#Return the third, fourth, and fifth item:
#thistuple =("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#print(thistuple[2:5])
#Note: The search will start at index 2 (included) and end at index 5 (notincluded).

#This example returns the items from the beginning to, but NOT included,"kiwi":
#thistuple =("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#print(thistuple[:4])

#This example returns the items from "cherry" and to the end:

#thistuple =("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#print(thistuple[2:])
#This example returns the items from index -4 (included) to index -1(excluded)
#thistuple =("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#print(thistuple[-4:-1])

#Check if "apple" is present in the tuple:
#thistuple = ("apple", "banana", "cherry")
#if "apple" in thistuple:
 #print("Yes, 'apple' is in the fruits tuple")
 
 
 #Convert the tuple into a list to be able to change it:
#x = ("apple", "banana", "cherry")
#y = list(x)
#y[1] = "kiwi"
#x = tuple(y)
#print(x)

#Convert the tuple into a list, add "orange", and convert it back into atuple:
#thistuple = ("apple", "banana", "cherry")
#y = list(thistuple)
#y.append("orange")
#thistuple = tuple(y)

#Create a new tuple with the value "orange", and add that tuple:
#thistuple = ("apple", "banana", "cherry")
#y = ("orange",)
#thistuple += y
#print(thistuple)
#Note: When creating a tuple with only one item, remember to include acomma after the item, otherwise it will not be identified as a tuple.




# Python3 implementation of the approach

		
# Python 3 implementation of the above approach

# Function to find the maximum number
# of 1's before 0
def noOfMoves(arr,n):
	cnt = 0
	maxCnt = 0

	# Traverse the array
	for i in range(n):
		# If value is 1
		if (arr[i] == 1):
			cnt += 1
		else:
			# If consecutive 1 followed
			# by 0, then update the maxCnt
			if (cnt != 0):
				maxCnt = max(maxCnt, cnt)
				cnt = 0

	# Print the maximum consecutive 1's
	# followed by 0
	print(maxCnt)

# Driver Code
if __name__ == '__main__':
	arr = [1, 0, 0, 1, 1, 0] 
	N = len(arr)

	# Function Call
	noOfMoves(arr, N)
	arr1 = [1, 0, 0, 1, 1, 0 ]
	N = len(arr1)

	# Function Call
	noOfMoves(arr1, N)


