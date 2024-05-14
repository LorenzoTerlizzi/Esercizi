# Lorenzo Terlizzi
# 14/05/2024

"""

In questo problema ricreerete la classica gara tra la tartaruga e la lepre. Userete la generazione di numeri casuali per sviluppare una simulazione di questo memorabile evento.
I contendenti iniziano la gara dal quadrato \#1 di un percorso composto da 70 quadrati. Ogni quadrato rappresenta una posizione lungo il percorso della corsa.
Il traguardo è al quadrato 70 e il contendente che raggiunge per primo o supera questa posizione vince la gara. Durante la corsa, i contendenti possono occasionalmente perdere terreno. C'è un orologio che conta i secondi. Ad ogni tick dell'orologio, il vostro programma deve aggiornare la posizione degli animali secondo le seguenti regole:

- Tartaruga:
    - Passo veloce (50% di probabilità): avanza di 3 quadrati.
    - Scivolata (20% di probabilità): arretra di 6 quadrati. Non può andare sotto il quadrato 1.
    - Passo lento (30% di probabilità): avanza di 1 quadrato.

- Lepre:
    - Riposo (20% di probabilità): non si muove.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
    -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.

Il percorso è rappresentato attraverso l'uso di una lista. Usate delle variabili per tenere traccia delle posizioni degli animali (i numeri delle posizioni sono da 1 a 70).
Fate partire ogni animale dalla posizione 1 (cioè ai "cancelli di partenza"). Se un animale scivola a sinistra prima del quadrato 1, riportatelo al quadrato 1.

Realizzate le percentuali delle mosse nell'elenco precedente generando un intero a caso, i, nell'intervallo 1 ≤ i ≤ 10. Per la tartaruga eseguite un "passo veloce" quando 1 ≤ i ≤ 5, una "scivolata" quando 6 ≤ i ≤ 7, o un "passo lento" quando 8 ≤ i ≤ 10.
Usate una tecnica simile per muovere la lepre seguendo le sue regole.

Iniziate la gara stampando:
'BANG !!!!! AND THEY'RE OFF !!!!!'

Quindi, per ogni tick dell'orologio (ossia per ogni iterazione di un ciclo), stampate una lista di 70 posizioni che mostra la lettera 'T' nella posizione della tartaruga, la lettera 'H' nella posizione della lepre, il carattere '_' nelle posizioni libere. Occasionalmente,
i contendenti si troveranno sullo stesso quadrato. In questo caso la tartaruga morde la lepre e il vostro programma deve stampare 'OUCH!!!' iniziando da quella posizione.
Tutte le posizioni di stampa diverse dalla 'T', dalla 'H' o dal 'OUCH!!!' (in caso della stessa posizione) devono essere il carattere '_'.

Dopo la stampa di ogni tick, verificate se gli animali hanno raggiunto o superato il quadrato 70.
Se è così, stampate il nome del vincitore e terminate la simulazione. Se vince la tartaruga, stampate "TORTOISE WINS! || VAY!!!". Se vince la lepre, stampate "HARE WINS || YUCH!!!".
Se allo stesso tick dell'orologio vincono tutti e due gli animali, potreste voler favorire la tartaruga (la "sfavorita"), oppure stampare "IT'S A TIE.". Se non vince nessun animale,
eseguite una nuova iterazione per simulare il successivo tick dell'orologio.

Requisiti del Codice:
- Utilizzare il modulo random per la generazione dei numeri casuali.
- Definire e utilizzare:
    - una funzione per visualizzare le posizioni sulla corsia di gara,
    - una funzione per calcolare la mossa della tartaruga,
    - una funzione per calcolare la mossa della lepre.
- Implementare un loop per simulare i tick dell'orologio. Ad ogni tick, calcolare le mosse, mostrare la posizione sulla corsia di gara, e determinare l'eventuale fine della gara.

"""
import random
def Posizioni_gara(posizioneTarta: int, posizioneLepre: int):
    lunghezza_lista = 70
    percorso: list[int] = ["_"] * lunghezza_lista
    percorso[posizioneTarta-1] = "T"
    percorso[posizioneLepre-1] = "H"
    if posizioneTarta == posizioneLepre:
        percorso[posizioneTarta -1] = "OUCH!!!"
    return percorso



