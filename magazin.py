class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} ₸"


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} себетке қосылды.")

    def remove_product(self, product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                self.products.remove(product)
                print(f"{product.name} себеттен өшірілді.")
                return

        print("Мұндай тауар себетте жоқ.")

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_cart(self):
        if not self.products:
            print("Себет бос.")
            return

        print("\nСебеттегі тауарлар:")
        for product in self.products:
            print(product)

        print(f"Жалпы сома: {self.total_price()} ₸")


class Customer:
    def __init__(self, name, discount_limit, discount_percent):
        self.name = name
        self.cart = Cart()
        self.discount_limit = discount_limit
        self.discount_percent = discount_percent

    def final_price(self):
        total = self.cart.total_price()

        if total >= self.discount_limit:
            discount = total * self.discount_percent / 100
            return total - discount

        return total

    def show_order(self):
        print(f"\nСатып алушы: {self.name}")
        self.cart.show_cart()

        total = self.cart.total_price()

        if total >= self.discount_limit:
            discount = total * self.discount_percent / 100
            print(f"Жеңілдік: {self.discount_percent}%")
            print(f"Жеңілдік сомасы: {discount:.2f} ₸")

        print(f"Төленетін сома: {self.final_price():.2f} ₸")


product1 = Product("Ноутбук", 350000)
product2 = Product("Құлаққап", 25000)
product3 = Product("Тінтуір", 12000)
product4 = Product("Пернетақта", 30000)

customer = Customer("Оразгүл", 300000, 10)

customer.cart.add_product(product1)
customer.cart.add_product(product2)
customer.cart.add_product(product3)
customer.cart.add_product(product4)

customer.show_order()

print("\nТауарды себеттен өшіру:")
customer.cart.remove_product("Тінтуір")

customer.show_order()