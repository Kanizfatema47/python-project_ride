#Ride Sharing App

from abc import ABC, abstractmethod
from datetime import datetime

class Ride_Sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders =[]
        self.drivers =[]
        self.rides =[]
        
    def add_rider(self, rider):
        self.riders.append(rider)
        
    def add_driver(self, driver):
        self.drivers.append(driver)
    
    def __repr__(self) -> str:
        return(f'{self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}')



class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email
        self.__id = 0
        self.__nid = nid
        self.wallet = 0
        
    @abstractmethod   
    def display_profile(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount) -> None:
        self.current_ride = None
        self.current_location = current_location
        super().__init__(name, email, nid)
        self.wallet = initial_amount
        
    def display_profile(self):
        print(f'Rider:name{self.name} email: {self.email}')

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
            
    def update_location(self, current_location):
        self.current_location = current_location
            
                
    def request_ride(self,ride_sharing,destination):
        if not self.current_ride:
            print('looking for a ride')
            ride_request=Ride_Request(self, destination)
            ride_matcher= Ride_Matching(ride_sharing.drivers)
            ride = ride_matcher.find_driver(ride_request)
            print('got the ride')
            self.current_ride =ride
    def show_current_ride(self):
        print(self.current_ride)
                    
            
class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email, nid) 
        self.current_location = current_location
        self.wallet = 0
         
    def display_profile(self):
        print(f'Driver name:{self.name} and email {self.email}')
        
    def accept_ride(self, ride):
        ride.set_driver(self)
        
class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None
        
    def set_driver(self, driver):
        self.driver = driver
        
    def start_ride(self):
        self.start_time = datetime.now()
        
    def end_ride(self, rider, amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
        
    def __repr__(self) -> str:
        return f'Ride Details: started from:{self.start_location} to {self.end_location}'


class Ride_Request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location
        
        
class Ride_Matching:
    def __init__(self, drivers) -> None:
        self.available_drivers = drivers
    
    def find_driver(self, ride_request):
        if len(self.available_drivers)> 0:
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride
        
class Vehicle(ABC):
    
    #class component:
    
    speed = {
        'car': 50,
        'bike': 60,
        'cng': 15
    }
    
    @abstractmethod
    def start_drive(self):
        pass
    
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = 'available'
        super().__init__()
        
class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
        
    def start_drive(self):
        self.status = 'unavialable'
        

class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
        
    def start_drive(self):
        self.status = 'unavialable'        
        
        
class CNG(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
        
    def start_drive(self):
        self.status = 'unavialable'  
    
        
#check the class integration

niye_jao = Ride_Sharing('Niye Jao')

rahim_rider = Rider('Rahim', 'rahim@gmail.com', 12345, 'mohakhali', 500)
niye_jao.add_rider(rahim_rider)

karim_driver = Driver('Karim', 'karim@gmail.com', 123456, 'gulshan-1')
niye_jao.add_driver(karim_driver)

rahim_rider.request_ride(niye_jao,'Uttara')
rahim_rider.show_current_ride()

print(niye_jao)
   
        

        