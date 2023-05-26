from abc import ABC

class CarriganTire(ABC):
    def __init__(self, array_of_tire_worness):
        self.array_of_tire_worness = array_of_tire_worness

    def needs_service(self):
        for tire in self.array_of_tire_worness:
            if tire >= .9:
                return True
        return False