f = open('sample.txt','r')

# Read first line
data = f.readline()
print(data)

# Read second line
data = f.readline()
print(data)

# Read third line
data = f.readline()
print(data)

# Read fourth line... so on....
data = f.readline()
print(data)

f.close()
