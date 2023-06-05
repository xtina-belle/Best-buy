from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    def apply_promotion(self, product, quantity) -> float:
        pass


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        discount = (product.price / 2) * (quantity // 2)
        return product.price * quantity - discount


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        discount = (quantity // 3) * product.price
        return product.price * quantity - discount


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        discount = (100 - self.percent) / 100
        return product.price * quantity * discount
