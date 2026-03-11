class vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print("vehicle brand:", self.brand)
        print("vehicle model:", self.model)
        print("year:",self.year)

class car(vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        print("car brand:", self.brand)
        print("car model:", self.model)
        print("year:", self.year)
        print("number_of_doors:", self.number_of_doors)

class bike(vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def display_info(self):
        print("bike brand:", self.brand)
        print("bike model:", self.model)
        print("year:", self.year)
        print("this is a two - wheeler bike.")

v = vehicle("Generic", "ModelX", 2020)
c = car("Toyota", "Corolla", 2022, 4)
b = bike("Yamaha", "R15", 2023)    
 
for object in (v, c, b):
    object.display_info()
    print()