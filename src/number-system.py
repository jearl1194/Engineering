
class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        print(f"{self.value}")

class Decimal(Number):
    def __init__(self):
        self.type = "Decimal"

class Binary(Number):
    def __init__(self):
        self.type = "Binary"

class Octal(Number):
    def __init__(self):
        self.type = "Octal"

class Hexadecimal(Number):
    def __init__(self):
        self.type = "Hexadecimal"


n = Decimal("10")
print("n")