

class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""  #


class EventGet:
    """ This class creates the event for
        getting data of the appropriate type.

    """
    def __init__(self, kind):
        self.name_type = self.inp_type(kind)  # It for know,
        # which class must processing a event

    def inp_type(self, kind):
        """ For assignment 'name_type' value:
            'int' or
            'float' or
            'str'

        """
        if issubclass(kind, int):
            return 'int'

        if issubclass(kind, float):
            return 'float'

        if issubclass(kind, str):
            return 'str'


class EventSet:
    """ This class creates a 'type(<value>)' field change event """
    def __init__(self, value):
        self.name = 'EventSet'
        self.value = value
        self.name_type = self.inp_type(value)  # It for know,
        # which class must processing a event

    def inp_type(self, value):
        """ For assignment 'name_type' value:
            'int' or
            'float' or
            'str'

        """
        if isinstance(value, int):
            return 'int'

        if isinstance(value, float):
            return 'float'

        if isinstance(value, str):
            return 'str'


class NullHandler:
    """ Passes the event to the next class
        in the chain, if there is one.

    """
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, char, event):
        if self.__successor is not None:
            return self.__successor.handle(char, event)


class IntHandler(NullHandler):
    """ Processing the events with 'int" type """
    def handle(self, char, event):
        if event.__class__.__name__ == 'EventGet':
            if event.name_type == 'int':
                return char.integer_field
            else:
                return super().handle(char, event)

        if event.__class__.__name__ == 'EventSet':
            if event.name_type == 'int':
                char.integer_field = event.value
            else:
                return super().handle(char, event)


class FloatHandler(NullHandler):
    """ Processing the events with 'float" type """
    def handle(self, char, event):
        if event.__class__.__name__ == 'EventGet':
            if event.name_type == 'float':
                return char.float_field
            else:
                return super().handle(char, event)

        if event.__class__.__name__ == 'EventSet':
            if event.name_type == 'float':
                char.float_field = event.value
            else:
                return super().handle(char, event)


class StrHandler(NullHandler):
    """ Processing the events with 'str" type """
    def handle(self, char, event):
        if event.__class__.__name__ == 'EventGet':
            if event.name_type == 'str':
                return char.string_field
            else:
                return super().handle(char, event)

        if event.__class__.__name__ == 'EventSet':
            if event.name_type == 'str':
                char.string_field = event.value
            else:
                return super().handle(char, event)


if __name__ == '__main__':
    obj = SomeObject()
    obj.integer_field = 42
    obj.float_field = 3.14
    obj.string_field = "some text"

    chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
    print(chain.handle(obj, EventGet(int)))

    print(chain.handle(obj, EventGet(float)))

    print(chain.handle(obj, EventGet(str)))

    chain.handle(obj, EventSet(100))
    print(chain.handle(obj, EventGet(int)))

    chain.handle(obj, EventSet(0.5))
    print(chain.handle(obj, EventGet(float)))

    chain.handle(obj, EventSet('new text'))
    print(chain.handle(obj, EventGet(str)))
