
class Critter(object):
    """" Virtual pet"""
    def __init__(self, name, hunger=1, boredom=1):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.boredom + self.hunger
        if unhappiness < 5:
            m = 'прекрасно'
        elif 5 <= unhappiness <= 9:
            m = 'неплохо'
        elif 10 <= unhappiness <= 12:
            m = 'не сказать чтобы хорошо'
        elif unhappiness > 12:
            m = 'ужасно'
            
        return m

    def talk(self):
        print(f'Меня зовут {self.name} и сейчас я чувствую себя {self.mood}')
        self.__pass_time()

    def eat(self, food=4):
        print('Ммм... Спасибо что кормишь меня!')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print('Уиии!Мне нравиться с тобой играть!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input('Как вы назовете свою зверюшку?\n')
    crit = Critter(crit_name)

    choise = None
    while choise != '0':
        print \
        (f"""
        Моя зверушка
        0 - Выйти
        1 - Узнать о самочувствии
        2 - Покормить зверька
        3 - Поиграть со зверьком
        """)
        choise = input('Ваш выбор:')
        print()

        if choise == '0':
            print('До свидания!')
        elif choise == "1":
            crit.talk()
        elif choise == "2":
            crit.eat()
        elif choise == "3":
            crit.play()
        else:
            print(f'Извините, но пункта {choise} пока не существует, но мы над этим работем =)')

main()
print('\n\nНажмите Enter чтобы выйти.')
