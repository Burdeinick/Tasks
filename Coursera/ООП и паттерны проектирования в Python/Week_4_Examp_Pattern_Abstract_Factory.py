class DishFaktory:

    @classmethod
    def create_dish(cls, name):
        return cls.Dish(name)

    @classmethod
    def create_sous(cls):
        return cls.Sous()

    @classmethod
    def create_garnir(cls):
        return cls.Garnir()


class VegetarianDish(DishFaktory):
    class Dish:
        def __init__(self, name):
            self.name = name
            self.sous = None
            self.garnir = None

        def add_sous(self, sous):
            self.sous = sous

        def add_garnir(self, garnir):
            self.garnir = garnir

        def pour_sous(self):
            print(f'The Vegetarian dish has {self.sous.pour_sous()}')
            # self.sous.pour_sous()

        def put_garnir(self):
            print(f'The Vegetarian dish has {self.garnir.put_garnir()}')
            # self.garnir.put_garnir()

    class Sous:
        def pour_sous(self):
            return 'ketchup'

    class Garnir:
        def put_garnir(self):
            return 'rice'


def cr_dish(factor):
    dish = factor.create_dish('Kari')

    sous = factor.create_sous()
    garnir = factor.create_garnir()

    dish.add_sous(sous)
    dish.add_garnir(garnir)

    return dish


dish_1 = cr_dish(VegetarianDish)
dish_1.pour_sous()
dish_1.put_garnir()
