"""
https://cs.wikipedia.org/wiki/Komplexn%C3%AD_%C4%8D%C3%ADslo

Definujte třídu ComplexNumber reprezentující komplexní číslo
a definujte následující metody:
- __init__ (konstruktor)
- __eq__ (rovnost)
- __lt__ (<)
- __gt__ (>)
- __repr__
- __str__
- properties (gettery a settery)
- add (sčítání)
- subtract (odečítání)
- multiply (násobení)
- divide (dělení)
- conjugate (číslo komplexně sdružené)
- absolute_value (absolutní hodnota)

A vše řádně otestujte.
"""


class ComplexNumber:
    __re = 0
    __img = 0

    def __init__(self, real_part=0.0, img_part=0.0):
        self.re = real_part
        self.img = img_part

    def __eq__(self, other):
        return self.re == other.re and self.img == other.img

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    @property
    def re(self):
        return self.__re

    @re.setter
    def re(self, real_part):
        if isinstance(real_part, int) or isinstance(real_part, float):
            self.__re = real_part
        else:
            raise Exception

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img_part):
        if isinstance(img_part, int) or isinstance(img_part, float):
            self.__img = img_part
        else:
            raise Exception
