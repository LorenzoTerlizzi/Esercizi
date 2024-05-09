class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

alice: Person = Person("Alice", 45)
bob: Person = Person("Bob", 36)

# Es. 1
print(bob.age)
person = [alice, bob]
for p in person:
    print(p.age)


# Es. 2
if alice.age > bob.age:
    print(alice.age)
else:
    print(bob.age)

