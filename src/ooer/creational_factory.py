# factory method
# decouple object consumer/users from object creatork
# this decoupling means introducing changes to creationg object is easy
# because no changes need to the object consumers/users

from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as etree


class JSONDataExtractor:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLDataExtrator:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


# factory method
def dataextraction_factory(filepath):
    if filepath.endswith("json"):
        extractor = JSONDataExtractor
    elif filepath.endswith("xml"):
        extractor = XMLDataExtrator
    else:
        raise ValueError(f"Cannot extract data from {filepath}")

    return extractor(filepath)


def main():
    # sqlite_factory = dataextraction_factory("data/person.sql")

    json_factory = dataextraction_factory("data/movies.json")
    json_data = json_factory.parsed_data
    for movie in json_data:
        print(f"Title: {movie['title']}")


main()


class Hero(ABC):
    @abstractmethod
    def interact_with(self, obstacle):
        pass


class Obstacle(ABC):
    @abstractmethod
    def action(self):
        pass


class Frog(Hero):
    def __init__(self, name):
        self.name = name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f"{self} the Frog encounters {obstacle} and {act}"
        print(msg)


class Bug(Obstacle):
    def __str__(self) -> str:
        return "a bug"

    def action(self):
        return "eats it"


# abstract factory
class FrogWorld:
    def __init__(self, name) -> None:
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n\n\t------- Frog World -------"

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard(Hero):
    def __init__(self, name) -> None:
        self.name = name

    def interact_with(self, obstacle):
        act = obstacle.action()
        msg = f"{self.name} the Wizard battles against {obstacle} and {act}"
        print(msg)


class Orc(Obstacle):
    def __str__(self):
        return "an evil orc"

    def action(self):
        return "defeats it"


# abstract factory
class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n\n\t---- Wizard World ----"

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Orc()


class GameEnvironment:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def main_new():
    age = 18
    name = "foo"

    game = FrogWorld if age < 18 else Wizard
    environment = GameEnvironment(game(name))
    environment.play()
