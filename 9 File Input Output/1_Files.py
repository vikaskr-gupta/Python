#************* Use open function to read the content of a file!*************

f = open('sample.txt', 'r')
# f = open('sample.txt')   #By default the mode is 'r'.

data = f.read()
# data = f.read(5)   #Read first five character from the file

print(data)
f.close()

# r --> open for reading
# w --> open for writing
# a --> open for appending
# + --> open for updating

# 'rb' will open for read in binary mode
# 'rt' will open for read in text mode
