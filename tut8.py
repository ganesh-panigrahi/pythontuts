# String Slicing

# print(mystr[2:5:2])
# 1. mystr variable ke andar joh bhi hai uske 2nd index se printing start karna hai.
# 2. mystr variable ke andar joh bhi hai uska 4 indexes ko hi print karna hai (5-1=1)
# 3. mystr variable ke andar ka joh 4 indexes ready hai print hone ke liye usme pehle letter ko chodkar 1 ke gap lekar letters (index values) ko print karna hai (2-1=1)

mystr = "Harry is a good Boy"
# print(len(mystr))
# print(mystr[0:5]) # String Slicing - Here, 0th index is including but 5th number is excluding
# print(mystr[78])  # Will give an error
# print(mystr[0:78])  # Will not give an error because there are characters from 0 to 18 index

# Extended String Slicing

print(mystr[:5])  # It will assume that there is 0
print(mystr[0:])  # It will take all from 0th index to end of the String
print(mystr[:])   # It will assume that first one is 0 and from the second blank it will assume that whole string from 0 to end needs to be printed
print(mystr[0:5:2])  # 0 se 4 tak ka joh string banta hai uska pehle letter ke baad ek ek letter chodkar print karo
print(mystr[0:5:])  # (khaali jagah pe 1 assume karta hai) 0 se 4 tak ka joh string banta hai uska koi letter na chodkar print karo
print(mystr[::]) # Will print the whole string




