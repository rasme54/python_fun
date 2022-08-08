# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

word = input("Type your word: ")
# print(len(word))
# print(word[0:len(word)])
# print(word[::-1])

if word == word[::-1]:
    print("This word is palindrome.")
else:
    print("This word isn\'t palindrome.")