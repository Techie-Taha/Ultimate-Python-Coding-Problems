# what will be the length of following set S

s = set()
s.add(20)
print(s)
s.add(20.0)
print(s)
s.add("20")
print(s)
# in the terminal we see {'20', 20} so it's considering 20.0 as 20, and removed the duplicate.
x = len(s)
print(x) # we get 2 because now we only have a string "20" and 20