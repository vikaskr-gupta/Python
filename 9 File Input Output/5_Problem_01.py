# f = open('poem.txt', 'r')

# t = f.read()
# if 'twinkle' in t:
#     print("Twinkle is present in the text.")
# else:
#     print("Twinkle is NOT present in the text.")

# f.close()


#*********************************************
# SECOND METHOD
with open('poems.txt', 'r') as f:
    t = f.read()

if 'twinkle' in t:
     print("Twinkle is present in the text.")
else:
    print("Twinkle is NOT present in the text.")
