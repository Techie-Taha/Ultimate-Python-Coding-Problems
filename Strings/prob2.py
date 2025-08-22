# write a program to fill in a letter template given below with name and date
"""
letter = 
Dear <|Name|>,
You are selected!
<|Date|>,

"""

letter = "Dear <|Name|>,"
result_1 = letter.replace("<|Name|>" , "Taha")

letter_2 = "<|Date|>"
result_2 = letter_2.replace("<|Date|>" , "08/22/25")

print(result_1)
print("You are selected!")
print(result_2)

# or we can chaining the replace method
letter = """
Dear <|Name|>,
You are selected!
<|Date|>
"""

print(letter.replace("<|Name|>" , "Taha").replace("<|Date|>" , "08/22/25"))