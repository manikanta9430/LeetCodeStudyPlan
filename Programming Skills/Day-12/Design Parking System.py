class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.ntable = {1: big, 2: medium, 3: small}
    def addCar(self, carType: int) -> bool:
        if self.ntable[carType] >0:
            self.ntable[carType] -=1
            return True
        else:
            return False
