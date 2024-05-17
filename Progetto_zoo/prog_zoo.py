class Animal:
    def __init__(self, name: str, species: str, age: int, 
                 height: float, width: float, preferred_habitat: str):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.healt = round(100*(1/age))
        self.area_animal = height * width
        self.fence = None


class Fence:
    def __init__(self, area: float, temperature: float, habitat: str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals: list[Animal] = []
         

class ZooKepper:
    def __init__(self, name: str, surname: str, id: int):
        self.name = name
        self.surname = surname
        self.id = id

    def add_animal(self, animal: Animal, fence: Fence):
        if animal.preferred_habitat == fence.habitat:
            if fence.area > animal.area_animal:
                fence.animals.append(animal)

    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals:
            fence.animals.remove(animal)

    def feed(self, animal: Animal):
        
        animal.healt += (animal.healt*0.01)
        animal.height += (animal.height*0.02)
        animal.width += (animal.width*0.02)

    def clean(self, fence: Fence) -> float:
        pass
        

class Zoo:
    def __init__(self, name: str):
        self.name = name
        self.fences = [Fence]
        self.zoo_keepers = [ZooKepper]
        self.animals = [Animal]

    def describe_zoo(self) -> None:
        print(f"Name: {self.name}")
        print(f"Zoo Keepers: \n")
        for a in self.zoo_keepers:
            print(f"Name: {a.name}, Surname: {a.surname}, Id: {a.id} \n")
        print("Fence: \n")
        for b in self.fences:
            print(f"Fence (area: {b.area}, temperature: {b.temperature}, habitat: {b.habitat})\n")
            print("Animals: \n")
            for c in b.animals:
                print(f"Animal (name: {c.name}, species: {c.species}, age: {c.age})\n")
            print("#" * 30)
            print("")

