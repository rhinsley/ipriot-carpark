# Ryan Hinsley, 04/12/2023

class CarPark:
    def __init__(self, location="Unknown", capacity=0, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates
        self.sensors = sensors
        self.displays = displays

    def __str__(self):
        return f"Car Park at 123 Example Street, with {self.capacity} bays."

