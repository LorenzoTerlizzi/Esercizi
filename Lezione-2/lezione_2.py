# Lorenzo Terlizzi
# 17/04/2024

print("Hello World")

# 2-3. Personal Message: Use a variable to represent a person’s
# name, and print a message to that person.
# Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”

name: str = "Stefano"
message: str = f"Hello {name}, would you like to learn some Python today?"
print(message)

# 2-4. Name Cases: Use a variable to represent a person’s name,
# and then print that person’s name in lowercase,
# uppercase, and title case.

name: str = "Stefano"

print(name.lower())
print(name.upper())
print(name.title())

# 2-5. Famous Quote: Find a quote from a famous person you admire.
# Print the quote and the name of its author. Your output should
# look something like the following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake
# never tried anything new.”

print("Darwin una volta disse: \"Chi consente l'oppressione, condivide la colpa\"")

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent 
# the famous person’s name using a variable called famous_person. 
# Then compose your message and represent it with a new variable
# called message. Print your message. 

famous_person: str = "Darwin"
message: str = f"{famous_person} una volta disse: \"Chi consente l'oppressione, condivide la colpa\""
print(message)

# 2-8. File Extensions: Python has a removesuffix() method that works exactly like
# removeprefix(). Assign the value 'python_notes.txt' to a variable called filename.
# Then use the removesuffix() method to display the filename without the file
# extension, like some file browsers do.

filename: str = "python_notes.txt"
filename_without_extension = filename.removesuffix(".txt")

# 3-1. Names: Store the names of a few of your friends in a list called names.
# Print each person’s name by accessing each element in the list, one at a time.

