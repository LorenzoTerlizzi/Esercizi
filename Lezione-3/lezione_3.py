# Lorenzo Terlizzi
# 19/04/2024

# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza, instead
# of printing just the name of the pizza. For each pizza, you should have one line
# of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states how
# much you like pizza. The output should consist of three or more lines about the
# kinds of pizza you like and then an additional sentence, such as I really love pizza!

pizza: list = ["margherita", "diavola", "patate e salsiccia"]
for p in pizza:
    print("I like pizza", p)
print("Ireally like pizza" )

# 4-2. Animals: Think of at least three different animals that have a common
# characteristic. Store the names of these animals in a list, and then use a for
# loop to print out the name of each animal.
# • Modify your program to print a statement about each animal, such as A dog would
# make a great pet.
# • Add a line at the end of your program, stating what these animals have in common.
# You could print a sentence, such as Any of these animals would make a great pet!

animals: list = ["orso", "Lupo", "Leone"]
for a in animals:
    print("come animale ho un", a)
print("Questi animali hanno tutti gli artigli")

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for number in range(21):
    print(number)

# 4-4. One Million: Make a list of the numbers from one to one million, and then use
# a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing CTRL-C or by closing the output window.)
num: list = range(1, 1000001)
#for number in num:
    #print(number)

# 4-5. Summing a Million: Make a list of the numbers from one to one million, and
# then use min() and max() to make sure your list actually starts at one and ends
# at one million. Also, use the sum() function to see how quickly Python can add a
# million numbers.
 
num: list = range(1, 1000001)
print(min(num))
print(max(num))
print(sum(num))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of
# the odd numbers from 1 to 20. Use a for loop to print each number.

for a in range(1, 21, 3 ):
    print(a)

# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print
# the numbers in your list.
num: list = range(3, 31, 3)
for n in num:
    print(n)

# 4-8. Cubes: A number raised to the third power is called a cube. For example, the
# cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is,
# the cube of each integer from 1 through 10), and use a for loop to print out the
# value of each cube.
num: list = range(1, 11)
for n in num:
    a: int = n**3
    print(a)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first
# 10 cubes.
num: list = [num **3 for num in range(1, 11)]
print(num)


# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines
# to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to print
# the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Then use a slice to 
# print three items from the middle of the list.
# • Print the message The last three items in the list are:. Then use a slice to print 
# the last three items in the list.
num: list = [num for num in range(1, 11)]
print("The first three items in the list are: ")
for item in num[:3]:
    #print("The first three items in the list are: ")
    print(item)
print("The first three items in the list are: ")
for item in num[4:7]:
    print(item)
print("The first three items in the list are: ")
for item in num[7:]:
    print (item)

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy
# of the list of pizzas, and call it friend_pizzas. Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists. Print the message My favorite pizzas are:,
# and then use a for loop to print the first list. Print the message My friend’s
# favorite pizzas are:, and then use a for loop to print the second list. Make sure
# each new pizza is stored in the appropriate list.
pizza: list = ["margherita", "diavola", "patate e salsiccia"]
friend_pizzas: list = pizza.copy()
pizza.append("marinara")
friend_pizzas.append("bianca")
print(pizza, friend_pizzas)
z: str= ""
y: str= ""
for p in pizza:
    z = z+ ", "+p
print(f"My favorite pizzas are: {z}")
for f in friend_pizzas:
    y = y+ ", "+f
print(f"My friend’s favorite pizzas are: {y}")


# 4-12. More Loops: All versions of foods.py in this section have avoided using for 
# loops when printing, to save space. Choose a version of foods.py, and write two
# for loops to print each list of foods.


#5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
car = input("Inserisci un'auto:")
if car == "subaru":
    print(car == "subaru")
elif car == "audi":
    print (car == "audi")
else:
    print(False)




# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to 10. If you want to try more comparisons, write more tests and add them
# to conditional_tests.py. Have at least one True and one False result for each of
# the following:
# • Tests for equality and inequality with strings
# • Tests using the lower() method
# • Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list



