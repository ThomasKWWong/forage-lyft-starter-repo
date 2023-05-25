#from abc import ABC, abstractmethod


class Car():
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    
    def needs_service(self):
        if self.engine.needs_service() == True or self.battery.needs_service() == False:
            return True
        else:
            return False
