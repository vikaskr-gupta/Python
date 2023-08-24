sub1 = int(input("Enter your first subject marks : "))
sub2 = int(input("Enter your second subject marks : "))
sub3 = int(input("Enter your third subject marks : "))

if(sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("You are fail because you have less than 33 marks in one of the subject")
elif((sub1 + sub2 + sub3)/3 < 40):
    print("Your are fail because you have less than 40% marks in overall subjects")
else:
    print("Congratulations! You are Passed")
