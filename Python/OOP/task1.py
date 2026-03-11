#TASK 1

class vehicle:
    def __init__(self,brand,model,year,price):
       self.brand = brand
       self.model = model 
       self.year = year 
       self.price = price

    def display_info(self):
        print("vehicle details:")
        print("brand:",self.brand)
        print("model:",self.model)
        print("year:",self.year)
        print("price:",self.price)


car = vehicle("toyota", "corolla", 2026, 2500000)
car.display_info()   