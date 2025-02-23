class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


car1 = Car("Nissan", "Kawasaki", 2016)
car2 = Car("Ford", "Ranger", 2003)

print("Car 1 Details:")
car1.display_info()

print("\nCar 2 Details:")
car2.display_info()