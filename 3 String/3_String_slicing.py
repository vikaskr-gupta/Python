name = "Vikas"

# The Index in a String start from 0 to (Length-1)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5])          Out of Range
# print(name[ ])          Empty String is not possible


#*************** String Slicing ****************

# Here the Index in a String is start from 0 to Length
print(name[0 : 5])
print(name[ : 5])     # is same as name[0 : 5]
print(name[0 : ])     # is same as name[0 : 5]
print(name[ : ])      # It printed all characters
print(name[0 : 1])
print(name[0 : 3])
print(name[2 : 4])
print(name[2 : ])     # is same as name[2 : 5]


#*************** Negative Indices **************

print(name[-4 : -1])   # is same as name[1 : 4]


#*********** Slicing with Skip Value ***********

name = "VikasIs Good"

# name[3] = d              #You do not change any character by writing this 
print(name[0 : 11: 2])     #It skip's every second value
print(name[ : : 3])        #It skip's every third value
print(name[ : 11 : 2])     #It skip's every second value
print(name[0 : : 3])       #It skip's every third value
# Spaces are also count...

'''**********************************************************************
    word[0 : 7]  =  word[  : 7]  =  word[0 : ]     #if word have 8 values
    First word or Last word automatically defined!!!  '''
