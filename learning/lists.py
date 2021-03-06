#Python Collections (Arrays)
# There are four 'collection data types' in the Python programming language:

# 1) List is a collection which is ordered and changeable. Allows duplicate members.
# 2) Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# 3) Set (JS Objects) is a collection which is unordered and unindexed. No duplicate members.
# 4) Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

1) List
# list
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
thislist[1] = "blackcurrant"
print(thislist[1])
print(thislist)

# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
# check if item exist
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
# Remove Item list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
  
-=-=-=-=-=-=-=
2) Tuples
# You cannot change values in a tuple:
thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant"
# The values will remain the same:
print(thistuple)

# Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
=-=-=-=-=-=-=-=-=  
3) Sets (js Objects)
 You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
 
 # Loop through the set
 thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Add an item to a set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add multiple items to a set
mySet = {"apple", "banana", "cherry"}
mySet.update(["orange"])
print(mySet)
 
# Remove Item (if exist)
thisset = {"apple", "banana", "cherry"}
if "banana" in thisset:
  print(thisset)
  thisset.remove("banana") # {'cherry', 'banana', 'apple'}
  print(thisset) # {'cherry', 'apple'}
  
--=-=-=-=-=  
# 4) Dictionary

# Change Values 
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}


# return values of a dictionary
for x in thisdict.values():
  print(x)
  
  
# loop through both keys and values
for x, y in thisdict.items():
  print(x, y)
  
  
# Check if Key Exists. Get value from a key
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print( thisdict.get("model") ) # Mustang
  
  
# delete
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
