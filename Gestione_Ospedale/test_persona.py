### Creazione di Test Case con UnitTest

# Creare una suite di test utilizzando il modulo unittest di Python per verificare il corretto funzionamento delle classi Persona, Dottore, Paziente e Fattura fornite nel codice. I test devono coprire l'inizializzazione degli oggetti, i metodi di accesso e modifica degli attributi, e i comportamenti specifici delle classi.
# Istruzioni
# Creare un nuovo file Python denominato "test_persona.py".
# Importare il modulo unittest e tutte le classi definite.

# Test della Classe Persona
# - Creare una classe di test chiamata TestPersona che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Persona con nome e cognome.
# - Scrivere test per verificare:
# - L'inizializzazione corretta degli attributi first_name, last_name e age.
# - Il funzionamento dei metodi setName, setLastName e setAge.

# Test della Classe Dottore
# - Creare una classe di test chiamata TestDottore che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Dottore con nome, cognome, specializzazione e parcella.
# - Scrivere test per verificare:
# - L'inizializzazione corretta degli attributi specifici di Dottore.
# - Il funzionamento del metodo isValidDoctor con diverse età.

# Test della Classe Paziente
# - Creare una classe di test chiamata TestPaziente che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Paziente con nome, cognome e ID.
# - Scrivere test per verificare:
# - L'inizializzazione corretta degli attributi specifici di Paziente.

# Test della Classe Fattura
# - Creare una classe di test chiamata TestFattura che eredita da unittest.TestCase.
# - Implementare il metodo setUp per inizializzare un oggetto Fattura con una lista di pazienti e un dottore valido.
# - Scrivere test per verificare:
# - L'inizializzazione corretta della classe Fattura.
# - Il calcolo corretto del salario e del numero di fatture.
# - L'aggiunta e la rimozione di pazienti dalla lista.



import unittest
from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fatture import Fattura
"""
class TestPerosna(unittest.TestCase):
    def setUp(self):
        persona = Persona("Mario", "Rossi", 30)
        self.assertEqual(persona.first_name, "Mario")
        self.assertEqual(persona.last_name, "Rossi")
        self.assertEqual(persona.age, 30)
        persona.setName("Luigi")
        persona.setLastName("Bianchi")
        persona.setAge(40)
        persona.getName()
  

class TestDottore(unittest.TesctCase):
    def setUp(self):
        self.dottore = Dottore("Mario", "Rossi", "Cardiologo", 100)

"""
class TestPersona(unittest.TestCase):
    def setUp(self):
        self.persona = Persona("Mario", "Rossi")

    def test_initialization(self):
        self.assertEqual(self.persona.getName(), "Mario")
        self.assertEqual(self.persona.getLastName(), "Rossi")
        self.assertEqual(self.persona.getAge(), 31)

    def test_setName(self):
        self.persona.setName("Luigi")
        self.assertEqual(self.persona.getName(), "Luigi")
        self.persona.setName(123)
        self.assertIsNone(self.persona.getName())

    def test_setLastName(self):
        self.persona.setLastName("Verdi")
        self.assertEqual(self.persona.getLastName(), "Verdi")
        self.persona.setLastName(456)
        self.assertIsNone(self.persona.getLastName())

    def test_setAge(self):
        self.persona.setAge(25)
        self.assertEqual(self.persona.getAge(), 25)
        self.persona.setAge("vecchio")
        self.assertNotEqual(self.persona.getAge(), "vecchio")

class TestDottore(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Anna", "Bianchi", "Cardiologo", 100.0)

    def test_initialization(self):
        self.assertEqual(self.dottore.getName(), "Anna")
        self.assertEqual(self.dottore.getLastName(), "Bianchi")
        self.assertEqual(self.dottore.getAge(), 40)
        self.assertEqual(self.dottore.getSpecialization(), "Cardiologo")
        self.assertEqual(self.dottore.getParcel(), 100.0)

    def test_isAValidDoctor(self):
        self.assertTrue(self.dottore.isAValidDoctor())
        self.dottore.setAge(25)
        self.assertFalse(self.dottore.isAValidDoctor())

class TestPaziente(unittest.TestCase):
    def setUp(self):
        self.paziente = Paziente("Luca", "Neri", 30, "PZ123")

    def test_initialization(self):
        self.assertEqual(self.paziente.getName(), "Luca")
        self.assertEqual(self.paziente.getLastName(), "Neri")
        self.assertEqual(self.paziente.getAge(), 30)
        self.assertEqual(self.paziente.getidCode(), "PZ123")
        

if __name__ == "__main__":
    unittest.main()                     

    



