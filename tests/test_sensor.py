import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.entry_sensor = EntrySensor(1, self.car_park, True)
        self.exit_sensor = ExitSensor(2, self.car_park, True)

    def test_sensors_initialized_with_all_attributes(self):
        # EntrySensor
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)
        self.assertEqual(self.entry_sensor.is_active, True)
        # ExitSensor
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertEqual(self.exit_sensor.id, 2)
        self.assertIsInstance(self.exit_sensor.car_park, CarPark)
        self.assertEqual(self.exit_sensor.is_active, True)

    def test_detect_vehicle(self):
        # EntrySensor
        self.entry_sensor.detect_vehicle()
        self.assertTrue(self.car_park.plates)  # plates added to CarPark
        # ExitSensor
        self.exit_sensor.detect_vehicle()
        self.assertFalse(self.car_park.plates)  # plates removed from CarPark


if __name__ == "__main__":
    unittest.main()
