import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self, inp_path):
        root_exp = os.path.splitext(inp_path)
        return root_exp[1]



class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
        self.car_type = 'car'




class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_whl = body_whl

        self.body_length = None
        self.body_width = None
        self.body_height = None
        
        
    def parse_body_whl(self, inp_body_whl):
        if inp_body_whl == '':
            self.body_length = 0
            self.body_width = 0
            self.body_height = 0


    def get_body_volume(self, ):
        pass





    

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'




def get_car_list(name_csv):
    car_list = []

    with open(name_csv) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:







            print(row)






    return car_list

a = get_car_list('prov.csv')
# print(a)



