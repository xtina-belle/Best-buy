from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract class for promotions"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """gets 2 parameters - a product instance and a quantity,
        and returns the discounted price after promotion was applied."""


class SecondHalfPrice(Promotion):
    """Represents a promotion Second for half price"""
    def apply_promotion(self, product, quantity) -> float:
        """gets a product instance and a quantity
        :returns: float, the discounted price: each second with half price"""
        discount = (product.price / 2) * (quantity // 2)
        return product.price * quantity - discount


class ThirdOneFree(Promotion):
    """Represents a promotion Every third for free"""
    def apply_promotion(self, product, quantity) -> float:
        """gets a product instance and a quantity
        :returns: float, the discounted price: each third for free."""
        discount = (quantity // 3) * product.price
        return product.price * quantity - discount


class PercentDiscount(Promotion):
    """Represent a Percent discount promotion"""
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        """gets a product instance and a quantity
        :returns: float, the discounted price: -percent% of all."""
        discount = (100 - self.percent) / 100
        return product.price * quantity * discount
