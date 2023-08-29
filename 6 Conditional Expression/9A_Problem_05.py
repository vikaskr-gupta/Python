names = ["Vikas", "Rahul", "Avanish", "Manish"]

name = input("Enter Your Name : ")

if(name in names):
    print("Your Name is Present in the list!")
else:
    print("Not matched!!!")

#***********************************************************
# Another Way

name = ["Vikas", "Rahul", "Manish", "Avanish"]
print(name)

text = input("Enter a name : ")

if("Vikas" in text):
    find = True
elif("Rahul" in text):
    find = True
elif("Manish" in text):
    find = True
elif("Avanish" in text):
    find = True
else:
    find = False


if(find):
    print("Mached!!!")
else:
    print("Not matched.")
