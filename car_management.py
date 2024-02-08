class CarManager:
    all_cars = []
    total_cars = 0
    
    def __init__(self, make, model, year, mileage, services=None):
        CarManager.total_cars += 1
        self._id = CarManager.total_cars
        CarManager.all_cars.append(self)
        self.set_make = make
        self.set_model = model
        self.set_year = year
        self.set_mileage = mileage
        self._services = [] if services is None else services
        
    def __str__(self):
        return f"\nID #{self.get_id}: {self.get_make}, {self.get_model}, {self.get_year}, {self.get_mileage}, {self.get_services}"
    
    def __repr__(self):
        return str(self)
        
    @property
    def get_id(self):
        return self._id
    
    @property
    def get_make(self):
        return self._make
    
    @get_make.setter
    def set_make(self, new_make):
        if isinstance(new_make, str):
            self._make = new_make.capitalize()
        else:
            print('Make must be a string.')
    
    @property
    def get_model(self):
        return self._model
    
    @get_model.setter
    def set_model(self, new_model):
        if isinstance(new_model, str):
            self._model = new_model.capitalize()
        else:
            print('Make must be a string.')
    
    @property
    def get_year(self):
        return self._year
    
    @get_year.setter
    def set_year(self, new_year):
        if isinstance(new_year, int):
            self._year = new_year
        else:
            print('Year must be an integer.')

    @property
    def get_mileage(self):
        return self._mileage
    
    @get_mileage.setter
    def set_mileage(self, new_mileage):
        if isinstance(new_mileage, int):
            self._mileage = new_mileage
        else:
            print('Mileage must be an integer.')

    @property
    def get_services(self):
        return self._services
    
    @get_services.setter
    def set_services(self, new_services):
        self._services.append(new_services)
    
def search_by_id(car_id):
    for car in CarManager.all_cars:
        if car.get_id == car_id:
            return car
    print(f'No car found with ID {car_id}')
    return None

# car1 = CarManager('toyota', 'camry', 2018, 40000, ['oil change', 'tire rotation'])
# car2 = CarManager('ford', 'mustang', 2019, 25000)
# car3 = CarManager('honda', 'civic', 2016, 55000)
# car4 = CarManager('chevrolet', 'silverado', 2020, 20000)
# print('total cars:' , CarManager.total_cars)
# print('all cars:', CarManager.all_cars)
# car1.set_services = ['replaced spark plugs']
# print('all cars:', CarManager.all_cars)
# print(search_by_id(1))