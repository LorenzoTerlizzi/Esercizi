# Lorenzo Terlizzi
# 23/04/2024

# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what
# you are learning about in this chapter. Call the function, and make sure the message displays correctly.

def display_message():
    a: str = "you are learning"
    print(a)
display_message()


# 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The
# function should print a message, such as "One of my favorite books is Alice in Wonderland".
# Call the function, making sure to include a book title as an argument in the function call.

def favorite_book(title):
    print(f"One of my favorite books is {title}")
favorite_book("harry potter")

# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that
# should be printed on the shirt. The function should print a sentence summarizing the size of the
# shirt and the message printed on it. Call the function once using positional arguments to make a shirt.
# Call the function a second time using keyword arguments.
def make_shirt(size, text_message):
    print(f"the size is {size}, the message on the shirt is {text_message}")
make_shirt("m", "wow")


# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message
# that reads I love Python. Make a large shirt and a medium shirt with the default message,
# and a shirt of any size with a different message.
def make_shirt(size: str = "L", text_message: str = "I love python"):
    print(f"the size is {size}, the message on the shirt is {text_message}")
make_shirt("m", "I love python")


# 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the
# country a default value. Call your function for three different cities, at least one of which is not
# in the default country.
def describe_city(name_city, country):
    country: str = "Italia"
    print(f"{name_city} is in {country}")
describe_city("roma", "")
describe_city("milano", "")
describe_city("napoli", "")


# 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted like this: "Santiago, Chile". Call your function
# with at least three city-country pairs, and print the values that are returned.

def city_country(name_city, country):
    a: str = f"{name_city}, {country}"
    return a
print(city_country("milano", "italia"))


# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title, and it should return a dictionary
# containing these two pieces of information. Use the function to make three dictionaries representing
# different albums. Print each return value to show that the  dictionaries are storing the album
# information correctly. Use None to add an optional parameter to make_album() that allows you to store
# the number of songs on an album. If the calling line includes a value for the number of songs,
# add that value to the album’s dictionary. Make at least one new function call that includes the
# number of songs on an album.

def make_album(name_artist, title) -> dict:
    album: dict = {"name artist" : name_artist, "album" : title}
    return album
print(make_album("bon jovi", "always"))



# 8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function
# called show_messages(), which prints each text message.

def show_messages(text_message: list =["ciao", "hello", "hola"]):
    for t in text_message:
        print(t)
show_messages()

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called
# send_messages() that prints each text message and moves each message to a new list called sent_messages
# as it’s printed. After calling the function, print both of your lists to make sure the messages were moved
# correctly.

def send_messages(text_message: list =["ciao", "hello", "hola"]):
    sent_messages: list = [] 
    for t in text_message:
        print(t)
        sent_messages.append(t)
        text_message.remove(t)    
    return sent_messages
send_messages()


# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, 
# and it should print a summary of the sandwich that’s being ordered.
# Call the function three times, using a different number of arguments each time.

def sandwich(*args):
    print("Elenco ingredienti panino: ")
    for i in args:
        print(i)


# 8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last
# names and three other key-value pairs that describe you. All the values must be passed to the function 
# as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"

def build_profiler(first_name, last_name, age, color_hair, weight) -> str:
    message: str = f"{first_name} {last_name}, age:{age}, color hair: {color_hair}, weight:{weight}"
    return message
print(build_profiler("lorenzo", "ultimo", 18, "black", 70))

# 8-14. Cars: Write a function that stores information about a car in a dictionary. The function should
# always receive a manufacturer and a model name. It should then accept an arbitrary number of
# keyword arguments. Call the function with the required information and two other name-value pairs,
# such as a color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True) Print the dictionary that’s returned
# to make sure all the information was stored correctly. 

def make_car(manufacturer, model, color) -> dict:
    car = {"manufacturer" : manufacturer,
           "model" : model,
           "color" : color}
    return car
print(make_car("manufacturer", "model", "colol"))

# 8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called
# printing_functions.py. Write an import statement at the top of printing_models.py, and modify
# the file to use the imported functions.




# Questa funzione impementa il bubble sort
def naive_bubblue_sort(A: list = [4, 3, 7, 8, 2, 9, 1, 5]):
    for i in range(len(A)):
        for j in range(len(A) -1):
            if A[j] > A[j+1]:
                temp: int = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    return A
print(naive_bubblue_sort())


import time
mylist: list = [i for i in range(1, 10001)]
def flag_bubblue_sort_2(A: list = [4, 3, 7, 8, 2, 9, 1, 5]):
    for i in range(len(A)):
        swap_flag = False
        for j in range(len(A) -1):
            if A[j] > A[j+1]:
                swap_flag = True
                temp: int = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
        if swap_flag is False:
            return A
    return A
start: float = time.time()
print(flag_bubblue_sort_2(mylist))
print(time.time()- start)

import time
def improved_bubblue_sort(A: list = [4, 3, 7, 8, 2, 9, 1, 5]):
    for i in range(len(A)):
        for j in range(len(A) -i -1):
            if A[j] > A[j+1]:
                temp: int = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    return A
start: float = time.time()
print(improved_bubblue_sort())
print(time.time()- start)
