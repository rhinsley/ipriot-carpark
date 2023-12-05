# Ryan Hinsley, 04/12/2023

class Display:
    def __init__(self, id, car_park, is_on=False, message=None, available_bays=None, temperature=None):
        self.id = id
        self.is_on = is_on
        self.car_park = car_park
        self.message = message
        self.available_bays = available_bays
        self.temperature = temperature

    def __str__(self):
        return f"Display {self.id}: Welcome to {self.car_park}."

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")
            if key == 'message':
                self.message = value
            elif key == 'available_bays':
                self.available_bays = value
            elif key == 'temperature':
                self.temperature = value



