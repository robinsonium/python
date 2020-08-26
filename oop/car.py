import unittest

class Car:
    def __init__(self, make, model, year):
        """ initialize attributes to make a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odomoter_reading = 0
    
    def get_descriptive_name(self):
        """ return a nicely formatted long name"""
        long_name=f"{self.year} {self.make} {self.model}"
        # use .title() to capitalize leading char
        return long_name.title()

    def set_odometer(self,mileage):
        """
        Update odomoter value
        If mileage < current value, error
        """
        if mileage >= self.odomoter_reading:
            self.odomoter_reading=mileage
            return self
        else:
            print("You can't roll back the odomoter!!")
            return False
    
    def get_odometer(self):
        return(self.odomoter_reading)
    
    def add_miles(self,miles):
        """ increment current odomoter value by 'miles' """
        self.odomoter_reading += miles
        return(self)

    

# my_car=Car('chevy','luv',1980)
# my_car.set_odometer(150).add_miles(25)
# print(f"My car is a {my_car.get_descriptive_name()} and it has {my_car.get_odometer()} miles on it")
# my_car.add_miles(50)
# print(f"Now my car has {my_car.get_odometer()} miles")
class TestCar(unittest.TestCase):
    """Tests for the Car class"""
    def test_set_odometer(self):
        my_car=Car('chevy','luv',1980)
        my_car.set_odometer(-100)
        self.assertFalse(my_car.get_odometer())
        my_car.set_odometer(2468)
        self.assertEqual(my_car.get_odometer(),2468)
    def test_descriptive_name(self):
        my_car=Car('chevy','luv',1980)
        self.assertEqual(my_car.get_descriptive_name(),'1980 Chevy Luv')
    def test_add_miles(self):
        my_car=Car('Nissan','Titan',2016)
        my_car.add_miles(1200).add_miles(2000).add_miles(10000)# should be 13200
        self.assertEqual(my_car.get_odometer(),13200)


if __name__ == '__main__':
    unittest.main()