# # Print out fizzbuzz with a loop
# i = 1
# while i <= 100:
#     if i % 15 == 0:
#         print("Fizzbuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)
#     i += 1

# Fizzbuzz as a class with OOP
class Fizzbuzz():
    def __init__(self):
        self.fizz_nums = 3  # divisor for fizz numbers
        self.buzz_nums = 5  # divisor for buzz numbers
        self.fizzbuzz_nums = 15  # divisor for fizzbuzz numbers

    def fizzbuzz_individual(self, num):
        if num % 15 == 0:
            return "Fizzbuzz"  # fizzbuzz if multiple of 15
        elif num % 5 == 0:
            return "Buzz"  # buzz if multiple of 5
        elif num % 3 == 0:
            return "Fizz"  # fizz if multiple of 3
        else:
            return num  # return number if neither multiple of 3 or 5

    def fizzbuzz_one_to_hundred(self):
        i = 1
        while i <= 100:
            print(Fizzbuzz().fizzbuzz_individual(i))  # need a reference to the class to call this method
            i += 1

# create an object of Fizzbuzz class
fb = Fizzbuzz()

# return the output of a single number
print(fb.fizzbuzz_individual(2))

# print fizzbuzz for 1-100
fb.fizzbuzz_one_to_hundred()
