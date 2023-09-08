# this = "      Vikas Kumar Gupta        "

# print(this)
# print(this.strip())

#*************************************


def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "        Vikas is a Good boy         "
n = remove_and_split(this, "Vikas")

print(n)
