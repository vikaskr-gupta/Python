a = "345543"   # "a" is here String Type
b = int(a)     # Now "a" is Integer Type(If Possible)
c = 5          # c is Integer Type

print(type(a))
print(type(b))
print(type(c))

# print(a + c)       # This is invailid because we add string + integer
print(b + c)         # Here, b is converting string-integer, add int + int & then print

d = 76             # "d" is here Numeric type
e = str(d)         # Now "d" is String Type
f = float(d)       # Now "d" is Float Type

print(type(d))
print(type(e))
print(type(f))