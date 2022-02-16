import os
import random
from envparse import env

class Casino:
    def __init__(self):
        self.__cash = int(os.environ.get('MY_MONEY'))
        while int(self.__cash) > 0:
            self.__slot = random.randint(1, 30)
            print(self.__slot)
            self.__bet = int(input('сколько хотите поставить?: '))
            if self.__bet > self.__cash:
                print('у вас не хватает денег!!!')
            else:
                self.__choice = int(input('Выберите слот: '))
                if self.__slot == self.__choice:
                    self.__cash += self.__bet
                    print(f'ты выиграл \nтвой твой выигрыш: {self.__cash}')
                    if self.__slot == self.__choice:
                        ans = input('Введите yes для продолжение введите no для выхода: ')
                        if ans == 'yes':
                            continue
                        if ans == 'no':
                            break
                else:
                    self.__cash -= self.__bet
                    print(f'вы проиграли \nу вас осталось: {self.__cash} денег')
                    if self.__slot != self.__choice:
                        ans = input('Введите yes для продолжение введите no для выхода: ')
                        if ans == 'yes':
                            continue
                        if ans == 'no':
                            break

    @property
    def slot(self):
        return self.__slot

    @slot.setter
    def slot(self, value):
        self.__slot = value


env.read_envfile('settings.env')
winner = Casino()