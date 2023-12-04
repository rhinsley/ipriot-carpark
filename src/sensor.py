# Ryan Hinsley, 04/12/2023

class Sensor:
    def __init__(self, id, car_park, is_active=False):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor {self.id}: Welcome to {self.car_park}."


class EntrySensor(Sensor):
    ...


class ExitSensor(Sensor):
    ...
