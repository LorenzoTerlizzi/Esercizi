class Person:
    def __init__(self, name: str, surname: str, birth_date: str, birth_place: str, gender: str) -> None:
        
        self._name: str = name
        self._surname: str = surname
        self._birth_date: str = birth_date
        self._birth_place: str = birth_place
        self._gender: str = gender
        self._ssn: str = None
        self.compute_ssn()

    def get_ssn(self) -> str:
        """
        This function returns the ssn value
        input: none
        return:self._ssn: str, the function returns the ssn value
        """
        return self._ssn
    
    def set_ssn(self, ssn: str) -> None:
        """
        This function set the snn value
        input: ssn: str, this parameter set the snn value
        return: none
        """
        #self._ssn = ssn
        raise Exception("You cannot modify the ssn number!")


    def get_name(self):
        """
        This function returns a person's name
        input: none
        return:self._name: str, the function returns the person's name
        """
        return self._name
    
    def set_name(self, name: str) -> None:
        """
        This function set the attribute name
        input: name: str, the parameter contains the user's name
        return: None
        """
        
        self._name = name
        self._ssn = self.compute_ssn()
    
    def __str__(self)-> str:
        return f"name: {self._name}, surname: {self._surname}, ssn: {self._ssn}"
    
    def compute_ssn(self) -> bool:
        """
        Check the ssn' correctness
        """
        vocali= "a e i o u A E I O U"
        for a in range(len(vocali)):
            self._name = self._name.replace(vocali[a], "")
            self._surname = self._surname.replace(vocali[a], "")
        day = self._birth_date[:2]
        month = self._birth_date[3:5]
        if month == "01":
            month = "A"
        elif month == "02":
            month = "B"
        elif month == "03":
            month = "C"
        elif month == "04":
            month = "D"
        elif month == "05":
            month = "E"
        elif month == "06":
            month = "H"
        elif month == "07":
            month = "L"
        elif month == "08":
            month = "M"
        elif month == "09":
            month = "P"
        elif month == "10":
            month = "R"
        elif month == "11":
            month = "S"
        elif month == "12":
            month = "T"
        year = self._birth_date[-2:]
        first_three_name_char = self._surname[:3]
        last_three_name_char = self._name[0] + self._name[2] + self._name[3]

        self._ssn = first_three_name_char.upper() + last_three_name_char.upper() + year + month + day + month

person_1: Person = Person(name="Lorenzo", surname="Terlizzi", birth_date="30/06/2004", birth_place="Roma", gender="Male")
person_2: Person = Person(name="Valentino", surname="Rossi", birth_date="12/02/2004", birth_place="Roma", gender="Male")

print(str(person_1))
print(str(person_2))

print(person_1.get_ssn())
queue: list [Person] = [person_1, person_2]



