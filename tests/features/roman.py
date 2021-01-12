class RomanNumerals:
    def __init__(self, arg):
        self.arg = arg

    def roman(self):
        int_val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        rom = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        rom_val = ''
        i = 0

        while self.arg > 0:
            for _ in range(self.arg // int_val[i]):
                rom_val += rom[i]
                self.arg -= int_val[i]
            i += 1
        return rom_val


if __name__ == "__main__":
    pass