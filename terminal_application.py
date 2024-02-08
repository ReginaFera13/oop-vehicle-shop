from car_management import CarManager, search_by_id

MENU = [
    '--- WELCOME ---',
    '1. Add a car',
    '2. View all cars',
    '3. View total number of cars',
    '4. See a car\'s details',
    '5. Service a car',
    '6. Update mileage',
    '7. Quit'
]

def terminal_application():
    menu_selection = 0
    while menu_selection < 7:
        for item in MENU:
            print(item)
    
        if menu_selection == 0:
            menu_selection = int(input('Enter menu number: '))
    
        if menu_selection == 1:
            make = input('Enter the vehichle make: ')
            # print(make)
            model = input('Enter the vehichle model: ')
            # print(model)
            year = int(input('Enter the vehichle year: '))
            # print(year)
            mileage = int(input('Enter the vehichle mileage: '))
            # print(mileage)
            services = list(input('Enter the service already completed on the vehicle: '))
            # print(services)
            new_car = CarManager(make, model, year, mileage, services)
            print(new_car)
            menu_selection = 0
        
        if menu_selection == 2:
            print('all cars:', CarManager.all_cars)
            menu_selection = 0
        
        if menu_selection == 3:
            print('total cars:' , CarManager.total_cars)
            menu_selection = 0
        
        if menu_selection == 4:
            car_id = int(input('Enter the car ID you\'d like to view: '))
            car = search_by_id(car_id)
            if car is not None:
                print(car)
            menu_selection = 0
            
        if menu_selection == 5:
            car_id = int(input('Enter the car ID you\'d like to service: '))
            car = search_by_id(car_id)
            if car is not None:
                services = input('Enter the services you performed, separated by commas: ')
                setattr(car, 'set_services', services)
            menu_selection = 0
        
        if menu_selection == 6:
            car_id = int(input('Enter the car ID you\'d like to update the mileage of: '))
            car = search_by_id(car_id)
            if car is not None:
                mileage = int(input('Enter the updated mileage: '))
                setattr(car, 'set_mileage', mileage)
            menu_selection = 0
        
        if menu_selection == 7:
            return 'Application Quit'

terminal_application()