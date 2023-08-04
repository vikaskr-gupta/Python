myDict = {
    "fast" : "In a quick manner",
    "creteria" : "Identification Mark",
    "marks" : [1, 4, 7, 8, 76],

    "anotherDict" : {"vikas" : "A goood boy"},
    76 : 7619984304
}

print(list(myDict.keys()))        # Printing in the list form


# *********************Methods**********************

print(myDict.keys())         # Print the keys of dictionary
print(myDict.values())       # Print the value of keys of dictionary
print(myDict.items())        # Print the (keys, values) all contents of mtDict

print(myDict)
updateDict = {
    "Friend" : "Rahul",
    "marks"  : [1, 1, 1, 1, 1]         # It is Muatble(Changeble)
}
myDict.update(updateDict)
print(myDict)                # Update the dictionary by adding key-value pairs from updateDict

print(myDict.get("Friend"))           # Print value associated with key "Friend"
print(myDict["Friend"])               # Print value associated with key "Friend" with List method
# Defference .get Vs []*******************************************************************************
print(myDict.get("DearFriend"))       #Return None as DearFriend is not present in the Dictionary
# print(myDict["DearFriend"])           # Through Error!!! as DearFriend not present in the Dictionary


#*********************Types*************************

print(type(myDict.keys()))        # Print the type of keys
print(type(myDict.values()))        # Print the type of keys
