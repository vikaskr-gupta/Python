n = int(input("Enter a number... "))

def sum(n):
    if(n == 0 or n == 1):
        return 1
    return  n + sum(n-1)

print(sum(n))
