class Car:
    #Class varibale
    total_cars=0 # to keep track of total cars

    def __init__(self,make,model,year,price):
        # instance variables
        self.make = make
        self.model = model
        self.year = year
        self.price = price

        Car.total_cars += 1 # incrementing class variable eevery time

    #instance method
    def car_info(self):
        print(F"Car Info: {self.make} {self.model} {self.year} {self.price}")

    #class method to get the no of cars
    @classmethod
    def get_total_cars(cls):
        print(f"Total cars created: {cls.total_cars}")
    
    #static varibale to calculate car depreciation 
    @staticmethod
    def calculate_depreciation(price,year):
        depreciation_rate=0.15
        depreciation_value=price*((1-depreciation_rate)**year)
        return depreciation_value
    
car1=Car("Toyota","Camry",2020,25000)
car2=Car("Honda","Civic",2022,23000)

car1.car_info()
car2.car_info()


Car.get_total_cars()

depreciated_value=Car.calculate_depreciation(25000,3) #static method is not depedent on class or instance variable
print(f"Depreciated value after 3 years: ${depreciated_value:.2f}")
