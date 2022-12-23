# # Lists - matlab just a list kuch chizon ki.
#
# grocery = ["Harpic", "golang", "vim bar", "deodrant", "khatam", 56] # This is a mixed list with strings as well as integer numbers
# print(grocery)
# print(grocery[1])  # prints the thing which is on the first index of grocery list i.e. golang
#
numbers = [22, 12, 8, 6, 1] # This a pure numbers list
print(numbers)
# print(numbers[2])
#
# # List Methods - sort [list mein numbers ko ascending order mein arrange karta hai], reverse [list mein numbers ko descending order mein arrange karta hai]
#
# numbers.sort()    # changes the orginal list of numbers # Implementation of sort method.
# print(numbers)
# numbers.reverse()  # changes the orginal list of numbers  # Implementation of reverse method.
# print(numbers)

# Lists Slicing

print(numbers[1:4])    # SLicing of list does not changes the orginal list.
print(numbers[1:4:])   # udharpe default value 1 hai means no skip
print(numbers[1:4:2])  # Ab 1 ka gap hoga kyuki last mein 2 hai.




