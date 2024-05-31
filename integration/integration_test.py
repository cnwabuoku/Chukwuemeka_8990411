import unittest


class Pet:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.health = 5

    def feed(self):
        self.hunger = max(self.hunger - 2, 1)
        self.health = min(self.health + 1, 10)

    def play(self):
        self.happiness = min(self.happiness + 2, 10)
        self.hunger = min(self.hunger + 1, 10)

    def rest(self):
        self.health = min(self.health + 2, 10)
        self.happiness = max(self.happiness - 1, 1)

    def pass_time(self):
        self.hunger = min(self.hunger + 1, 10)
        self.happiness = max(self.happiness - 1, 1)
        self.health = max(self.health - 1, 1)

    def critical_condition(self):
        return self.hunger == 10 or self.happiness == 1 or self.health == 1


class TestPet(unittest.TestCase):

    def setUp(self):
        self.pet = Pet("Cat", "Whiskers")

    def test_play(self):
        self.pet.play()
        self.assertEqual(self.pet.happiness, 7)
        self.assertEqual(self.pet.hunger, 6)

    def test_rest(self):
        self.pet.rest()
        self.assertEqual(self.pet.health, 7)
        self.assertEqual(self.pet.happiness, 1)  # Incorrect expected outcome to make the test fail


if __name__ == "__main__":
    unittest.main()










# import addition
# import multiplication
#import calculator
#def test_integration():
    # Test multiplying the result of adding two numbers with another number
#   assert calculator.multiply(calculator.add(2, 3), 4) == 20



## Unit testing

# def test_addition():
#     assert calculator.add(2, 3) == 5
#
# def test_subtraction():
#     assert calculator.subtract(5, 3) == 2
#
# def test_multiplication():
#     assert calculator.multiply(2, 3) == 6
#
# def test_division():
#     assert calculator.divide(6, 3) == 2
#
# def test_divide_by_zero():
#     try:
#         calculator.divide(6, 0)
#     except ValueError as e:
#         assert str(e) == "Cannot divide by zero"
#     else:
#         assert False, "Expected ValueError"
#
#
#
