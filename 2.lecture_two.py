str = 'apna college'

str1 = 'apna'
len1 = len(str1)
print(len1)

str2 = 'college'
final_str = str1 + " " +str2
print(final_str)

print(len(final_str))


# Start indexing

"""
Apna_Colle g e
012345678910 11
"""

# Start Slicing
# str[strting_index:ending_index] --> ending index is not included
print(str[0:4]) # apna

print(str[5:12]) # 5 to last index of string
print(str[5:len(str)]) # 5 to last index of string
print(str[5:]) # 5 to last index of string --> [5:len(str)]

print(str[:4]) # start to before index 4 or till 4th index of string --> [0:4]

# Slicing with negative index
"""
 A  p  p  l  e
-5 -4 -3 -2 -1
"""
negStr = "Apple"
print(negStr[-3:-1])   # pl
print(negStr[-5:-2])   # App


# String Function
str = "i am studying python from Apna College. This is the $ symbol, using like $99.99"
print(str.endswith("ege"))      # True or False
print(str.capitalize())         # Make upper the first letter.
print(str.replace("o", "a"))    # Replace a character or letter with another of a string.
print(str.replace("python", "javascript"))
print('Find character with st indexing point:', str.find("st"))   # Return the first index number of str. --> 2, if it is not available then i'll be return -1
print('Count a:', str.count("a"))   # Count How many exact character or letter has in this string?

print('Dollar count:', str.count("$"))
userName = input("Your first name: ")
print('Your name is:', userName, 'and name length is:', len(userName))
