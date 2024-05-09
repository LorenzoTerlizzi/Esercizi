class Student:
    def __init__(self, name: str, studyProgram: str, age: int, gender: int):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender

    def printInfo(self):
        print(self.name, self.studyProgram, self.age, self.gender)

student1: Student = Student("Lorenzo", "Python", 19, "Male")
student2: Student = Student("Andrea", "Python", 20, "Male")
student3: Student = Student("Alessio", "Python", 19, "Male")


student1.printInfo()
student2.printInfo()
student3.printInfo()


# Esercizio 3
class Animal:
    def __init__(self, name: str, legs: int):
        self.name = name
        self.legs = legs

    def getLegs(self):
         return self.legs
    
    def setLegs(self, legs: int):
            self.legs = legs

    
    def printInfo(self):
         print(self.name, self.legs)

animal1: Animal = Animal("lion", 3)
animal2: Animal = Animal("fish", 0)

animal1.printInfo()
animal2.printInfo()

animal1.legs = 4

print(animal1.getLegs())

animal2.setLegs(2)
print(animal2.legs)

animal1.printInfo()
animal2.printInfo()


class Food:
     def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description

meat: Food = Food("steak", 15.99, "pig's meat")
fish: Food = Food("fish", 19.99, "tuna's fish")
fruits: Food = Food("apple", 1.50, "red's apple")

class Menu:
    def __init__(self, lista: list = []):
        self.lista = lista
    
    def addFood(self, food: Food ):
        self.lista.append(food)
    def removeFood(self, food: Food):
        self.lista.remove(food)
    def printPrice(self):
        for i in self.lista:
            print(i.name, i.price, i.description)

    def getAveragePrice(self):
        conta = 0
        average = 0
        for b in self.lista:
            conta += 1
            average += b.price
        average /= conta
        return print(f"the average prise is: {average}")

        
menu: Menu = Menu()
menu.addFood(meat)
menu.addFood(fish)
menu.addFood(fruits)
menu.printPrice()
print(menu.getAveragePrice())