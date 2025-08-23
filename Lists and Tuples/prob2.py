# write a program to accept marks of 6 students and display them in a sorted manner

marks = []
mark1 = int(input("Enter: ")) # the reason we added int, because input returned string, in order to get actual sequence, it has to be integers. 
marks.append(mark1)
mark2 = int(input("Enter: "))
marks.append(mark2)
mark3 = int(input("Enter: "))
marks.append(mark3)
mark4 = int(input("Enter: "))
marks.append(mark4)
mark5 = int(input("Enter: "))
marks.append(mark5)
marks.sort()
print(marks) 