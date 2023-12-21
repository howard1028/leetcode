class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        
    def addCar(self, carType: int) -> bool:
        parking_lot = [self.big , self.medium , self.small]
        print(parking_lot)

        if parking_lot[carType - 1] > 0 and carType >= 1 and carType <= 3:
            parking_lot[carType - 1] -= 1
            if carType == 1:
                self.big -= 1
            elif carType == 2:
                self.medium -= 1
            elif carType == 3:
                self.small -= 1
            return True
            
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)