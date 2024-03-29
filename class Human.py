from typing import Any


class Human:
    default_name = "Иван"
    default_age = 30

    def __init__(self, money, house, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house
        self.get_numberhouses()

    def get_numberhouses(self):
        if self.__house in "yesYESYes":
            self.__numberhouses = 1
            return self.__numberhouses
        else:
            self.__numberhouses = 0
            return self.__numberhouses

    def private_info(self):
        print(
            f"Покупатель: {self.name}, {self.age} лет, общее количество денег = {self.__money}, наличие дома: {self.__house}, количество домов: {self.__numberhouses}"
        )

    def info(self):
        print(f"Покупатель: {self.name}, {self.age} лет")

    @classmethod
    def default_info(cls):
        print(cls.default_name, cls.default_age)

    @staticmethod
    def pay_house(money, price):
        if money >= price:
            print(f"Вы купили дом, и у вас осталось {money - price} рублей")
        else:
            print("Вы не можете его купить, необходимо больше золота")

    def buy_house(self, price=1000000):
        print("Дом стоит", price, "рублей")
        return self.pay_house(self.__money, price)

    def private_house(self):
        self.__numberhouses += 1

    def __setattr__(self, key, value):
        if type(value) not in (str, int):
            print("Недопустимое значение свойства объекта!")
            return False
        else:
            return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        print("Такого свойства у объекта и класса нет!")
        return False

    def __delattr__(self, item):
        print("Вы удалили свойство объекта:", item)
        return object.__delattr__(self, item)

    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money):
        self.__money = money
    @money.deleter
    def money(self):
        del self.__money    
    @property
    def house(self):
        return self.__house
    @house.setter
    def house(self, house):
        self.__house = house
    @house.deleter
    def house(self):
        del self.__house
        


print(
    "Введите необходимую информацию: количество денег, наличие дома, имя, возраст, приватные данные будут засекречены"
)
Nikita = Human(10000000, "no", "Никита", 25)
Nikita.info()
Nikita.private_info()
Nikita.buy_house()
Nikita.private_house()
Nikita.private_info()

