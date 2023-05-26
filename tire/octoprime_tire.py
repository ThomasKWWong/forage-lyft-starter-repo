from abc import ABC

class OctoprimeTire(ABC):
    def __init__(self, array_of_tire_worness):
        self.array_of_tire_worness = array_of_tire_worness

    def needs_service(self):
        sum = 0
        for tire in self.array_of_tire_worness:
            sum = sum + tire
        if sum >= 3:
            return True
        return False