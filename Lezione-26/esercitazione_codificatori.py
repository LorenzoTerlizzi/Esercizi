#Si crei una classe astratta chiamata CodificatoreMessaggio che ha un solo metodo astratto codifica(testoInChiaro), 
# dove testoInChiaro sarà il messaggio da codificare. Il metodo restituirà il messaggio codificato.

#Si crei una classe astratta chiamata DecodificatoreMessaggio che abbia un solo metodo decodifica(testoCodificato), 
# dove testoCodificato sarà il messaggio da decodificare. Il metodo ritornerà il messaggio decodificato.

#Si crei una classe CifratoreAScorrimento che implementa le classi astratte CodificatoreMessaggio e 
# DecodificatoreMessaggio. Il costruttore dovrebbe ricevere un numero intero chiamato chiave. Si definisca il 
# metodo codifica(testoInChiaro) così che ogni lettera del testo sia spostata dal valore contenuto in chiave.
#Per esempio, se chiave è uguale a 3, la lettera 'a' sarà sostituita da 'd', la lettera 'b' sarà sostituita da 'e', 
# la lettera 'c' sarà sostituita da 'f' e così via.

#     Suggerimento: si potrebbe definire un metodo privato sposta_carattere(c) che restituisca la codifica di 
#     un singolo carattere c da concatenare agli altri per costruire il messaggio codificato nel metodo codifica(testoInChiaro).


#Si crei una classe CifratoreACombinazione che implementa le classi astratte CodificatoreMessaggio e 
# DecodificatoreMessaggio. Il costruttore dovrebbe ricevere un numero intero chiamato n. Si definisca il metodo 
# codifica(testoInChiaro) così che il messaggio sia combinato n volte. Per eseguire una singola combinazione, 
# si divide il messaggio a metà e poi si prendono i caratteri da ognuna delle metà in modo alternato. 
# Per esempio, se il messaggio è 'abcdefghi', le metà sono 'abcde' e 'fghi' (nel caso in cui la lunghezza del testo da 
# decifrare sia un numero dispari, la prima metà deve essere più lunga della seconda metà). Il messaggio combinato 
# è 'afbgchdie'.

#    Suggerimento: si potrebbe definire un metodo privato combinazione(testo) che esegue la combinazione del testo e 
#    ritorni il testo cifrato da usare nel metodo codifica(testoInChiaro).


#Si scriva il metodo decodifica(testoCodificato) per ognuna delle classi CifrarioAScorrimento e CifrarioACombinazione.

#    Suggerimento: definire il metodo privato decodifica_carattere() per la classe CifrarioAScorrimento che compie 
#    un'azione inversa al metodo sposta_carattere().

#    Suggerimento: definire il metodo privato decodifica_combinazione() per la classe CifrarioACombinazione che 
#    compie un'azione inversa al metodo combinazione().


#Infine, si implementi anche un metodo per leggere il testo da cifrare da un file e un metodo per scrivere il testo 
# cifrato su un file per entrambe le classi CifratoreAScorrimento e CifratoreACombinazione.

from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):
    @abstractmethod
    
    def codifica(self, testoInChiaro):
        pass

class DecodificatoreMessaggio(ABC):
    @abstractmethod
    def decodifica(self, testoCodificato):
        pass


class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, chiave):
        self.chiave = chiave
    def codifica(self, testoInChiaro):
        testoCodificato = ""
        for c in testoInChiaro:

            testoCodificato += self.sposta_carattere(c)
            return testoCodificato
        
class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, n: int):
        self.n = n
    def codifica(self, testoInChiaro):