def Mossa_Tarta(i: int):
    mossa: str = ""
    if 1 <= i <= 5:
        mossa = "Passo Veloce"
    elif 6 <= i <= 7:
        mossa = "Scivolata"
        
    elif 8 <= i <= 10:
        mossa = "Passo Lento"
    return mossa


def Mossa_Lepre(i: int):
    mossa = ""
    if 1 <= i <= 2:
        mossa = "Riposo"
    elif 3 <= i <= 4:
        mossa = "Grande Balzo"
    elif i == 5:
        mossa = "Grande Scivolata"
    elif 6 <= i <= 8:
        mossa = "Picoolo Balzo"
    elif 9 <= i <= 10:
        mossa = "Piccola Scivolata"
    return mossa

posizioneTarta: int = 1
posizioneLepre: int = 1
tempo: list = ["soleggiato", "piovoso"]
energiaTarta: int = 100
energiaLepre: int = 100
while posizioneTarta != 70 and posizioneLepre != 70:
        i: int = random.randint(1, 10)
        t = random.choice(tempo)
        if Mossa_Tarta(i) == "Passo Veloce":
            posizioneTarta = posizioneTarta + 3
            energiaTarta -= 5
            
            if posizioneTarta > 70:
               posizioneTarta = 70
            if t == "piovoso":
                posizioneTarta = posizioneTarta - 1
                    
        elif Mossa_Tarta(i) == "Scivolata":
            posizioneTarta = posizioneTarta - 6
            energiaTarta -= 10
            if posizioneTarta < 1:
               posizioneTarta = 1
            if t == "piovoso":
                posizioneTarta = posizioneTarta - 1
                
        elif Mossa_Tarta(i) == "Passo Lento":
            posizioneTarta = posizioneTarta + 1
            energiaTarta -= 3
            if posizioneTarta > 70:
               posizioneTarta = 70
            if t == "piovoso":
                posizioneTarta = posizioneTarta - 1
                
        

        if Mossa_Lepre(i) == "Riposo":
            posizioneLepre = posizioneLepre
            if t == "piovoso":
                posizioneLepre = posizioneLepre - 1
                
        elif Mossa_Lepre(i) == "Grande Balzo":
            posizioneLepre = posizioneLepre + 9
            if posizioneLepre > 70:
               posizioneLepre = 70
            if t == "piovoso":
                posizioneLepre = posizioneLepre - 1
                
        elif Mossa_Lepre(i) == "Grande Scivolata":
            posizioneLepre = posizioneLepre - 12
            if posizioneLepre < 1:
               posizioneLepre = 1
            if t == "piovoso":
                posizioneLepre = posizioneLepre - 1
                
        elif Mossa_Lepre(i) == "Piccolo Balzo":
            posizioneLepre = posizioneLepre + 1
            if posizioneLepre > 70:
               posizioneLepre = 70
            if t == "piovoso":
                posizioneLepre = posizioneLepre - 1
                
        elif Mossa_Lepre(i) == "Piccola Scivolata":
            posizioneLepre = posizioneLepre - 2
            if posizioneLepre < 1:
               posizioneLepre = 1
            if t == "piovoso":
                posizioneLepre = posizioneLepre - 1
                
        if t == "piovoso":
            print("Tartaruga: ", Mossa_Tarta(i), posizioneTarta, "energia Tartaruga: ", energiaTarta, "\n" "Piovoso: Penalità -1") 
            print("Lepre: ", Mossa_Lepre(i), posizioneLepre, "energia Lepre: ", energiaLepre, "\n" "Piovoso: penalità -2")

        print(Posizioni_gara(posizioneTarta, posizioneLepre))
if posizioneTarta == 70:
    print("Tortoise wins! || Vay!!!")
elif posizioneLepre == 70:
    print("Hare wins || Yuch!!!")
elif posizioneTarta == posizioneLepre:
    print("It's a tie")

