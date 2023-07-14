story = '''once upon a time there was a boy named Vikas trying to learn Python.
    Vikas is a good guy.'''


print(len(story))


print(story.endswith("Python"))    # Are the story ends with Python?
print(story.endswith("upon"))      # Are the story ends with upon?


print(story.count("a"))                #Counting charactor "a".
print(story.count("Vikas"))            #Counting string "Vikas".


print(story.capitalize())          # It Capitalize the first charactor of the sentance. 


print(story.find("Vikas"))            # Finding the index of First word.
                                   # If it find, it gives the Index or if not,
                                   # it gives -1


print(story.replace("Vikas", "Codewithvikas"))     # It changes every "Vikas" to "Codewithvikas".
