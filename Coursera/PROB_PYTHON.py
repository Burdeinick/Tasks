# import os

# path = 'f.jpeg'

# root_exp = os.path.splitext(path)

# print(root_exp[1])

# lis = []


# try:
#     print(lis[0])
    

# except IndexError:
#     pass


# print('dctbhnyn')    

class Cri:
    tyu = '1'
    def __setattr__(self, name_atrib, value):
        print(f'Создается атрибут {name_atrib} = {value}')


a = Cri()
a.typ = '2'
print(a.tyu)