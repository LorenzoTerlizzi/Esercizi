# Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). 
# Handle ValueError if the input is negative by returning an informative message.

def safe_sqrt(number):
    import math
    num = math.sqrt(number)
    if number < 0:
        try: 
            num = math.sqrt(number)
        except:
            {f"Impossible calculates the square root of  a negative number {number}"}
    print(num)

# Password Validation: Write a function validate_password(password) that checks if a password meets certain criteria 
# (i.e., minimum length of 20 characters, at least three uppercase characters, and at least four special characters).  
# Raise a custom exception (e.g., InvalidPasswordError) for invalid passwords.
class InvalidPasswordError(Exception):
    pass

def validate_password(password):
    a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    b = ["_", "-", ".", ";", ":", ",", "!", "?", "@", "#"]
    conta = 0
    conta1= 0
    for i in password:
        if i in a:
            conta += 1
        if i in b:
            conta1 += 1
    if len(password) < 20:
        raise InvalidPasswordError("Password is short")
    
    try:
        return "password is valid"
    except InvalidPasswordError as error:
        return error

# Context Managers for File Handling: Use the with statement and context managers to open and close a file. 
# Handle potential IOError within the with block for clean resource management.

try:
    with open("file.py") as file:
        file.read()
except IOError as error:
    print("block for clean resource management")
finally:
    file.close()

# Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa implementing methods to add a new date,
# delete a given date, modify a date, and perform a query on a given date is required.  A query on a given date allows for 
# retrieving a given new date. Note that a date is an object for your database; it must be instantiated from a string.

class Database:
    def __init__(self):
        self.dates = {} 
        
    def add_date(self, date):
        day, month, year = date.split('.')
        self.dates[date] = {'day': day, 'month': month, 'year': year}
    
    def remove_date(self, date):
        if date in self.dates:
            self.dates.remove(date)
        else:
            print("Date not found")
    
    def modify_date(self, date):
        if date in self.dates:
            day, month, year = date.split('.')
            self.dates[date] = {'day': day, 'month': month, 'year': year}
        else:
            print("Date not found")

    def query_date(self, date):
        if date in self.dates:
            return self.dates[date]
        
# An interactive calculator: It is required to develop an interactive calculator with at least 10 test cases using UnitTest trying 
# to (possibly) cover all execution paths! User input is assumed to be a formula that consists of a number, an operator 
# (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), 
# and check whether the resulting list is valid:
#   If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
#   Try to convert the first and third inputs to a float (like so: float_value = float(str_value)). Catch any ValueError 
#   that occurs, and instead raise a FormulaError.
#   If the second input is not '+' or '-', again raise a FormulaError.
#   If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, 
#   and so on, until the user enters quit.
