# Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only 
# the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you 
# can’t figure this out at this point - we’ll get to it soon)
import random

c = []

for i in b:
    if i in a and i in b:
        c.append(i)
print(c)

#extras:
rang = input("Type list\'s range: ")
num_range = input("Type numbers range: ")

d = []
e = []

for i in range(1, int(rang)):
    d.append(random.randint(1, int(num_range)))
    e.append(random.randint(1, int(num_range)))
print(d)
print(e)