m = int(input("Enter your marks : "))

if(m >= 90 and m <= 100):
    print("Exelent")
elif(m >= 80 and m <= 89):
    print("A Grade")
elif(m >= 70 and m <= 79):
    print("B Grade")
elif(m >= 60 and m <= 69):
    print("C Grade")
elif(m >= 50 and m <= 59):
    print("D Grade")
elif(m < 50):
    print("Fail")

#************************************************
# Another way

m = int(input("Enter your marks : "))

if(m >= 90 and m <= 100):
    Grade = "Exelent"
elif(m >= 80 and m <= 89):
    Grade = "A"
elif(m >= 70 and m <= 79):
    Grade = "B"
elif(m >= 60 and m <= 69):
    Grade = "C"
elif(m >= 50 and m <= 59):
    Grade = "D"
elif(m < 50):
    Grade = "F"

print("Your Grade is : " + Grade)   # Concadinating
