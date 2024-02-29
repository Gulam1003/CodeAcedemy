class fract():
    def __init__(self, x, y):
        self.num = x
        self.den = y

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        return f"{self.num * other.den + other.num * self.den}/{self.den * other.den}"


if __name__ == "__main__":
    fractio1 = fract(4, 5)
    fractio2 = fract(6, 8)

    print(fractio1 + fractio2)
