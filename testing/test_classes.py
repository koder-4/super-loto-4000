from pytest import fixture

from bag import Bag
from card import Card


@fixture(scope='function')
def new_bag() -> Bag:
    return Bag()


@fixture(scope='function')
def new_card() -> Card:
    return Card()


# class for testing Bag
class TestBag:
    # test __init__ - bag created correctly
    def test_bag_created(self, new_bag) -> None:
        assert len(new_bag.numbers) == 90
        assert set(new_bag.numbers) == set(range(1, 91))
        assert list(range(1, 91)) != new_bag.numbers

    def test_get_one(self, new_bag):
        numbers = []
        for i in range(1, 91):
            numbers.append(new_bag.get_one())

            # check that numbers left correctly
            assert len(new_bag.numbers) == (90 - i)

        # check all numbers, got from the bag:
        assert len(numbers) == 90
        assert set(numbers) == set(range(1, 91))


class TestCard:
    # test the representation of number for pretty print
    def test_num_repr(self, new_card):
        assert new_card.num_repr(1) == ' 1'
        assert new_card.num_repr(2) == ' 2'
        assert new_card.num_repr(None) == '  '
        assert new_card.num_repr(new_card.NUMBER_CROSSED_OUT) == '--'

    # test the Card created correctly:
    def test_card_created(self, new_card) -> None:
        # check, that have 3 rows:
        assert len(new_card.rows) == 3
        for i in range(3):
            # 10 cells in each row
            assert len(new_card.rows[i]) == 10
            # no numbers, that crossed_out
            assert new_card.NUMBER_CROSSED_OUT not in new_card.rows[i]
            # 5 numbers in each row
            assert len([col for col in new_card.rows[0] if col is not None]) == 5

        # have 15 unique numbers on card
        assert len(set([x for row in new_card.rows for x in row if x is not None])) == 15

    def test_numbers_left(self, new_card):
        numbers_left = new_card.numbers_left()

        # check, that have all numbers in the Card
        for number in numbers_left:
            assert any([number in row for row in new_card.rows])

    def test_cross_out(self, new_card):
        for num in new_card.numbers_left():
            # check, that num disapeared from card after cross_out
            assert num in new_card.numbers_left()
            new_card.cross_out(num)
            assert num not in new_card.numbers_left()
