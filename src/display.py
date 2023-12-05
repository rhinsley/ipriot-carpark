# Ryan Hinsley, 04/12/2023

class Display:
    def __init__(self, id, car_park, message=None, is_on=False):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"Display {self.id}: Welcome to {self.car_park}."

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")

