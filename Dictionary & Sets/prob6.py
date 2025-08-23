# create a dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique
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




#info["Ishrat"] = "Mandarin" # This is how we can add
#info.update({"Taha": "Japanese"}) # this is how we can update it