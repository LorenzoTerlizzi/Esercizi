class Zoo:
    def __init__(self, fences: str, zoo_keepers: str):
        self.fences = fences
        self.zoo_keepers = zoo_keepers
    
class Animal:
    def __init__(self, name: str, species: str, age: int, 
                 height: float, width: float, preferred_habitat: str, healt: float, area_animal: float):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.healt = round(100*(1/age), 3)
        self.area_animal = height * width


class Fence:
    def __init__(self, area: float, temperature: float, habitat: str, lista: list):
        self.area = area
        self.tempareture = temperature
        self.habitat = habitat
        self.lista = lista

class ZooKepper:
    def __init__(self, name: str, surname: str, id: int):
        self.name = name
        self.surname = surname
        self.id = id

    def add_animal(self, animal: Animal, fence: Fence):
        self.animal = [Animal]
        if animal.preferred_habitat == fence.habitat:
            if fence.area > animal.area_animal:
                fence.append(animal)

    def remove_animal(self, animal: Animal, fence: Fence):
        self.animal = [Animal]
        fence.remove(animal)

    def feed(self, animal: Animal):
        self.animal = [Animal]
        healt = healt + (healt/100)
        height = height + ((height*2)/100)
        width = width + + ((width*2)/100)

    def clean(self, fence: Fence) -> float:
        self.fence = Fence
        



