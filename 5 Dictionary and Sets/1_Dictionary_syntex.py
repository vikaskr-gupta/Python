myDict = {
    "fast" : "In a quick manner",
    "creteria" : "Identification Mark",
    "marks" : [1, 4, 7, 8, 76],

    "anotherDict" : {"vikas" : "A goood boy"},
    76 : 7619984304
}

print(myDict['fast'])
print(myDict['creteria'])
print(myDict['marks'])
print(myDict['anotherDict']['vikas'])

myDict['marks'] = [76,76,76]
print(myDict['marks'])              # It is Mutable(Changable)

print(myDict[76])
