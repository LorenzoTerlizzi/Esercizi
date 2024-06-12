# 2. RENDERING GRAFICO
# Si vuole sviluppare un sistema in Python per gestire il rendering di diverse forme geometriche. Il sistema dovrà supportare 
# almeno tre tipi di forme: quadrati, rettangoli, e triangoli rettangoli.

# Definire la classe astratta Forma che sarà utilizzata per definire l'attributo corrispondente al nome della forma e le 
# funzionalità base di ogni forma, come i metodi astratti getArea() per calcolare l'area e render() per disegnare su schermo la forma.

# Definire la classe Quadrato che estende la classe Forma e aggiunge specifiche circa la lunghezza di un suo lato.
# Il costruttore della classe deve ricevere come argomento solo il lato del quadrato, ed impostare il nome della forma su "Quadrato".
# Il metodo getArea() deve calcolare l'area del quadrato.
# Il metodo render() deve stamapre su schermo un quadrato avente lato pari al valore passato nel costruttore. 
# Il quadrato da stampare deve essere un quadrato vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. 
# (Vedi Esempio di output)

# Definire la classe Rettangolo che estende la classe Forma e aggiunge specifiche circa la lunghezza della sua base e della sua altezza.
# Il costruttore della classe deve ricevere come argomento solo la base e l'altezza del rettangolo, ed impostare il nome 
# della forma su "Rettangolo".
# Il metodo getArea() deve calcolare l'area del rettangolo.
# Il metodo render() deve stampare su schermo un rettangolo avente base ed altezza pari ai valori passati nel costruttore. 
# Il rettangolo da stampare deve essere un rettangolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. (Vedi Esempio di output)

# Definire la classe Triangolo che estende la classe Forma e aggiunge specifiche circa la dimensione di un lato del trinagolo 
# (per semplicità, si suppone che il triangolo in questione sia un triangolo rettangolo).
# Il costruttore della classe deve ricevere come argomento solo il lato del triangolo, ed impostare il nome della forma su "Triangolo".
# Il metodo getArea() deve calcolare l'area del triangolo.
# Il metodo render() deve stamapre su schermo un triangolo rettangolo avente i due cateti di lunghezza pari ai valori passati nel 
# costruttore. Il traingolo da stampare deve essere un traingolo vuoto (" "), avente degli asterischi ("*") lungo il suo perimetro. 
# (Vedi Esempio di output)
# Hint: per il disegno utilizzare print("*", end=" "), dato che l'argomento end = " " permette di controllare come termina ogni 
# chiamata a print, e impostandolo a uno spazio si può fare in modo che tutte le stampe successive siano sulla stessa riga, 
# separate da uno spazio.
from abc import ABC, abstractmethod
class Forma(ABC):
    def __init__(self, nome_forma: str):
        self.nome_forma = nome_forma

    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def render(self):
        pass

class Quadrato(Forma):
    def __init__(self, lunghezza_lato: int):
        super().__init__("Quadrato")
        self.lunghezza_lato = lunghezza_lato

    def getArea(self):
        return self.lunghezza_lato ** 2
    
    def render(self):
        for c in range(self.lunghezza_lato):
            print("*", end=" ")
        print()
        for r in range(self.lunghezza_lato-2): 
            print("*", end=" ")
            for c in range(self.lunghezza_lato-2):
                print(" ", end=" ")
            print("*")
        for c in range(self.lunghezza_lato):   
            print("*", end=" ")
        

q = Quadrato(4)       
print(q.getArea())
print(q.render())

class Rettangolo(Forma):
    def __init__(self, lunghezza_base, lunghezza_altezza):
       super().__init__("Rettangolo")
       self.lunghezza_base = lunghezza_base
       self.lunghezza_altezza = lunghezza_altezza

    def getArea(self):
        return self.lunghezza_base * self.lunghezza_altezza 

    def render(self):
        for c in range(self.lunghezza_base):
            print("*", end=" ")
        print()
        for r in range(self.lunghezza_altezza-2): 
            print("*", end=" ")
            for c in range(self.lunghezza_base-2):
                print(" ", end=" ")
            print("*")
        for c in range(self.lunghezza_base):   
           print("*", end=" ")

r = Rettangolo(7, 5)       
print(r.getArea())
print(r.render())