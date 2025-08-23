# create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique

info = {
    "Taha": "English", # keys are the name, values are the languages
    "Nishat": "Japanese",
    "Sahat": "Bengali",
    "Ishrat": "Mandarin"
}
#info["Ishrat"] = "Mandarin" # This is how we can add
#info.update({"Taha": "Japanese"}) # this is how we can update it
print(info["Taha"], info["Nishat"], info["Sahat"], info["Ishrat"])