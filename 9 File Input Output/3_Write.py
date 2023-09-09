# Uses of 'w' for writing --------------------


f = open('firstsample.txt', 'w')   # If there is no such files(firstsample.txt) , it creates the text-file and writes them in.

# f.write("Please write this in the firstsample file.")
f.write("PLEASE WRITE THIS IN THE FIRSTSAMPLE FILE.")   #If we change something in the text, this text is overwrite on the other text.

f.close()


#***************************************************************************************************
# Uses of 'a' for appending -------------------

f = open('secondsample.txt', 'a')

f.write("Here, I am appending...")   # We can write text Any no. of times through running the this code again and again.

f.close()
