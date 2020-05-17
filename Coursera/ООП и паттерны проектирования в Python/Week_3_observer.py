from abc import ABC, abstractmethod


class Engine:
    pass


class ObservableEngine(Engine):
    """ Heir of Engine class"""
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self,subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    """ Class for realizing ShortNotificationPrinter class and
        FullNotificationPrinter class.
    
    """
    @abstractmethod
    def update(self):
        pass


class ShortNotificationPrinter(AbstractObserver):
    """ This Class can to save set names achievement
        which it get. 

    """
    def __init__(self):
        self.achievements = set()

    def update(self, message):
        self.achievements.add(message['title'])


class FullNotificationPrinter(AbstractObserver):
    """ This Class can to save list achievement
        in order in which it to get them of Engin class.
    """
    def __init__(self):
        self.achievements = list()

    def update(self, message):
        if message not in self.achievements:
            self.achievements.append(message)

def main():
    mess = {"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"}
    short_not = ShortNotificationPrinter()
    full_not = FullNotificationPrinter()
    obser = ObservableEngine()
    obser.subscribe(short_not)
    obser.subscribe(full_not)
    obser.notify(mess)

    print(short_not.achievements, full_not.achievements, sep='\n')


if __name__ == '__main__':
    main()
