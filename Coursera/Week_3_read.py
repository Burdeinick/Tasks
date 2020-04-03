class FileReader:
    """ The class that reading the path and return the string"""


    def __init__(self, path):
        self.path = path

    def read(self):
        """ This function for reading a files, if the path is wrong return '' """
        try:
            with open(self.path, 'r') as f:
                line = f.read()
                return line

        except FileNotFoundError:
            return ''
            



