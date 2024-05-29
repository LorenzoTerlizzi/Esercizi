class Prodotto:
    def __init__(self, nome: str, quantità: int):
        self.nome = nome
        self.quantità = quantità

class Magazzino:
    def __init__(self):
        self.prodotti = []

    def aggiungi_prodotto(self, prodotto: Prodotto):
        self.prodotti.append(prodotto)
    
    def cerca_prodotto(self, name: str):
        for a in self.prodotti:
            if name in a.nome:
                return f"{name} trovato"
            
    def verifica_disponibilità(self, nome: str):
        for prodotto in self.prodotti:
            if prodotto.nome == nome:
                return f"{prodotto.nome} disponibile"
        return f"{prodotto.nome} non disponibile"


prodotto1: Prodotto = Prodotto("Acqua", 5)
prodotto2: Prodotto = Prodotto("Tè", 3)
prodotti: Magazzino = Magazzino()

prodotti.aggiungi_prodotto(prodotto1)
prodotti.aggiungi_prodotto(prodotto2)   

print(prodotti.cerca_prodotto("Acqua"))
print(prodotti.verifica_disponibilità("Acqua"))
print("\n")
print(prodotti.cerca_prodotto("Tè"))
print(prodotti.verifica_disponibilità("Tè"))