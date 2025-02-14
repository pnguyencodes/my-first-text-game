# All creatures know the language "common."
class Creature:
    def __init__(self, gender: str, race: str, traits=None):
        self._language = ["common"]
        self._gender = gender
        self._race = race
        self._traits = traits

    @property
    def language(self):
        return self._language

    @property    
    def gender(self):
        return self._gender
    
    @property
    def race(self):
        return self._race

    @property
    def traits(self):
        return self._traits
    
    def is_human(self):
        return False
    
    def is_elf(self):
        return False
    
class Human(Creature):
    def __init__(self, gender: str, race: str, traits=None):
        super().__init__(gender, race, traits)

    def is_human(self):
        return True

class Elf(Creature):
    def __init__(self, gender: str, race: str, traits=None):
        super().__init__(gender, race, traits)

    def is_elf(self):
        return True