# If languages of two friends are the same, what will happen to the program in problem 6
info ={}

name1 = input("Enter your name: ")
lang1 = input("Enter your language: ")
info.update({name1: lang1})

name2 = input("Enter your name: ")
lang2 = input("Enter your language: ")
info.update({name2: lang2})


name3 = input("Enter your name: ")
lang3 = input("Enter your language: ")
info.update({name3: lang3})


name4 = input("Enter your name: ")
lang4 = input("Enter your language: ")
info.update({name4: lang4}) # we can keep on updating to change the info

print(info)
# when it's about values like language, nothing will happen, only gets updated when it's about the key