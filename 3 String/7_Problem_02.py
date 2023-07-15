latter = '''Dear, <NAME>
From, ABC Company
We are Happy to tell you about your selection.
You are Selected.
Congratulations!!!
Date : <DATE>'''

name = input("Enter Your Name\n")
date = input("Enter Date\n")

latter = latter.replace("<NAME>", name)
latter = latter.replace("<DATE>", date)

print(latter)