names = ["Lorenzo", "Luca", "Andrea", "Filippo"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message
# should be the same, but each message should be personalized with the person’s name.

names: list = ["Lorenzo", "Luca", "Andrea", "Filippo"]
message: str = f"Ciao {names[0]}, come stai?"
print(message)
message: str = f"Ciao {names[1]}, come stai?"
print(message)
message: str = f"Ciao {names[2]}, come stai?"
print(message)
message: str = f"Ciao {names[3]}, come stai?"
print(message)

# 3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”

list_mezzi: list = ["Ducati", "Honda", "Aprilia"]
message: str = f"Mi piacerebbe avere una moto {list_mezzi[0]}"
print (message)
message: str = f"Mi piacerebbe avere una moto {list_mezzi[1]}"
print (message)
message: str = f"Mi piacerebbe avere una moto {list_mezzi[2]}"
print (message)

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

list_nomi: list = ["Angelina Jolie", "Leonardo Davinci", "Lorenzo"]
print(f"Ciao {list_nomi[0]}voui venire a cena?")
print(f"Ciao {list_nomi[1]}voui venire a cena?")
print(f"Ciao {list_nomi[2]}voui venire a cena?")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of your
# program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name
# of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in
# your list.

list_nomi: list = ["Angelina Jolie", "Leonardo Da Vinci", "Lorenzo"]
print(f"Ciao {list_nomi[0]} voui venire a cena?")
print(f"Ciao {list_nomi[1]} voui venire a cena?")
print(f"Ciao {list_nomi[2]} voui venire a cena?")
print("Purtroppo Leonardo Da Vinci non può venire")
list_nomi.remove("Leonardo Da Vinci")
list_nomi.append("Napoleone")
print(f"Ciao {list_nomi[0]} voui venire a cena?")
print(f"Ciao {list_nomi[1]} voui venire a cena?")
print(f"Ciao {list_nomi[2]} voui venire a cena?")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end
# of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

list_nomi: list = ["Angelina Jolie", "Leonardo Da Vinci", "Lorenzo"]
print(f"Ciao {list_nomi[0]} voui venire a cena?")
print(f"Ciao {list_nomi[1]} voui venire a cena?")
print(f"Ciao {list_nomi[2]} voui venire a cena?")
print("Purtroppo Leonardo Da Vinci non può venire")
list_nomi.remove("Leonardo Da Vinci")
list_nomi.append("Napoleone")
print(f"Ciao {list_nomi[0]} voui venire a cena?")
print(f"Ciao {list_nomi[1]} voui venire a cena?")
print(f"Ciao {list_nomi[2]} voui venire a cena?")
print(f"Ciao {list_nomi}, abbiamo trovato una tavola più grossa ")
list_nomi.insert(0, "Luca")
list_nomi.insert(2, "Alessio")
list_nomi.append("Andrea")
print(list_nomi)
print(f"Ciao {list_nomi[0]}, sei invitato alla cena nel nuovo posto")
print(f"Ciao {list_nomi[1]}, sei invitato alla cena nel nuovo posto")
print(f"Ciao {list_nomi[2]}, sei invitato alla cena nel nuovo posto")
print(f"Ciao {list_nomi[3]}, sei invitato alla cena nel nuovo posto")
print(f"Ciao {list_nomi[4]}, sei invitato alla cena nel nuovo posto")
print(f"Ciao {list_nomi[5]}, sei invitato alla cena nel nuovo posto")

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a message
# saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names 
# remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know
# they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list.
# Print your list to make sure you actually have an empty list at the end of your 
# program.

list_nomi: list = ["Angelina Jolie", "Leonardo Da Vinci", "Lorenzo"]
print(f"Ciao {list_nomi[0]} voui venire a cena?")
print(f"Ciao {list_nomi[1]} voui venire a cena?")
print(f"Ciao {list_nomi[2]} voui venire a cena?")
print("Purtroppo Leonardo Da Vinci non può venire")
list_nomi.remove("Leonardo Da Vinci")
list_nomi.append("Napoleone")
print(f"Ciao {list_nomi[0]} voui venire a cena?")
print(f"Ciao {list_nomi[1]} voui venire a cena?")
print(f"Ciao {list_nomi[2]} voui venire a cena?")
print(f"Ciao {list_nomi}, abbiamo trovato una tavola più grossa ")
list_nomi.insert(0, "Luca")
list_nomi.insert(2, "Alessio")
list_nomi.append("Andrea")
print(f"Ciao {list_nomi[0]}, sei invitato alla cena nel nuovo posto")
print(f"Ciao {list_nomi[1]}, sei invitato alla cena nel nuovo posto")
print(f"Ciao {list_nomi[2]}, sei invitato alla cena nel nuovo posto")
print(f"Ciao {list_nomi[3]}, sei invitato alla cena nel nuovo posto")
print(f"Ciao {list_nomi[4]}, sei invitato alla cena nel nuovo posto")
print(f"Ciao {list_nomi[5]}, sei invitato alla cena nel nuovo posto")

print(f"Buonasera {list_nomi}, purtroppo il ristorante ci ha comuniato di avere solo due posti disponibili ")
andrea = list_nomi.pop(5)
print(f"{andrea}, mi diaspiace non poterti più invitare")
lorenzo = list_nomi.pop(3)
print(f"{lorenzo}, mi diaspiace non poterti più invitare")
alessio = list_nomi.pop(2)
print(f"{alessio}, mi diaspiace non poterti più invitare")
luca = list_nomi.pop(0)
print(f"{luca}, mi diaspiace non poterti più invitare")
print(f"{list_nomi[0]} ci vediamo alla cena")
print(f"{list_nomi[1]} ci vediamo alla cena")
del list_nomi[0]
del list_nomi[0]
print(list_nomi)

# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly; 
# just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the 
# actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse-alphabetical order without changing 
# the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse()  to change the order of your list. Print the list to show that its 
# order has changed.
# • Use reverse() to change the order of your list again. Print the list to show it’s 
# back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the 
# list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.

list_viaggi: list = ["Londra", "Los Angeles", "Dubai", "Australia"]
print(list_viaggi)
print(sorted(list_viaggi))
print(list_viaggi)
print(sorted(list_viaggi, reverse = True))
print(list_viaggi)
list_viaggi.reverse()
print(list_viaggi)
list_viaggi.reverse()
print(list_viaggi)
list_viaggi.sort()
print(list_viaggi)
list_viaggi.sort(reverse = True)
print(list_viaggi)

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() 
# to print a message indicating the number of people you’re inviting to dinner.

list_nomi: list = ["Angelina Jolie", "Leonardo Da Vinci", "Lorenzo"]
len_lista = len(list_nomi)
print(len_lista)

# 3-10. Every Function: Think of things you could store in a list. For example, you 
# could make a list of mountains, rivers, countries, cities, languages, or anything 
# else you’d like. Write a program that creates a list containing these items and 
# then uses each function introduced in this chapter at least once.

lista: list = ["Laghi", "Cielo", "Mare"]

# 6-1. Person: Use a dictionary to store information about a person you know. Store 
# their first name, last name, age, and the city in which they live. You should have
# keys such as first_name, last_name, age, and city. Print each piece of information
# stored in your dictionary.

informazioni: dict = {"nome": "Luca", "cognome": "Scarsella", "età": 19, "città": "Milano"}
print(informazioni)

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print each
# person’s name and their favorite number. For even more fun, poll a few friends
# and get some actual data for your program.

numeri_preferiti: dict = {"Lorenzo": 20, "Luca": 12, "Leonardo": 24, "Stefano": 34, "Federico": 7}
print("il numero preferito di Lorenzo è: ", numeri_preferiti["Lorenzo"])
print("il numero preferito di Luca è: ", numeri_preferiti["Luca"])
print("il numero preferito di Leonardo è: ", numeri_preferiti["Leonardo"])
print("il numero preferito di Stefano è: ", numeri_preferiti["Stefano"])
print("il numero preferito di Federico è: ", numeri_preferiti["Federico"])

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. You might print the
# word followed by a colon and then its meaning, or print the word on one line and
# then print its meaning indented on a second line. Use the newline character (\n)
# to insert a blank line between each word-meaning pair in your output.

parole: dict = {
                
                "variabile": "nome associato a un valore",
                "cicli": "iterazione ripetuta di istruzioni",
                "funzione": "pezzo di codice che esegue una determinata istruzione"
                }
print("Variabile", parole["variabile"])
print("\n")