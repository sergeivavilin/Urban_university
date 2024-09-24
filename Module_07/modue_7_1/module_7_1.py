class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self._file_name = "products.txt"

    def get_products(self):
        try:
            with open(self._file_name, "r") as file:
                return file.read()
        except FileNotFoundError:
            print("File not found")

    def add(self, *products: Product):
        with open(self._file_name, "a") as file:
            exist_text = self.get_products().split("\n")
            for product in products:
                product_str = str(product).rsplit("\n")[0]
                if product_str not in exist_text:
                    file.write(str(product) + "\n")
                else:
                    print(f"{product_str} уже есть в магазине")


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
