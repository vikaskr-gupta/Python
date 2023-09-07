cel = int(input("Enter Temperature... "))

def fornh(cel):
    return (cel * (5/9)) + 32
    
F = fornh(cel)
print("The temperature in Fohreignhight is " + str(F))
