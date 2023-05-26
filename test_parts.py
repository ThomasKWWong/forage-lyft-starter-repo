import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


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

class testSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()