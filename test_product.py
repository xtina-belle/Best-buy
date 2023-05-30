import pytest

from products import Product


def test_create_product():
    product = Product("Phone", 950.00, 50)

    assert product.name == "Phone"
    assert product.price == 950.00
    assert product.get_quantity() == 50


def test_create_product_with_invalid_name():
    invalid_name = ""

    with pytest.raises(ValueError):
        Product(invalid_name, 50.00, 5)


def test_create_product_with_invalid_price():
    with pytest.raises(ValueError):
        Product("Phone", -950.00, 50)


def test_create_product_with_invalid_quantity():
    with pytest.raises(ValueError):
        Product("Phone", 950.00, -50)


def test_reach_0():
    product = Product("Phone", 950.00, 50)
    product.buy(50)
    assert not product.is_active()


def test_modifies_quantity():
    product = Product("Phone", 950.00, 50)
    product.buy(25)

    assert product.get_quantity() == 25


def test_purchase():
    product = Product("Phone", 950.00, 50)

    assert product.buy(10) == 9500.00


def test_overpurchase():
    product = Product("Phone", 950.00, 50)

    with pytest.raises(ValueError):
        product.buy(60)


pytest.main()