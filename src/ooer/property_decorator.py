class Celsius:
    def __init__(self, temperature=0) -> None:
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Not possibruuu")
        self._temperature = value


hooman = Celsius(37)
print(f"{hooman.get_temperature()}")


# using property class
class CelsiusProperty(Celsius):
    def __init__(self, temperature=0):
        self.temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


human = CelsiusProperty(37)

print(human.temperature)

print(human.to_fahrenheit())

coldest_thing = Celsius(-300)
