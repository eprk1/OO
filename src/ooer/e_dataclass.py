from dataclasses import dataclass, field
import random
import string


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


class Person:
    def __init__(self, name: str, address: str, active: bool = True):
        self.name = name
        self.address = address
        self.active = active

    def __str__(self) -> str:
        return f"{self.name}, {self.address}, {self.active}"


@dataclass
class NewPerson:
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    id: str = field(default_factory=generate_id)

    # this means cannot pass in as constructor
    no_pass_id: str = field(init=False, default_factory=generate_id)

    search_string: str = field(init=False)
    private_search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.search_string = f"{self.name}"
        self.private_search_string = f"{self.name}"


# this means you cant update the value ie FrozenNewPerson().name = "eugene" will raise FrozenInstanceError
@dataclass(frozen=True)
class FrozenNewPerson:
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    id: str = field(default_factory=generate_id)

    # this means cannot pass in as constructor
    no_pass_id: str = field(init=False, default_factory=generate_id)

    search_string: str = field(init=False)
    private_search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.search_string = f"{self.name}"
        self.private_search_string = f"{self.name}"


# @dataclass(kw_only=True)
# @dataclass()


myName = "Eugene"
myAddress = "Earth"

print(Person(myName, myAddress))

print(NewPerson(myName, myAddress))
