
class Worker:
    name = None
    surname = None
    position = None
    _income = {'wage': 'wage',
               'bonus': 'bonus'
               }

class Position(Worker):
    def __init__(self, name:str, surname:str, wage:int, bonus:int):
        self.name = name
        self.surname = surname
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def get_full_name(self):
        return self.name  + " " + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

position = Position(name="Timur", surname="Abdikarimov", wage=100000, bonus=40000)

print(f'{position.get_full_name(),position.get_total_income()}')
