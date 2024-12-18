"""Exercise 5

Write a class that will represent the magazine.
Storage capacity (float value reflecting cubic meters) is defined by the constructor.
Create a class that will reflect the product.
The product volume is defined by the constructor.
The magazine will have a method "add", which will take a Product object as its argument
and return the remaining free space, or -1 if you can't add a new item since it won't fit in the warehouse anymore.

Use fixture to prepare a set of products that flow into warehouses every month
and create tests that will check whether warehouses respond correctly to adding more products.
Accuracy should be implemented to two decimal places.
"""


class Product:
    __name = None
    __volume = None

    def __init__(self, name: str, volume: float):
        self.name = name
        self.volume = volume

    def __repr__(self):
        return f"Product(name={self.name}, volume={self.volume})"

    def __str__(self):
        return f"Product '{self.name}' with volume: {self.volume}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_):
        self.__name = name_

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        if volume <= 0:
            raise ValueError
        self.__volume = volume


class Magazine:
    __capacity = None
    __products = []

    def __init__(self, _capacity):
        self.capacity = _capacity
        self.__products = []

    def __repr__(self):
        return f"Magazine(capacity={self.capacity})"

    def __str__(self):
        return (f"Magazine with capacity: {self.capacity} "
                f"has {len(self.__products)} products in warehouse.")

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, _capacity):
        if _capacity <= 0:
            raise ValueError
        self.__capacity = _capacity

    def add(self, product):
        total_volume = sum([product.volume for product in self.__products])
        free_space = self.capacity - total_volume
        if product.volume <= free_space:
            self.__products.append(product)
            return self.capacity - total_volume - product.volume
        return -1


if __name__ == '__main__':
    magazine = Magazine(100)
    print(magazine)
    product1 = Product("Item 1", 12.89)
    print(product1)
    magazine.add(product1)
    print(magazine)
    magazine.add(product1)
    print(magazine)
