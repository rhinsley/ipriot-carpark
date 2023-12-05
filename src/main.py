# Ryan Hinsley, 04/12/2023

from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

# create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
# create an entry sensor object with id 1, is_active True, and car_park car_park
# create an exit sensor object with id 2, is_active True, and car_park car_park
# create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
# drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
# drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)

def main():
    car_park = CarPark("moondalup", 100, log_file="moondalup.txt")
    car_park.write_config()
    entry_sensor = EntrySensor(1, car_park, True)
    exit_sensor = ExitSensor(2, car_park, True)
    display = Display(1, car_park, True, "Welcome to Moondalup")

    for iterable in range(10):
        entry_sensor.detect_vehicle()
    for iterable in range(2):
        exit_sensor.detect_vehicle()

if __name__ == "__main__":
    main()
