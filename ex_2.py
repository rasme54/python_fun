# Ask the user for a number. Depending on whether the number 
# is even or odd, print out an appropriate message to the user. Hint: 
# how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) 
# and one number to divide by (check). If check divides evenly 
# into num, tell that to the user. If not, print a different appropriate message.

num = input("Type your number: ")
check = input("Type number to divide by: ")

#even - odd - check
if int(num) % 4 == 0:
    print("Number " ,num , "is even. Also it's a multiple of 4.")
elif int(num) % 2 == 0:
    print("Number " ,num , "is even.")
else:
    print("Number " ,num , "is  odd.")

#divide check
rest = int(num) % int(check)
if int(num) % int(check) == 0:
    print("No rest from this divining.")
else:
    print("The rest is ", rest, ".")