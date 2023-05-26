#from abc import ABC, abstractmethod


class Car():
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    
    def needs_service(self):
        if self.engine.needs_service() == True or self.battery.needs_service() == True or self.tire.needs_service() == True:
            return True
        else:
            return False
