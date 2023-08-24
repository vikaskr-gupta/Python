num1 = int(input("Enter First Number : \n"))
num2 = int(input("Enter Second Number : \n"))
num3 = int(input("Enter Third Number : \n"))
num4 = int(input("Enter Fourth Number : \n"))

if(num1 > num2):
    f1 = num1
else:
    f1 = num2

if(num3 > num4):
    f2 = num3
else:
    f2 = num4

if(f1 > f2):
    print("The Greatest Number is", str(f1))
else:
    print("The Greatest Number is", str(f2))
