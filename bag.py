from random import shuffle


# A class for bag with boxes
class Bag:
    def __init__(self):
        # shuffling numbers from 1 to 90
        numbers = list(range(1, 91))
        shuffle(numbers)

        self.numbers = numbers

    # returns the next number in a bag
    def get_one(self):
        if len(self.numbers) > 0:
            return self.numbers.pop()

    def __str__(self):
        # number, that left in a bag
        return " ".join(map(str, self.numbers[:-1]))
