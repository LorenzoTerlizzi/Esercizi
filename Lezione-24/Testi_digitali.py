class Documento:
   
    def __init__(self, testo: str):
        self.testo = testo

    def getText(self):
        return self.testo

    def setText(self, testo):
        self.testo = testo

    def isInText(self, parolaChiave: str) -> bool:
        if parolaChiave in self.testo:
            return True
        else:
           return "Parola non presente nel testo"

doc = Documento("ciao sono lorenzo")
doc.setText("Ciao sono lorenzo")
print(doc.getText())
print(doc.isInText("lorenzo"))

class Email(Documento):
    def __init__(self, testo, mittente: str, destinatario: str, titoloMess: str):
        super().__init__(testo)
        self.mittente = mittente
        self.destinatario = destinatario
        self.titoloMess = titoloMess

    def getDestinatario(self):
        return self.destinatario
    def setDestinatario(self, destinatario):
        self.destinatario = destinatario

    def getMittente(self):
        return self.mittente
    def setMittente(self, mittente):
        self.mittente = mittente

    def getTitolo(self):
        return self.titoloMess
    def setTitolo(self, titoloMess):
        self.titoloMess = titoloMess

    def getText(self):
        return f"Da: {self.getMittente()}, A: {self.getDestinatario()} \nTitolo: {self.getTitolo()} \nMessaggio: {super().getText()}"
    
    def writeToFile(self):
        

