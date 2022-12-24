# # Lists - matlab just a list kuch chizon ki.
# grocery = ["Harpic", "golang", "vim bar", "deodrant", "khatam", 56] # This is a mixed list with strings as well as integer numbers
# print(grocery)
# print(grocery[1])  # prints the thing which is on the first index of grocery list i.e. golang
#
# numbers = [22, 12, 8, 6, 1] # This a pure numbers list
# print(numbers)
# print(numbers[2])
#
# # List Methods - sort [list mein numbers ko ascending order mein arrange karta hai], reverse [list mein numbers ko descending order mein arrange karta hai]
# numbers.sort()    # changes the orginal list of numbers # Implementation of sort method.
# print(numbers)
# numbers.reverse()  # changes the orginal list of numbers  # Implementation of reverse method.
# print(numbers)
#
# # Lists Slicing
# print(numbers[1:4])    # SLicing of list does not changes the orginal list.
# print(numbers[1:4:])   # udharpe default value 1 hai means no skip.
# print(numbers[1:4:2])  # Ab 1 ka gap hoga kyuki last mein 2 hai.
#
# # Negative Slicing
# print(numbers[::-1])  # This will just reverse the list items
# print(numbers[::-3])  # This will first reverse the list items and then from the reversed list it will take two two gaps and print the numbers
# #  It is advisable to use only -1 in negative slicing and nothing else
#
# # Few features
# print(len(numbers))  # 'numbers' list ki length print karta hai yaani list ke andar kitne elments hai woh.
# print(max(numbers))  # 'numbers' list mein joh maximum hai woh print kardeta hai.
# print(min(numbers))  # 'numbers' list mein joh minimum hai woh print kardeta hai.
#
# # append()
# numbers.append(7)   # 'numbers' list mein last mein 7 jod deta hai
# numbers.append(7)   # 'numbers' list mein last mein 7 jod deta hai
# numbers.append(7)   # 'numbers' list mein last mein 7 jod deta hai
# numbers.append(7)   # 'numbers' list mein last mein 7 jod deta hai
# #  Ab yeh append statement 4 baar likha hai iska matlab 4 baar 7 as a list item, list mein include ho jaayega.
# print(numbers)
#
# numbers.insert(2,44)  # Inserts 44 at index no. 2 in the list named 'numbers' and shifts the number which is already present there to the next index.
# print(numbers)
# numbers.remove(7)    # Removes one 7 from the numbers list
# print(numbers)
# numbers.pop()  # Removes the last element from the list
# print(numbers)
#
# numbers[1] = 98    # Inserts 98 at index no. 1 of 'numbers' list by replacing the one which is already there at that index.
# print(numbers)
#
# # Mutable - can change
# # Immutable - cannot change

# # Tuple - Immutable List (List items cannot be changed by any means or methods)
# tp = (1, 2, 3, 4)
# print(tp)

#  Interchange the values of two variables with each other if a = 1 & b = 2.
a = 1
b = 2
print(a,b)
# Interchanging method in other languages
# temp = a   # temp variable mein a ka value daalo
# a = b      # a variable mein b ka value daalo
# b = temp   # b variable mein temp ka value daalo
# print (a,b)
# Interchanging method in Python
a, b = b, a
print(a,b)

#  Python list functions and methods yeh sab aur padho from python documentation and Google...