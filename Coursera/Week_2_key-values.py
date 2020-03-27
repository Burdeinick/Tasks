import os
import argparse
import tempfile
import json


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
def seek_file():
    """Return 
    - if path - Tru
    - if path - False 

    """

    return os.path.exists(storage_path)

def creat_file(bol):
     """If the file - "storage.data" not exist - then to create it. """

    if not bol:
        with open(storage_path, 'w') as f:
            f.write('{}')
    return True

def pars_data():
    """Readind the meaning"""
    parser = argparse.ArgumentParser(description='Parsing keys and values')
    parser.add_argument('--key', action="store", dest="key", type=str)
    parser.add_argument('--val', action="store", dest="val", type=str)
    args = parser.parse_args()
    return (args.key, args.val)

def add_or_get(arg):
    """ This function solve:
    - add new key and value,
    - add to key other - new value, doesn't changing older,
    - show values of key (if entered only key) 
    """
    data = {}
    if arg[1] is None:       
        with open(storage_path, 'r') as f:
            file_f = f.read()
            data = json.loads(file_f)       
            if arg[0] in data:
                print(*data[arg[0]], sep=', ')
            else:
                print(None)

    elif arg[0] and arg[1]:
        with open(storage_path, 'r') as f:
            file_f = f.read()
            data = json.loads(file_f)

            if arg[0] in data: 
                with open(storage_path, 'w') as fil:
                    data[arg[0]].append(arg[1])
                    fil.write(json.dumps(data))
            else:
                with open(storage_path, 'w') as f:
                    data.setdefault(arg[0], [arg[1]])
                    f.write(json.dumps(data))


def main():
    a = seek_file()
    b = creat_file(a)

    if b:
        c = pars_data()
        d = add_or_get(c)

main()

