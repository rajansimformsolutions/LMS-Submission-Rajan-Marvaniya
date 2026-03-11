class vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"brand: {self.brand}, model: {self.model}, year: {self.year}, price: {self.price}")

    def calculate_discount(self, *args):
        if len(args) == 1:
            discount = self.price * args[0]/100
            return self.price - discount
        elif len(args) == 2:
            discount = self.price * args[0] / 100
            additional_discount = args[1]
            return self.price - discount - additional_discount
        else:
            return self.price
car = vehicle("toyota", "corola", 2026, 2500000.0)
car.display_info()

price_after_discount = car.calculate_discount(10)
print("price after 10% discount:", price_after_discount)

price_after_total_discount = car.calculate_discount(10,500)
print("price after 10% + $500 discount:",price_after_total_discount)