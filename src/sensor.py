# Ryan Hinsley, 04/12/2023

# from car_park import CarPark
from abc import ABC, abstractmethod
import random


class Sensor(ABC):
    def __init__(self, id, car_park, is_active=False):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor {self.id}: Welcome to {self.car_park}."

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    @abstractmethod
    def update_car_park(self, plate):
        pass


class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")


class ExitSensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")

    def _scan_plate(self):
        return random.choice(self.car_park.plates)
