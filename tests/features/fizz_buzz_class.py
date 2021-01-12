class FizzBuzz:
    def __init__(self, number):
        self.number = number

    def game(self):
        if (int(self.number) % 15) == 0:
            return "FizzBuzz"
        elif int(self.number) % 3 == 0:
            return "Fizz"
        elif int(self.number) % 5 == 0:
            return "Buzz"
        else:
            raise Exception("Error in FizzBuzz")

    def is_Fizz(self):
        if self.number != "Fizz":
            return str(self.number) + ' is not Fizz!'
        return self.number

    def is_Buzz(self):
        if self.number != "Buzz":
            return str(self.number) + ' is not Buzz!'
        return self.number
