class ParkingSystem(object):
    d = {}

    def __init__(self, big, medium, small):
        self.d[1] = big
        self.d[2] = medium
        self.d[3] = small

    def addCar(self, carType):
        if self.d[carType] > 0:
            self.d[carType] -= 1
            return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)