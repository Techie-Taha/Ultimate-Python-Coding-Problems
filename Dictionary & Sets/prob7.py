# If the the names of two friends are the same, what will happen to the program in problem 6

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
 # it execute line 5, 6, 7, it avoided like updated the dictionaries, if keys are the same it gets updated. 