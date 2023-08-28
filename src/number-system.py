
class Number:
    def __init__(self):
        self.type = Number

        self.decimal = None
        self.binary = None
        self.octal = None
        self.hexadecimal = None

        self.decimal_symbols = {"0": 0, "1": 1, "2": 2, "3": 3,
                                "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        self.binary_symbols = {"0": 0, "1": 1}
        self.octal_symbols = {"0": 0, "1": 1, "2": 2,
                              "3": 3, "4": 4, "5": 5, "6": 6, "7": 7}
        self.hexadecimal_symbols = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                                    "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

    def __repr__(self):
        return f"Decimal:\t{self.decimal}\nBinary:\t\t{self.binary}\nOctal:\t\t{self.octal}\nHexadecimal:\t{self.hexadecimal}"

    def __str__(self):
        if self.type == Decimal:
            return self.decimal
        elif self.type == Binary:
            return self.binary
        elif self.type == Octal:
            return self.octal
        elif self.type == Hexadecimal:
            return self.hexadecimal

    # Convert a decimal number to a different base
    def from_decimal(self, number, symbols):
        result = ""
        number = int(number)
        base = len(symbols)
        while (number > 0):
            remainder = number % base
            number = number // base
            result = list(symbols.keys())[remainder] + result
        return result

    # Convert a different base number to a decimal number
    def to_decimal(self, number, symbols):
        result = 0
        number = list(number)
        base = len(symbols)
        for index in range(len(number)):
            result += int(symbols[number.pop()]) * base ** index
        return str(result)


class Decimal(Number):
    def __init__(Number, number):
        super().__init__()
        Number.type = Decimal
        Number.decimal = number
        Number.binary = Number.from_decimal(number, Number.binary_symbols)
        Number.octal = Number.from_decimal(number, Number.octal_symbols)
        Number.hexadecimal = Number.from_decimal(
            number, Number.hexadecimal_symbols)


class Binary(Number):
    def __init__(Number, number):
        super().__init__()
        Number.type = Binary
        Number.binary = number
        Number.decimal = Number.to_decimal(number, Number.binary_symbols)
        Number.octal = Number.from_decimal(
            Number.decimal, Number.octal_symbols)
        Number.hexadecimal = Number.from_decimal(
            Number.decimal, Number.hexadecimal_symbols)


class Octal(Number):
    def __init__(Number, number):
        super().__init__()
        Number.type = "Octal"
        Number.octal = number
        Number.decimal = Number.to_decimal(number, Number.octal_symbols)
        Number.binary = Number.from_decimal(
            Number.decimal, Number.binary_symbols)
        Number.hexadecimal = Number.from_decimal(
            Number.decimal, Number.hexadecimal_symbols)


class Hexadecimal(Number):
    def __init__(Number, number):
        super().__init__()
        Number.type = "Hexadecimal"
        Number.hexadecimal = number
        Number.decimal = Number.to_decimal(number, Number.hexadecimal_symbols)
        Number.binary = Number.from_decimal(
            Number.decimal, Number.binary_symbols)
        Number.octal = Number.from_decimal(
            Number.decimal, Number.octal_symbols)
