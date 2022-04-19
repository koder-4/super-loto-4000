from card import Card
from abc import ABC, abstractmethod


# Abstract class for player
class Player(ABC):
    PLAY_CROSS_OUT = 1
    PLAY_DO_NOT_CROSS_OUT = 0

    def __init__(self, name: str):
        self.name = name
        self.card = Card()

# Must have a decision method
    @abstractmethod
    def decide_how_to_play(self, num: int) -> int:
        pass


# Class for Computer player
class ComputerPlayer(Player):
    COMPUTER_PLAYER_NUM = 1

    def __init__(self):
        super().__init__(f'computer #{self.COMPUTER_PLAYER_NUM}')
        self.__class__.COMPUTER_PLAYER_NUM += 1

    def decide_how_to_play(self, num: int) -> int:
        # decide to cross out if the num is on card
        return self.PLAY_CROSS_OUT if num in self.card else self.PLAY_DO_NOT_CROSS_OUT

    def __str__(self):
        return self.name


# Class for Human player
class HumanPlayer(Player):
    def decide_how_to_play(self, num: int) -> int:
        print('Enter your move:')
        print('0: do not cross out the number')
        print('1: cross out the number')

        # decide to cross out due to user input
        return self.PLAY_CROSS_OUT if int(input()) == 1 else self.PLAY_DO_NOT_CROSS_OUT
