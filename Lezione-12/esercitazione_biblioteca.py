        
# Lorenzo Terlizzi
# 29/05/2024

# Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un inventario di libri e le operazioni di prestito e restituzione degli stessi.
# Gli utenti del sistema devono essere in grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.

# Classi:
# - Libro: Rappresenta un libro con titolo, autore, stao del prestito. Il libro deve essere inizialmente disponibile (non prestato).

# - Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

# Metodi:
# - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

# - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.

# - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

# - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri disponibili, restituisce un messaggio di errore.

class Libro:
    def __init__(self, titolo: str, autore: str, stato_prestito: bool = True):
        self.titolo = titolo
        self.autore = autore
        self.stato_prestito: bool = stato_prestito
    
class Biblioteca:
    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, libro: str):
        if libro not in self.libri:
            self.libri.append(libro)
        else:
            print("Libro già presente")

    def presta_libro(self, titolo: str):
        for i in self.libri:
            if titolo == i.titolo and i.stato_prestito == True:
                return f"{titolo}: Libro disponibile"
            else:
                return f"{titolo}:Libro non disponibile"
                break

    def restituisci_libro(self, titolo):
        for i in self.libri:
            if titolo == i.titolo and i.stato_prestito == False:
                return f"{titolo}:Libro disponibile"
            else:
                return f"{titolo}:Libro non disponibile"
                break    

    def mostra_libri_disponibili(self):
        for i in self.libri:
            if i.stato_prestito == True:
                print(self.libri(i.stato_prestito == True))

libro1: Libro = Libro("libro1", "Io", )
libro2: Libro = Libro("libro2", "Tu", False)
libri: Biblioteca = Biblioteca()

libri.aggiungi_libro(libro1)
libri.aggiungi_libro(libro2)
libri.aggiungi_libro(libro1)
print(libri.presta_libro("libro2"))
print(libri.presta_libro("libro1"))
print(libri.presta_libro("Libro2"))
print(libri.restituisci_libro("libro1"))

