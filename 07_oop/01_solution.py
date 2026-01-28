class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel

    def full_name(self):
        return f"{self.brand}{self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


tesla = ElectricCar("Tesla", "Model S", "85kWH")
print(tesla.model)
print(tesla.full_name())


# my_car = Car("Toyota", "Corolla")

# print(my_car.brand)
# print(my_car.model)

# my_new_car = Car("Tata", "Nexon")
# print(my_new_car.brand)
# print(my_new_car.model)

# print(my_car.full_name())
# print(my_new_car.full_name())
