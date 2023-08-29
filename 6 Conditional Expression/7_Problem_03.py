text = input("Enter the Text : ")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("click here" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This is Spam")
else:
    print("This is not A Spam")
