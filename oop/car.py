class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odomter_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year),self.make,self.model
        return long_name

    def read_odometer(self):
        print("This car has", str(self.odomter_reading),"miles on it")

    def update_odometer(self,mileage):

        if mileage >= self.odomter_reading:
            self.odomter_reading = mileage
        else:
            print("You can't roll back an odomter")
    def increment_odometer(self,miles):
        self.odomter_reading += miles

car = Car('audi','a4',2016)
print(car.get_descriptive_name())

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a" + str(self.battery_size) + "-kWh battery")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

            message = "This car can go approximately",str(range)
            message += " miles on a full charge."
            print(message)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()