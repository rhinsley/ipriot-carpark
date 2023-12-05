# Ryan Hinsley, 04/12/2023

from pathlib import Path
from datetime import datetime
from display import Display
from sensor import Sensor


class CarPark:
    def __init__(self, location="Unknown", capacity=0, plates=None, sensors=None, displays=None, log_file=Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)

    def __str__(self):
        return f"Car Park at 123 Example Street, with {self.capacity} bays."

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as file:
            file.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        self.plates.pop(self.plates.index(plate))
        self.update_displays()
        self._log_car_activity(plate, "exited")

    def update_displays(self):
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)

    @property
    def available_bays(self):
        return max(self.capacity - len(self.plates), 0)
