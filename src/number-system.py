
class Number:
    def __init__(self):
        self.type = Number
        self.decimal = None
        self.binary = None
        self.octal = None
        self.hexadecimal = None

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


class Decimal(Number):
    def __init__(self, number):
        Number.type = Decimal
        Number.decimal = number
        Number.binary = self._binary()
        Number.octal = self._octal()
        Number.hexadecimal = self._hexadecimal()

    # Convert number to a different base
    def convert(self, symbols):
        """Convert a number to a different base by providing the symbols to use. The base will be computed from the number of symbols.

        >>> convert(("0", "1", "2", "3"), 4)
        """
        result = ""
        base = len(symbols)
        number = int(Number.decimal)
        while (number > 0):
            remainder = number % base
            number = number // base
            result = symbols[remainder] + result
        return result

    # Convert number to binary
    def _binary(self):
        symbols = ("0", "1")
        return self.convert(symbols)

    # Convert number to octal
    def _octal(self):
        symbols = ("0", "1", "2", "3", "4", "5", "6", "7")
        return self.convert(symbols)

    # Convert number to hexadecimal
    def _hexadecimal(self):
        symbols = ("0", "1", "2", "3", "4", "5", "6", "7",
                   "8", "9", "A", "B", "C", "D", "E", "F")
        return self.convert(symbols)


class Binary(Number):
    def __init__(self, number):
        self.type = "Binary"
        Number.binary = number


class Octal(Number):
    def __init__(self, number):
        self.type = "Octal"
        Number.octal = number


class Hexadecimal(Number):
    def __init__(self, number):
        self.type = "Hexadecimal"
        Number.hexadecimal = number
