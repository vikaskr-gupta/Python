num1 = int(input("Enter First numbers... "))
num2 = int(input("Enter Second numbers... "))
num3 = int(input("Enter Third numbers... "))

def greater(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3


G = greater(num1, num2, num3)
print("The greatest number is " + str(G))
