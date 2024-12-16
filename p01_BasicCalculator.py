class BasicCalculator:

    def add(self, num1, num2):
        if ((isinstance(num1, int) or
             isinstance(num1, float)) and
                (isinstance(num2, int) or
                 (isinstance(num2, float)))):
            return num1 + num2
        return None

    def subtract(self, num1, num2):
        if ((isinstance(num1, int) or
             isinstance(num1, float)) and
                (isinstance(num2, int) or
                 (isinstance(num2, float)))):
            return num1 - num2
        return None

    def multiply(self, num1, num2):
        if ((isinstance(num1, int) or
             isinstance(num1, float)) and
                (isinstance(num2, int) or
                 (isinstance(num2, float)))):
            return num1 * num2
        return None

    """def divide(self, num1, num2):
        if ((isinstance(num1, int) or
             isinstance(num1, float)) and
                (isinstance(num2, int) or
                 (isinstance(num2, float))) and
                num2 != 0):
            return num1 / num2
        return None"""

    def divide(self, num1, num2):
        if ((isinstance(num1, int) or
             isinstance(num1, float)) and
                (isinstance(num2, int) or
                 (isinstance(num2, float)))):
            try:
                return num1 / num2
            except:
                return None
        return None

    def divide2(self, num1, num2):
        if ((isinstance(num1, int) or
             isinstance(num1, float)) and
                (isinstance(num2, int) or
                 (isinstance(num2, float)))):
                return num1 / num2
        return None


if __name__ == '__main__':
    basic_calculator = BasicCalculator()
    num1 = float(input("Zadejte první číslo: "))
    op = input("Zadejte požadovanou operaci [+, -, *, /]: ")
    num2 = float(input("Zadejte druhé číslo: "))
    if op == '+':
        print(f"{num1} {op} {num2} = {basic_calculator.add(num1, num2)}")
    if op == '-':
        print(f"{num1} {op} {num2} = {basic_calculator.subtract(num1, num2)}")
    if op == '*':
        print(f"{num1} {op} {num2} = {basic_calculator.multiply(num1, num2)}")
    if op == '/':
        print(f"{num1} {op} {num2} = {basic_calculator.divide(num1, num2)}")
