import csv
import os


class CarBase:

    def __init__(self, brand=None, photo_file_name=None, carrying=None):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying =  float(carrying) if carrying != None else carrying

    def get_photo_file_ext(self):
        _, root_exp = os.path.splitext(self.photo_file_name)
        if root_exp in ('.jpg', '.jpeg', '.png', '.gif'):
            return root_exp
        else: 
            return False



class Car(CarBase):

    def __init__(self, brand=None, photo_file_name=None, carrying=None, passenger_seats_count=None):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count) if passenger_seats_count != None else carrying
        self.car_type = 'car'


class Truck(CarBase):

    def __init__(self, brand=None, photo_file_name=None, carrying=None, body_whl=None):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_whl = body_whl 

        if body_whl:
            self.body_whl = body_whl.split('x')

        if (self.body_whl == None) or (len(self.body_whl) != 3):
            self.body_length = 0.0
            self.body_width = 0.0
            self.body_height = 0.0

        else:
            self.body_length, self.body_width, self.body_height = map(float,self.body_whl)

    def get_body_volume(self):
        return float(self.body_length) * float(self.body_width) * float(self.body_height)


class SpecMachine(CarBase):

    def __init__(self, brand=None, photo_file_name=None, carrying=None, extra=None):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'

def get_car_list(name_csv):
    car_list = []
    with open(name_csv) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row_list in reader:
            try:
                if row_list[0] != '':
                    if row_list[0] == Car().car_type:
                        if (row_list[1] != '') and (row_list[2] != '') and (row_list[5] != ''):
                            obj = Car(brand=row_list[1], photo_file_name=row_list[3], carrying=row_list[5], passenger_seats_count=row_list[2])
                            if obj.get_photo_file_ext():
                                car_list.append(obj)

                    elif row_list[0] == Truck().car_type:
                        if (row_list[1] != '') and (row_list[5] != ''):
                            obj = Truck(brand=row_list[1], photo_file_name=row_list[3], carrying=row_list[5], body_whl= row_list[4])
                            if obj.get_photo_file_ext():
                                car_list.append(obj)
                                
                    elif row_list[0] == SpecMachine().car_type:
                        if (row_list[1] != '') and (row_list[5] != '') and (row_list[6] != ''):
                            obj = SpecMachine(brand=row_list[1], photo_file_name=row_list[3], carrying=row_list[5], extra= row_list[6])
                            if obj.get_photo_file_ext():
                                car_list.append(obj)
                                    
            except IndexError:
               pass

    return car_list
