import json

class CharacterSheet:
    def __init__(self, name: str, character_class: str):
        self._name = name
        self._initialize_stats(character_class)
        self._hit_points = self._max_hit_points

    def _initialize_stats(self, character_class: str):
        with open("classes.json") as jf:
            stats = json.loads(jf.read())[character_class]
            self._max_hit_points = stats["max_hit_points"]
            self._strength = stats["strength"]
            self._agility = stats["agility"]
            self._intelligence = stats["intelligence"]

    def __str__(self):
        return f"{self._name}'s stats: HP: {self._hit_points}/{self._max_hit_points}, STR: {self._strength}, " \
                f"AGI: {self._agility}, INT: {self._intelligence}."

class CharacterClass:
    classes = ["warrior", "rogue", "mage"]
