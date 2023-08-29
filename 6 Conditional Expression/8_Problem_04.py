char = input("Enter a Word : ")

if(len(char)  <= 10):
    char = True
elif(len(char) > 10):
    char = False

if(char):
    print("Done!")
else:
    print("Invalid Username, Try Again!")
