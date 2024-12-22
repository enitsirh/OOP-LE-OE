class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
nissan = Car("Nissan", "Blue")
nissan.brand = "Nissan"
print(f" Car1\n {nissan.brand}, {nissan.color}")
nissan.color = "Red"
print(f"\n{nissan.brand}, {nissan.color}")
nissan.brand = "R390 GT1"
nissan.color = "Black"
print(f" Car2\n {nissan.brand}, {nissan.color}")