from random import sample, shuffle


# A class for card
class Card:
    NUMBER_CROSSED_OUT = -1

    @classmethod
    # represents the number on a card as printable
    def num_repr(cls, num: int) -> str:
        if num is None:                         # Empty
            return '  '
        elif num == cls.NUMBER_CROSSED_OUT:     # Crossed out number
            return '--'
        else:
            return f'{num:2}'       # Not crossed out

    def __init__(self):
        # Shuffling numbers from 1 to 90
        possible_numbers = list(range(1, 91))
        shuffle(possible_numbers)

        self.rows = []

        for _ in range(3):      # 3 rows on a card
            row = [None] * 10       # 10 columns in a row

            # get 5 numbers for a row
            numbers_in_row = possible_numbers[:5]
            numbers_in_row.sort()
            del possible_numbers[:5]

            # get 5 positions for numbers above
            row_indexes = sample(range(1, 10), k=5)
            row_indexes.sort()

            # putting numbers to a card row
            for row_number_index, row_position in enumerate(row_indexes):
                row[row_position] = numbers_in_row[row_number_index]

            # adding row to a card
            self.rows.append(row)

    # printable card, table format
    def __str__(self):
        return '\n'.join(
            [' '.join(map(self.num_repr, row)) for row in self.rows]
        )

    # numbers, that are on the card and not crossed out
    def numbers_left(self):
        return [x for row in self.rows for x in row if x != self.NUMBER_CROSSED_OUT and x is not None]

    # check, if number is on a card and not crossed out
    def __contains__(self, item: int) -> bool:
        return item in self.numbers_left()

    # returns amount of numbers, that are not crossed out
    def __len__(self) -> int:
        return len(self.numbers_left())

    # crosses out the number on a card (if exists), nothing otherwise
    def cross_out(self, num: int):
        for row in self.rows:
            if num in row:
                row[row.index(num)] = self.NUMBER_CROSSED_OUT
