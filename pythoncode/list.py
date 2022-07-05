# print a given list 
#list = ["apple", "banana", "cherry"]
#print(list)

#Print the second item of the list:
#list = ["apple", "banana", "cherry"]
#print(list[1])

#Print the secondlast item of the list:
#thislist = ["apple", "banana", "cherry"]
#print(thislist[-2])

#Return the third, fourth, and fifth item:

#list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(list[2:5])

#This example returns the items from the beginning to, but NOT including,"kiwi":
#list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(list[:4])
#By leaving out the end value, the range will go on to the end of the list:

#This example returns the items from "cherry" to the end:
#thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(thislist[2:])

#This example returns the items from "orange" (-4) to, but NOT including"mango" (-1): range of nehative index value
#thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(thislist[-4:-1])

#To determine how many items a list has, use the len() function:Example Print the number of items in the list:
#thislist = ["apple", "banana", "cherry"]
#print(len(thislist))

#What is the data type of a list?
#mylist = ["apple", "banana", "cherry"]
#print(type(mylist))
#mylist = ["true", "false", "true"]
#print(type(mylist))

#Change Item ValueTo change the value of a specific item, refer to the index number:Change the second item:
#list = ["apple", "banana", "cherry"]
#list[1] = "blackcurrant"
#print(list)

#Change a Range of Item ValuesChange the values "banana" and "cherry" with the values "blackcurrant"and "watermelon":
#list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
#list[1:3] = ["blackcurrant", "watermelon"]
#print(list)

#Change the second value by replacing it with two new values:
#thislist = ["apple", "banana", "cherry"]
#thislist[1:2] = ["blackcurrant", "watermelon"]
#print(thislist)
#Note: The length of the list will change when the number of itemsinserted does not match the number of items replaced

#Change the second and third value by replacing it with one value:
#thislist = ["apple", "banana", "cherry"]
#thislist[1:3] = ["watermelon"]
#print(thislist)

#Insert "watermelon" as the third item: To insert a new list item, without replacing any of the existing values, wecan use the insert() method.
#thislist = ["apple", "banana", "cherry"]
#thislist.insert(2, "watermelon")
#print(thislist)

#To add an item to the end of the list, use the append() method:Using the append() method to append an item:
#thislist = ["apple", "banana", "cherry"]
#thislist.append("orange")
#print(thislist)

#To append elements from another list to the current list, usethe extend() method.
#thislist = ["apple", "banana", "cherry"]
#tropical = ["mango", "pineapple", "papaya"]
#thislist.extend(tropical)
#print(thislist)

#The remove() method removes the specified item.Remove "banana":
#thislist = ["apple", "banana", "cherry"]
#thislist.remove("banana")
#print(thislist)

#Remove Specified Index The pop() method removes the specified index.Remove the second item:
#thislist = ["apple", "banana", "cherry"]
#thislist.pop(1)
#print(thislist)

#The del keyword also removes the specified index:Remove the first item:
#thislist = ["apple", "banana", "cherry"]
#del thislist[0]
#print(thislist)

#Delete the entire list:
#thislist = ["apple", "banana", "cherry"]
#del thislist

#Print all items in the list, one by one:useing loops
#list = ["apple", "banana", "cherry"]
#for x in list:
#print(x)

#You can also loop through the list items by referring to their indexnumber.
# the range() and len() functions to create a suitable iterable.Print all items by referring to their index number:
#list = ["apple", "banana", "cherry"]
#for i in range(len(list)):
 #print(list[i])

#Print all items, using a while loop to go through all the index numbers
#list = ["apple", "banana", "cherry"]
# = 0
#while i < len(list):
#print(list[i])
#i = i + 1


#append() Adds an element at the end of the list
#clear() Removes all the elements from the list
#count() Returns the number of elements with the specified value
#extend() Add the elements of a list (or any iterable), to the end of the current list
#index() Returns the index of the first element with the specified value
#insert() Adds an element at the specified position
#pop() Removes the element at the specified position
#remove() Removes the item with the specified value
#reverse() Reverses the order of the list
#sort() Sorts the list

