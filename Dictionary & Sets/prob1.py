# write a program to create a dictionary of Bengali words with values as their English translation. Prove user with an option to look it up

words = {
    "Sahajjo": "Help", 
    "kaj": "work",
    "khabar": "food",
    "alo": "Tahsan"
}

meaning = input("Enter words: ")
print(words[meaning]) # The reason we printed meaning because, the moment we using input, we gettings words, if we print words[meaning], menaing is just indirectly the answer from input. 
