# create a Dictionary
#dict = {1:'abc',2:'egg',3:True,4:'gfsdsd'}
#print(dict)

#dict = { "brand": "Ford", "model": "Mustang", "year": 1964}
#print(dict)

#Dictionaries cannot have two items with the same key:ExampleDuplicate values will overwrite existing values:
#dict = {"brand": "Ford","model": "Mustang" "year": 1964,"year": 2020}
#print(dict)

#Print the number of items in the dictionary:
#print(len(dict))

#Print the data type of a dictionary:
#dict = {"brand": "Ford","model": "Mustang","year": 1964}
#print(type(dict))

#Get the value of the "model" key:
#dict = {"brand": "Ford","model": "Mustang","year": 1964}
#x = dict["model"]
#print(x)
#There is also a method called get() that will give you the same result:

#The keys() method will return a list of all the keys in the dictionaryGet a list of the keys:
#dict = {"brand": "Ford","model": "Mustang","year": 1964}
#x = dict.keys()
#print(x)

#Add a new item to the original dictionary, and see that the keys list getsupdated as well:
#car = {"brand": "Ford","model": "Mustang","year": 1964}
#x = car.keys()
#print(x)
#car["color"] = "white"
#print(x)

#Get a list of the values:
#thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
#x = thisdict.values()
#print(x)


#Make a change in the original dictionary, and see that the values list getsupdated as well:
#car = {"brand": "Ford","model": "Mustang","year": 1964}
#x = car.values()
#print(x) #before the change
#car["year"] = 2020
#print(x) #after the change

#Get a list of the key:value pairs
#thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
#x = thisdict.items()
#print(x)

#Add a new item to the original dictionary, and see that the items list getsupdated as well:
#car = {"brand": "Ford","model": "Mustang","year": 1964}
#x = car.items()
#print(x) #before the change
#car["color"] = "red"
#print(x) #after the change

#Check if "model" is present in the dictionary:
#thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
#if "model" in thisdict:
# print("Yes, 'model' is one of the keys in the thisdict dictionary")

#You can change the value of a specific item by referring to its key name:
#Change the "year" to 2018:
#thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
#thisdict["year"] = 2018

#Update the "year" of the car by using the update() method:
#thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
#thisdict.update({"year": 2020})

#Adding an item to the dictionary is done by using a new index key andassigning a value to it:

#thisdict = {
 #"brand": "Ford",
# "model": "Mustang",
## "year": 1964
#}
#thisdict["color"] = "red"
#print(thisdict)

#The pop() method removes the item with the specified key name:
#thisdict = {
 #"brand": "Ford",
 #"model": "Mustang",
 #"year": 1964
#}
#thisdict.pop("model")
#print(thisdict)

#The del keyword removes the item with the specified key name:
#thisdict = {
# "brand": "Ford",
# "model": "Mustang",
 #"year": 1964
#}
#del thisdict["model"]
#print(thisdict)

#The clear() method empties the dictionary:
#thisdict = {
 #"brand": "Ford",
 #"model": "Mustang",
# "year": 1964
#}
#thisdict.clear()
#print(thisdict)

#clear() Removes all the elements from the dictionary
#copy() Returns a copy of the dictionary
#fromkeys() Returns a dictionary with the specified keys and value
#get() Returns the value of the specified key
#items() Returns a list containing a tuple for each key value pair
#keys() Returns a list containing the dictionary's keys
#pop() Removes the element with the specified key
#popitem() Removes the last inserted key-value pair