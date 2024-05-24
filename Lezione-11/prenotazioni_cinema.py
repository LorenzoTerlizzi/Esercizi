class Film:
    def __init__(self, titolo: str, durata: float):
        self.titolo = titolo
        self.durata = durata

class Sala:
    def __init__(self, id_sala: int, film_attuale: Film, posti_totali: int):
        self.id_sala = id_sala
        self.film_attuale = film_attuale
        self.posti_totali = posti_totali
        self.posti_prenotati = 0
    
    def prenota_posti(self, num_posti):
        posti_d = self.posti_totali - self.posti_prenotati
        if num_posti < posti_d:
            print("Prenotazione posti confermata")
            self.posti_prenotati += num_posti
        else:
            print("Errore prenotazione posti")
    
    def posti_disponibili(self):
        return self.posti_totali - self.posti_prenotati
    
class Cinema:
    def __init__(self):
        self.sale = []

    def aggiungi_sala(self, sala):
        self.sale.append(sala)

    def prenota_film(self, titolo_film: str, num_posti: int):
        for sala in self.sale:
            if titolo_film in sala.film_attuale.titolo:
                return sala.prenota_posti(num_posti)
        return print("Film non trovato")   

film1: Film = Film("film 1", 120)
film2: Film = Film("film 2", 99)
film3: Film = Film("film 3", 80)

sala1: Sala = Sala(10, film1, 30)
sala2: Sala = Sala(20, film2, 45)
sala3: Sala = Sala(30, film3, 40)

cinema: Cinema = Cinema()
cinema.aggiungi_sala(sala1)
cinema.aggiungi_sala(sala2)
print(cinema.prenota_film("film 1", 4))
print(cinema.prenota_film("film 2", 10))
sala2.prenota_posti(12)
print(sala2.posti_disponibili())