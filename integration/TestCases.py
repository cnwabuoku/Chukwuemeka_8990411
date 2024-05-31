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

    def test_initial_status(self):
        self.assertEqual(self.pet.hunger, 5)
        self.assertEqual(self.pet.happiness, 5)
        self.assertEqual(self.pet.health, 5)

    def test_feed(self):
        self.pet.feed()
        self.assertEqual(self.pet.hunger, 3)
        self.assertEqual(self.pet.health, 6)

    def test_play(self):
        self.pet.play()
        self.assertEqual(self.pet.happiness, 7)
        self.assertEqual(self.pet.hunger, 6)

    def test_rest(self):
        self.pet.rest()
        self.assertEqual(self.pet.health, 7)
        self.assertEqual(self.pet.happiness, 4)

    def test_pass_time(self):
        self.pet.pass_time()
        self.assertEqual(self.pet.hunger, 6)
        self.assertEqual(self.pet.happiness, 4)
        self.assertEqual(self.pet.health, 4)

    def test_critical_condition(self):
        self.pet.hunger = 10
        self.assertTrue(self.pet.critical_condition())
        self.pet.hunger = 5
        self.pet.happiness = 1
        self.assertTrue(self.pet.critical_condition())
        self.pet.happiness = 5
        self.pet.health = 1
        self.assertTrue(self.pet.critical_condition())

    def test_pass(self):
        # This test is designed to pass
        self.pet.feed()
        self.assertEqual(self.pet.hunger, 3)  # Expected outcome
        self.assertEqual(self.pet.health, 6)  # Expected outcome

    def test_fail(self):
        # This test is designed to fail
        self.pet.feed()
        self.assertEqual(self.pet.hunger, 10)  # Incorrect expected outcome
        self.assertEqual(self.pet.health, 1)  # Incorrect expected outcome


if __name__ == "__main__":
    unittest.main()
