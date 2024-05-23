# Lorenzo Terlizzi
# 23/05/2024

# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes:
# a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information,
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant (self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant (self):
        print("The restaurant is open")
    
restaurant_1: Restaurant = Restaurant("OYO", "Giapponese")
print(restaurant_1.restaurant_name)
print(restaurant_1.cuisine_type)
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class,
# and call describe_restaurant() for each instance.
restaurant_1: Restaurant = Restaurant("OYO", "Giapponese")
restaurant_2: Restaurant = Restaurant("Bella Napoli", "Pizzeria")
restaurant_3: Restaurant = Restaurant("Burger King", "Fast Food")
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

#9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes
# that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information.
# Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.
class User:
    def __init__(self, first_name: str, last_name:str, age: int, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        print(self.first_name, self.last_name, self.age, self.gender)
    
    def greet_user(self):
        print(f"Hi {self.first_name}, how are you?")

user_1: User = User("Giacomo", "Rossi", 32, "Male")
user_2: User = User("Ilenia", "Verdi", 28, "Female")
user_3: User = User("Luca", "Bianchi", 45, "Male")

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()

# 9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class. Print the number of customers the restaurant has served,
# and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers
# that have been served. Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
# Call this method with any number you like that could represent how many customers were served in, say, a day of business. 
class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant (self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant (self):
        print("The restaurant is open")
    
    def set_number_served(self, number_served: int):
        self.number_served = number_served

    def increment_number_served(self, number_increment: int):
        self.number_increment = number_increment
        self.number_served += number_increment

restaurant: Restaurant = Restaurant("OYO", "Giapponese")
print(restaurant.number_served)
restaurant.set_number_served(20)
print(restaurant.set_number_served)
restaurant.increment_number_served(10)
print(restaurant.increment_number_served)

# 9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3. Write a method called
# increment_login_attempts() that increments the value of login_attempts by 1. Write another method called reset_login_attempts()
# that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times.
# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
# Print login_attempts again to make sure it was reset to 0.
class User:
    def __init__(self, first_name: str, last_name:str, age: int, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        print(self.first_name, self.last_name, self.age, self.gender)
    
    def greet_user(self):
        print(f"Hi {self.first_name}, how are you?")

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits
# from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. Either version of the class will work;
# just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method. 

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name: str, cuisine_type: str):
        Restaurant.__init__(self, restaurant_name, cuisine_type)
        self.flavors: list = ["Cioccolato", "Vaniglia", "Stracciatella"]
    
    def displays_flavors(self):
        for a in self.flavors:
            print(a)
iceCream: IceCreamStand = IceCreamStand("Name", "Type")
iceCream.displays_flavors()

# 9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote
# in Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post",
# "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges.
# Create an instance of Admin, and call your method. 
class Admin(User):
    def __init__(self, privileges, first_name: str, last_name:str, age: int, gender: str):
        User.__init__(self, first_name, last_name, age, gender)
        self.privileges = privileges
    
    def show_privileges(self):
        print(self.privileges)
admin: Admin = Admin("can add post", "Mario", "Rossi", 32, "Male")
admin.show_privileges()

# 9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings
# as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in
# the Admin class. Create a new instance of Admin and use your method to show its privileges.
class Privileges:
    def __init__(self, privileges: list):
        self.privileges = privileges

    def show_privileges(self):
        for a in self.privileges:
            print(a)  


class Admin2(User):
    def __init__(self, privileges: Privileges, first_name: str, last_name:str, age: int, gender: str):
        User.__init__(self, first_name, last_name, age, gender)
        self.privileges = privileges
    
    def show_privileges(self):
        self.privileges.show_privileges()

privileges: Privileges = Privileges(["can add post", "can delete post", "can ban user"])
admin1: Admin2 = Admin2(privileges, "Mario", "Rossi", 32, "Male")
admin1.show_privileges()

# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class called
# upgrade_battery(). This method should check the battery size and set the capacity to 65 if it isn’t already. Make an electric
# car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery.
# You should see an increase in the car’s range.

# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant.
# Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.
####


# 9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module.
# Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

# 9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. 
# In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

# 9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that
# prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
import random
class Die:
    def __init__(self):
        self.sides: int = 6
    
    def roll_die(self):
        self.num: int = random.randint(1, 7)
        print(self.num)
        
# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers or letters from
# the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.

# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or
# tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many
# times the loop had to run to give you a winning ticket.






