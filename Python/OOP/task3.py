class vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print("brand:",self.brand)
        print("model",self.model)
        print("year",self.year)

class car(vehicle):
    def __init__(self, brand, model, year,number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        print("brand:",self.brand)
        print("model:",self.model)
        print("year:",self.year)
        print("number_of_doors:",self.number_of_doors)

my_car = car("toyota", "corolla", 2026, 4)
my_car.display_info()