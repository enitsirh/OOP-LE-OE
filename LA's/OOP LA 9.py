class Car:
    def __init__(self, brand):
        self.brand = brand
    def __srt__(self):
        return f"{self.brand} is a car object"

car = Car("Ferrari")
print(car)
del car
print(car)