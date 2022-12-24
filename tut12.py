# Set
s = set()      # Declaration of a set/ Made a blank set of 's' name.
print(type(s))
s.add(1)      # Method to add elements in a set.
s.add(1)     # Here, we've again added 1, but it will not be printed because, s is a set (holds only unique elements) not a list (holds all elements put in it)
print(s)
s.add(1)
print(s)


# l = [1, 2, 3, 4]   # This is a list stored in a variable 'l'
# s_from_list = set(l)  # Here, we're converting the list in 'l' to a set & storing it in 's_from_list' variable
# print(s_from_list)
# print(type(s_from_list))

