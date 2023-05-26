#Import all engines and batteries
from car import Car

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire
#--------------------------------


def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, array_of_tire_worness):
    #capulet, spindler
    capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
    spindlerBattery = SpindlerBattery(last_service_date, current_date)
    calliopeCar = Car(capuletEngine, spindlerBattery)
    return calliopeCar #return car object

def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, array_of_tire_worness):
    #willoughby, spindler
    willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
    spindlerBattery = SpindlerBattery(last_service_date, current_date)
    glissadeCar = Car(willoughbyEngine, spindlerBattery)
    return glissadeCar #return car object

def create_palindrome(current_date, last_service_date, warning_light_on, array_of_tire_worness):
    #sternman, spindler
    sternmanEngine = SternmanEngine(warning_light_on)
    spindlerBattery = SpindlerBattery(last_service_date, current_date)
    glissadeCar = Car(sternmanEngine, spindlerBattery)
    return glissadeCar #return car object

def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, array_of_tire_worness):
    #willoughby, nubbin
    willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
    nubbinBattery = NubbinBattery(last_service_date, current_date)
    glissadeCar = Car(willoughbyEngine, nubbinBattery)
    return glissadeCar #return car object

def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, array_of_tire_worness):
    #capulet, nubbin
    capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
    nubbinBattery = NubbinBattery(last_service_date, current_date)
    glissadeCar = Car(capuletEngine, nubbinBattery)
    return glissadeCar #return car object