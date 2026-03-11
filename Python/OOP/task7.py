class vehicle:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print("brand:", self.brand)
        print("model", self.model)
        print("year:", self.year)
        print("price:", self.price)

    def save_to_file(self):
        filename = f"{self.brand}_{self.model}.txt"

        with open(filename, "w") as file:
            file.write(f"Brand: {self.brand}\n")
            file.write(f"Model: {self.model}\n")
            file.write(f"Year: {self.year}\n")
            file.write(f"Price: {self.price}\n")
        print("vehicle details saved to", filename)

car = vehicle("toyota", "corolla", 2026, 2500000)
car.save_to_file()