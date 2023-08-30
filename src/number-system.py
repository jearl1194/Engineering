
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
    def __init__(Number, number):
        super().__init__()
        Number.type = Decimal
        Number.decimal = int(number)
        Number.binary = bin(number)
        Number.octal = oct(number)
        Number.hexadecimal = hex(number)


class Binary(Number):
    def __init__(Number, number):
        super().__init__()
        Number.type = Binary
        Number.decimal = int(number, 2)
        Number.binary = bin(Number.decimal)
        Number.octal = oct(Number.decimal)
        Number.hexadecimal = hex(Number.decimal)


class Octal(Number):
    def __init__(Number, number):
        super().__init__()
        Number.type = Octal
        Number.decimal = int(number, 8)
        Number.octal = oct(Number.decimal)
        Number.binary = bin(Number.decimal)
        Number.hexadecimal = hex(Number.decimal)


class Hexadecimal(Number):
    def __init__(Number, number):
        super().__init__()
        Number.type = "Hexadecimal"
        Number.decimal = int(number, 16)
        Number.hexadecimal = hex(Number.decimal)
        Number.binary = bin(Number.decimal)
        Number.octal = oct(Number.decimal)
