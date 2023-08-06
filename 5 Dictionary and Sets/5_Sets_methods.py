# Creating an empty set
a = set()
print(type(a))


##### Adding an element in an empty set*********************
a.add(4)
a.add(6)
a.add(9)

a.add(4)                     # Repeation is not allowed!!!
a.add(4)


##### Accessing Element 
# a.add([4, 5, 6])           # We cannaot add list or Dictionary in any set...
# a.add({5 : 7619984304})    #...because they are Unhashable(Changable)

a.add((5,6,7,8,9))           # Adding Tupple in an empty set and this is Alowed Because it is Hashable(Unchangable)


##### Length of the Set**************************************
print(len(a))                # Print the length of the set


##### Removal of an Element**********************************
a.remove(6)                  # Removes 6 from the set a
# a.removes(76)              # Through an Error!!! while trying to remove 76(Bec. 76 is not present in the set a)
print(a)


##### A Kind of Method***************************************
print(a.pop())        # It removes the any arbitary element from the set and print the removed element
print(a)


##### Clear the Set******************************************
print(a.clear())
