class Roman:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value + other.value)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value - other.value)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value * other.value)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, Roman):
            return Roman(self.value // other.value)
        else:
            raise TypeError("Unsupported operand type for /")

    @staticmethod
    def from_roman(roman):
            num1 = Roman(10)
            num2 = Roman(5)
            result = num1 + num2
            print(result.value)  # Output: 15

            result = num1 / num2
            print(result.value)  # Output: 2

            decimal_num = Roman.from_roman("XV")
            print(decimal_num)  # Output: 15

            roman_num = Roman.to_roman(15)
            print(roman_num)  # Output: "XV"