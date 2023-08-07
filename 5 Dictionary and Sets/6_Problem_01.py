myDict = {
    "Fan" : "Pankha",
    "Box" : "Dabba",
    "Things" : "Vastu"
}
print("Options are", myDict.keys())
a = input("Enter the English Word\n")

# print("The Hindi meaning of your Word is : ", myDict[a])
# Below line will not throw an error if the key is not present in the list
print("The Hindi meaning of your word is : ", myDict.get(a))
