"""
use builder patter when,

need to create an obj that is composed of multiple parts and 
the composition needs to be done step by step


"""


class Computer:
    def __init__(self, serial_number) -> None:
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = (
            f"Memory: {self.memory}GB",
            f"Hard Disk: {self.hdd}GB",
            f"Graphics Card: {self.gpu}",
        )
        return "\n".join(info)


# director
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer("AG12312308")

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


# step by step construction
class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        steps = (
            self.builder.configure_memory(memory),
            self.builder.configure_hdd(hdd),
            self.builder.configure_gpu(gpu),
        )

    @property
    def computer(self):
        return self.builder.computer


def main():
    eng = HardwareEngineer()
    eng.construct_computer(hdd=500, memory=8, gpu="nice one")
    computer = eng.computer
    print(computer)


from abc import ABC, abstractmethod
from enum import Enum
import time

# pizza is prepared in steps that should follow a specific order
# To add the sauce, you first need to prepare the dough
# to add the topping, you first need to add the sauch
# and you cant bake unless both sauce and topping are placed on the dough
# not to mention, different baking times to produce diff thickness

PizzaProgress = Enum("PizzaProgress", "queued preparation baking ready")
PizzaDough = Enum("PizzaDough", "thin thick")
PizzaSauce = Enum("PIzzaSauce", "tomato creme_fraiche")
PizzaTopping = Enum(
    "PizzaTopping",
    "mozzarella double_mozzarella bacon ham mushrooms red_onion oregano",
)
STEP_DELAY = 3


class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print(f"preparing the {self.dough.name} dough of your {self}")

        time.sleep(STEP_DELAY)
        print(f"done with the {self.dough.name} dough")


class PizzaBuilder(ABC):
    @abstractmethod
    def prepare_dough(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_topping(self):
        pass

    @abstractmethod
    def bake(self):
        pass


class MargaritaBuilder(PizzaBuilder):
    def __init__(self) -> None:
        self.pizza = Pizza("margarita")

        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print("adding the tomato sauce to your margarita")
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print("done with the tomato sauce")

    def add_topping(self):
        topping_desc = "double mozzarella, oregano"
        topping_items = (PizzaTopping.oregano, PizzaTopping.double_mozzarella)
        print(f"adding the topping {topping_desc} to your margarita")
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f"done with the topping {topping_desc}")

    def bake(self):
        self.progress = PizzaProgress.baking
        print(f"baking your margarita for {self.baking_time}")
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print(f"your margarita is ready")


class CreamyBaconBuilder(PizzaBuilder):
    def __init__(self) -> None:
        self.pizza = Pizza("creamy bacon")

        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        pass

    def add_sauce(self):
        pass

    def add_topping(self):
        pass

    def bake(self):
        pass


class Waiter:
    def __init__(self) -> None:
        self.builder = None

    def construct_pizza(self, builder: PizzaBuilder):
        self.builder = builder
        steps = (
            builder.prepare_dough,
            builder.add_sauce,
            builder.add_topping,
            builder.bake,
        )
        [step() for step in steps]

    @property
    def pizza(self):
        return self.builder.pizza


def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)

    builder_key = "c"
    builder_key = "m"
    builder = builders[builder_key]()

    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza


# fluent builder

main()
