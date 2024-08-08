

class Person:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def display_info(self):
        print(f"Name: {self._name}, Email: {self._email}")


class Customer(Person):
    def __init__(self, name, email, address):
        super().__init__(name, email)
        self._address = address

    def get_address(self):
        return self._address

    def display_info(self):
        super().display_info()
        print(f"Address: {self._address}")


class Product:
    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    def get_product_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_stock(self):
        return self._stock

    def update_stock(self, quantity):
        if quantity > self._stock:
            print("Not enough stock available.")
            return
        self._stock -= quantity

    def display_info(self):
        print(f"Product ID: {self._product_id}, Name: {self._name}, Price: {self._price}, Stock: {self._stock}")


class Order:
    def __init__(self, order_id, customer, product, quantity):
        self._order_id = order_id
        self._customer = customer
        self._product = product
        self._quantity = quantity

        if self._quantity > self._product.get_stock():
            print("Invalid order: quantity exceeds stock.")
            return
        self._product.update_stock(self._quantity)

    def get_order_id(self):
        return self._order_id

    def get_customer(self):
        return self._customer

    def get_product(self):
        return self._product

    def get_quantity(self):
        return self._quantity

    def display_info(self):
        print(f"Order ID: {self._order_id}")
        self._customer.display_info()
        self._product.display_info()
        print(f"Quantity: {self._quantity}")


class Payment:
    def __init__(self, payment_id, order, amount, method):
        self._payment_id = payment_id
        self._order = order
        self._amount = amount
        self._method = method

    def get_payment_id(self):
        return self._payment_id

    def get_order(self):
        return self._order

    def get_amount(self):
        return self._amount

    def get_method(self):
        return self._method

    def display_info(self):
        print(f"Payment ID: {self._payment_id}, Amount: {self._amount}, Method: {self._method}")
        self._order.display_info()



customer1 = Customer("Alice", "alice@example.com", "123 Main St")
product1 = Product(101, "Laptop", 1200.00, 10)
customer1.display_info()
product1.display_info()

order1 = Order(1, customer1, product1, 2)
order1.display_info()

payment1 = Payment(1, order1, 2400.00, "Credit Card")
payment1.display_info()
product1.display_info()
