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
                return name
            
    
