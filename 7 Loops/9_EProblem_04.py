num = int(input("Enter a Number ")) 
prime = True

for i in range(2, num):
    if (num%i == 0):
        prime = False
        break
if prime:
    print("This is Print Number...")
else:
    print("This is not a Prime Number")
