from abc import ABC, abstractmethod
from typing import Protocol


"""
https://peps.python.org/pep-0544/

Protocols: Structural subtyping (static duck typing) 

not a nominal typing

Protocol does not inherits but defines an interface to implement

"""


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("woof")


class AnimalProtocol(Protocol):
    def speak(self):
        ...


def make_sound(animal: AnimalProtocol) -> None:
    print(animal.speak())


make_sound(Dog())


class Cat:
    def speak(self):
        print("meow")


make_sound(Cat())
