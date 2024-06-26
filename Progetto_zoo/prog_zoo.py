# Lorenzo Terlizzi

"""
Sistema di gestione dello zoo virtuale

Classi:

1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat, health che è uguale a round(100 * (1 / age), 3).

3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. I recinti possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.

4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. I guardiani dello zoo hanno un name, un surname, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.

Funzionalità:

1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.

2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width) vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.

5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 
"""

class Animal:
    def __init__(self, name_animal: str, species: str, age: int, 
                 height: float, width: float, preferred_habitat: str):
        self.name_animal = name_animal
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100*(1/age))
        self.fence = None
        

    def area_animal(self) -> None:
        area_a: float = self.width * self.height
        return area_a

class Fence:
    def __init__(self, area: float, temperature: float, habitat: str):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals: list[Animal] = []

    def area_libera(self) -> None:
        area_l: int = self.area
        for animal in self.animals:
            area_l -= animal.area_animal()
        return area_l
         

class ZooKeeper:
    def __init__(self, name: str, surname: str, id: int):
        self.name = name
        self.surname = surname
        self.id = id
        self.fences: list[Fence] = []

    def add_animal(self, animal: Animal, fence: Fence):
        if animal.preferred_habitat == fence.habitat and fence.area_libera() >= animal.area_animal():
            fence.animals.append(animal)
            animal.fence = fence

    def remove_animal(self, animal: Animal, fence: Fence):
        if animal in fence.animals:
            fence.animals.remove(animal)
            animal.fence = None
        else:
            print("Animal is not in thi fence")

    def feed(self, animal: Animal):
        if animal.fence.area_l() >= animal.area_animal() * 0.02:
            animal.health += (animal.health*0.01)
            animal.height += (animal.height*0.02)
            animal.width += (animal.width*0.02)
        else:
            print("Not enough space in fence")

    def clean(self, fence: Fence, animal: Animal) -> float:
        if fence.area_l > 0:
            time_clean: float = animal.area_animal / fence.area_libera
        else:
            time_clean = animal.area_animal
        return time_clean
        

class Zoo:
    def __init__(self, name: str):
        self.name = name
        self.fences = [Fence]
        self.zoo_keepers = [ZooKeeper]

    def describe_zoo(self) -> None:
        print(f"Name: {self.name}")
        print(f"Zoo Keepers: \n")
        for a in self.zoo_keepers:
            print(f"Name: {a.name}, Surname: {a.surname}, Id: {a.id} \n")
        print("Fence: \n")
        for b in self.fences:
            print(f"Fence (area: {b.area}, temperature: {b.temperature}, habitat: {b.habitat})\n")
            print("with Animals: \n")
            for c in b.animals:
                print(f"Animal (name: {c.name_animal}, species: {c.species}, age: {c.age})\n")
            print("#" * 30)
            print("")



