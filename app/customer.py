from app.car import Car


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location_home: list,
                 money: int | float,
                 car: Car,
                 ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location_home = location_home
        self.money = money
        self.car = car

    def buy(self, price: float) -> None:
        self.money -= price
