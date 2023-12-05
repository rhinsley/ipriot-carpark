# Ryan Hinsley, 04/12/2023

from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


def main():
    car_park = CarPark("moondalup", 100, log_file="moondalup.txt")
    entry_sensor = EntrySensor(1, car_park, True)
    exit_sensor = ExitSensor(2, car_park, True)
    display = Display(1, car_park, True, "Welcome to Moondalup")

    for iterable in range(10):
        entry_sensor.detect_vehicle()
    for iterable in range(2):
        exit_sensor.detect_vehicle()


if __name__ == "__main__":
    main()
