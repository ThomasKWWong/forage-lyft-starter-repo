#Import all engines and batteries
from car import Car

from engine.capulet_engine import Capulet
from engine.sternman_engine import Sternman
from engine.willoughby_engine import Willoughby

from battery.nubbin_battery import Nubbin
from battery.spindler_battery import Spindler
#--------------------------------


def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
    #capulet, spindler
    capuletEngine = Capulet(current_mileage, last_service_mileage)
    spindlerBattery = Spindler(last_service_date, current_date)
    calliopeCar = Car(capuletEngine, spindlerBattery)
    return calliopeCar #return car object

def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
    #willoughby, spindler
    willoughbyEngine = Willoughby(current_mileage, last_service_mileage)
    spindlerBattery = Spindler(last_service_date, current_date)
    glissadeCar = Car(willoughbyEngine, spindlerBattery)
    return glissadeCar #return car object

def create_palindrome(current_date, last_service_date, warning_light_on):
    #sternman, spindler
    sternmanEngine = Sternman(warning_light_on)
    spindlerBattery = Spindler(last_service_date, current_date)
    glissadeCar = Car(sternmanEngine, spindlerBattery)
    return glissadeCar #return car object

def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
    #willoughby, nubbin
    willoughbyEngine = Willoughby(current_mileage, last_service_mileage)
    nubbinBattery = Nubbin(last_service_date, current_date)
    glissadeCar = Car(willoughbyEngine, nubbinBattery)
    return glissadeCar #return car object

def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
    #capulet, nubbin
    capuletEngine = Capulet(current_mileage, last_service_mileage)
    nubbinBattery = Nubbin(last_service_date, current_date)
    glissadeCar = Car(capuletEngine, nubbinBattery)
    return glissadeCar #return car object