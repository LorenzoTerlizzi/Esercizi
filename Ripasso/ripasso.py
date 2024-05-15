nome_variabile: int = 10
nome_variabile: float = 10.0
nome_variabile: bool = False
nome_variabile: str = "Ciao"

nome_variabile: float = 10.0
nome_variabile = nome_variabile + 5.5
nome_variabile += 5.5

variabile_float: float = 0.0
variabile_float = 5.5 + 10.0

variabile_int: int = 0
variabile_int = 10.0 + 5.5

print(nome_variabile)

lunghezza_lista: int = 7

import math
punto_di_mezzo: int = 7 / 2
print(math.ceil(punto_di_mezzo))

var_1: bool = True
var_2: bool = False

print(var_1 and var_2)
print(var_1 or var_2)
print(not var_1)

x: int = - 1000

i: int = 0

a: bool = True
b: bool = False

lista: list = [1, 2, 3, 5, 6]

for numero in lista:
    print(f"x^2: {numero**2}") 

for numero in range(len(lista)):

    print(f"x^2: {lista[numero]**2}") 

contatore: int = 0
while contatore < len(lista):
    print(f"x^2: {lista[contatore]**2}")
    contatore += 1


if a and b:
    print(f"Sono nel primo if")

elif a or b:
    print(f"Sono nel primo elif")

elif not(a and b):
    print(f"Sono nell'else")


class Persona:
    def __init__(self):
        pass

anagrafe: dict = {
    "persona_1": "Flavio",
    "persona_2": "Marco",
    "persona_3": "Leonardo"
}

print(anagrafe["persona_1"])

anagrafe["persona_2"] = "Bardh"


anagrafe: dict = {
    "persona_1": "Flavio",
    "persona_2": "Marco",
    "persona_3": "Leonardo"
}

key: str = "persona_100"

voti: list = [{"nome": "Flavio", "voto": 18}, {"nome": "Flavio","voto": 25}, {"nome": "Marco", "voto": 26}]
aggr: dict = {}

aggre: dict = {
    "key_1": {
        "key_1_1": {
            "floor": 0
        }
    }
}
print(aggre["key_1"]["key_1_1"]["floor"])

for dizionario in voti:

    nome: str = dizionario["nome"]
    voto: int = dizionario["voto"]

    if nome in aggr:

        aggr[nome].append(voto)
    else:
        aggr[nome] = [voto]
print(aggr)


for key, value in aggr.items():
    print(key, value)


for value in aggr.values():
    print(value)

for key in aggr.keys():
    print(key)