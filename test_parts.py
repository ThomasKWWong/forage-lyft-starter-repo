import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

#Engine tests
class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_one = True

        engine = SternmanEngine(warning_light_is_one)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_one = False

        engine = SternmanEngine(warning_light_is_one)
        self.assertFalse(engine.needs_service())


class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        self.assertFalse(engine.needs_service())


#Battery tests
class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


class testSpindler(unittest.TestCase): #updated for 3 years
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())


#Tire tests
class TestCarrigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        array_of_tire_worness = [0.9, 0, 0, 0]

        tire = CarriganTire(array_of_tire_worness)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        array_of_tire_worness = [1, 1, 1, 0]

        tire = OctoprimeTire(array_of_tire_worness)
        self.assertTrue(tire.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        array_of_tire_worness = [1, 1, 1, 0]

        tire = OctoprimeTire(array_of_tire_worness)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        array_of_tire_worness = [1, 1, 0.5, 0.4]

        tire = OctoprimeTire(array_of_tire_worness)
        self.assertFalse(tire.needs_service())


if __name__ == '__main__':
    unittest.main()