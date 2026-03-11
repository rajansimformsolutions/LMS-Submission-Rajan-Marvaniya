class Vehicle:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model 
        self.year = year
        self.__price = 0.0

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price
    
    def display_info(self):
        print("vehicle details:")
        print("brand:",self.brand)
        print("model:",self.model)
        print("year:",self.year)
        print("price:",self.__price)

car = Vehicle("toyota", "corolla", 2026)
car.set_price(3000000)
print("vehicle price:",car.get_price())
car.display_info()