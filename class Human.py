class Human:
    default_name = "Иван"
    default_age = 30

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Покупатель: {self.name}, {self.age} лет")

    @classmethod
    def default_info(cls):
        print(cls.default_name, cls.default_age)

    @staticmethod
    def pay_house(money, price):
        if money >= price:
            print(f"Вы можете купить дом, и у вас останется {money - price} рублей")
        else:
            print("Вы не можете его купить, необходимо больше золота")

    def buy_house(self, money=0, price=1000000):
        print("Дом стоит", price, "рублей")
        return self.pay_house(money, price)

