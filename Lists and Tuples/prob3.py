# check that a tuple type cannot be changed in python
try:
    
   tuples = (1, 2, 4)
   tuples[2] = "Taha" # so we knew our program will crash since a tuple type cannot be changed in python, in order to avoid crashing, we used this method which prints out Invalid action

   print(tuples)
except TypeError:
   print("Invalid action")