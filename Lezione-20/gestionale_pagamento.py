# 1. GESTIONALE PAGAMENTO
# Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza l'importo del pagamento e 
# si definiscano appropriati metodi get() e set(). L'importo non è un parametro da passare in input alla classe Pagamento ma deve 
# essere inizializzato utilizzando il metodo set() dove opportuno. Si crei inoltre un metodo dettagliPagamento() che visualizza 
# una frase che descrive l'importo del pagamento, ad esempio: "Importo del pagamento: €20.00". Quando viene stampato, 
# l'importo è sempre con 2 cifre decimali.

# Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. 
# Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. 
# Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 
# 20 euro, 10 euro, 5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono 
# necessarie per pagare l'importo in contanti.

# Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. 
# Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, e il numero della carta 
# di credito. Infine, si ridefinisca il metodo dettagliPagamento() per includere tutte le informazioni della carta di credito 
# oltre all'importo del pagamento.

# Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti e 
# si invochi dettagliPagamento() per ognuno di essi.

class Pagamento():
    def __init__(self):
        self.__importo = 0.0

    def setImporto(self, importo: float):
        self.__importo = importo

    def getImporto(self):
        return self.__importo
    
    def dettagliPagamento(self):
        print(f"Importo del pagamento: €{self.getImporto:.2f}")

class PagamentoContanti(Pagamento):
    def __init__(self, importo):
        super().__init__()
        self.setImporto(importo)
    def dettagliPagamento(self):
        print(f"Importo del pagamento in contanti: €{self.getImporto():.2f}")

    def inPezziDa(self):
        importo = self.getImporto()
        pezzi = {
            500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0,
            2: 0, 1: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.01: 0}

        for value in pezzi:
            pezzi[value] = int(importo // value)
            importo -= pezzi[value] * value
            importo = round(importo, 2)  

        for value, quantità in pezzi.items():
            if quantità > 0:
                tipo = "banconote" if value >= 5 else "monete"
                print(f"{quantità} {tipo} da €{value:.2f}")
                    
                
   
class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, importo, nomeTitolare, scadenzaCarta, numeroCarta):
        super().__init__()
        self.setImporto(importo)
        self.nomeTitolare: str = nomeTitolare
        self.scadenzaCarta: str = scadenzaCarta
        self.numeroCarta: int = numeroCarta

    def dettagliPagamento(self):
       print(f"Importo del pagamento con carta di credito: €{self.getImporto():.2f}")
       print(f"Nome del titolare: {self.nomeTitolare} \n Numero carta: {self.numeroCarta} \n Data Scadenza carta: {self.scadenzaCarta}")





pc = PagamentoContanti(360)
pc.dettagliPagamento()
pc.inPezziDa()
pcc = PagamentoCartaDiCredito(150, "Giuseppe Verdi", "12/05/2030", 27472924)
pcc.dettagliPagamento()


        




    

