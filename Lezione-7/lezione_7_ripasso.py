# Lorenzo Terlizzi
# 16/05/2024

# Write a function to find all numbers divisible by 7, not a multiple of 5, between 2000 and 3200 (both included).
# The numbers should be stored in a list and returned as output.
def number_divisible_7():
    numero: list = [lista for lista in range(2000, 3201)]
    num: list = []
    for a in numero:
        if a % 7 == 0 and a % 5 != 0:
            num.append(a)
    return num
print(number_divisible_7())

# Write a function to calculate the factorial of a number given as input. The number should be returned as output.
# For example:
# Input: 8
# Output: 40320

def fattoriale(n = int):
   
    f: int = 1
    for i in range(1, n+1):
        f = f * i
    return f
n = 8
print(fattoriale(n))
    
# Use the function implemented in Exercise 2 to compute all factorial numbers of a list of numbers.
# The list is given as input to the function. All factorials should be returned as output.
# For example:
# Input: [2, 5, 8, 10]
# Output: [2, 120, 40320, 3628800]
def Es_3(num_list: list):
    num_fatt: list = []
    for n in num_list:
        num_fatt.append(fattoriale(n))
    return num_fatt
num_list: list = [3, 4, 5, 6]
print(Es_3(num_list))

# Given an integer n as input, write a function to generate a dictionary that contains (i, i*i) as (key, value)
# pairs such that i is an integer between 1 and n (both included). The function should return the dictionary as output.
# For example:
# Input: 8
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
def Es_4(num: int):
    num_dict: dict = {}
    for a in range(1, num + 1):
        b = a * a
        num_dict[a] = b
    return num_dict
num = 8
print(Es_4(num))

# Write a function that accepts a string with a comma-separated sequence of words
# as input and prints the words as a comma-separated sequence after sorting them alphabetically.
# For example:
# Input: without,hello,bag,world
# Output: bag,hello,without,world
def Es_5(sequenza:  str):
    a = sequenza.replace(","," ")
    x =  a.split()
    x.sort()
    delim = ","
    frase = delim.join(x)
    return frase
         
sequenza: str = "without,hello,bag,world"
print(Es_5(sequenza))

# Write a function that accepts a list of sentences (string) as input and returns each line as output after capitalising all sentence characters.
#  For example:
# Input: Practice makes perfect
# Output: PRACTICE MAKES PERFECT

def Es_6(sequenza:  str):
    
    return sequenza.upper()
         
sequenza: str = "Practice makes perfect"
print(Es_6(sequenza))