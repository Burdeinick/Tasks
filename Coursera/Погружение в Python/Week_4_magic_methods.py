import os.path
import tempfile
from random import choice
from string import ascii_letters


class File:
    """ This class is the interface for work with some files """

    def __init__(self, file):
        self.path_to_file_tmp = os.path.join(tempfile.gettempdir(), file)
        self.count = 0
        if not os.path.exists(self.path_to_file_tmp):
            with open(self.path_to_file_tmp, 'w') as f:
                f.write('')

    def __str__(self):
        return str(os.path.abspath(self.path_to_file_tmp))

    def read(self):
        with open(self.path_to_file_tmp, 'r') as f:
            f_read = f.read()
            return str(f_read)

    def write(self, str_for_write):
        with open(self.path_to_file_tmp, 'w') as f:
            f.write(str_for_write)

    def __add__(self, obj_2):
        data_new_obj = self.read() + obj_2.read()
        sum_file_obj = os.path.join(
            tempfile.gettempdir(),
            ''.join(choice(ascii_letters) for _ in range(12)))
        with open(sum_file_obj, 'w') as f:
            f.write(data_new_obj)
        return File(sum_file_obj)

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path_to_file_tmp, 'r') as f:
            line = f.readlines()
            if self.count <= (len(line) - 1):
                x = self.count
                self.count += 1
                return line[x]
            else:
                raise StopIteration
