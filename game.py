from player import HumanPlayer, ComputerPlayer, Player
from bag import Bag


class Game:
    PLAYER_WIN = 1
    PLAYER_CONTINUE = 0
    PLAYER_LOSE = -1

    def __init__(self):
        self.bag = Bag()
        self.players = []

    # Adding a player to a game
    def add_player(self, player: Player):
        player.state = 0
        self.players.append(player)

    # Print all the cards
    def print_cards(self):
        for num, player in enumerate(self.players):
            print(f'=========== player: {player.name:20} ===========')
            print(player.card)

    # check, if the player wins or loses
    @classmethod
    def check_player_state(cls, player: Player, bag_item, decision):
        if decision == Player.PLAY_CROSS_OUT and bag_item in player.card:
            if len(player.card) == 1:
                return cls.PLAYER_WIN
            else:
                return cls.PLAYER_CONTINUE
        elif decision == Player.PLAY_DO_NOT_CROSS_OUT and bag_item not in player.card:
            return cls.PLAYER_CONTINUE
        else:
            return cls.PLAYER_LOSE

    # asks every players decision and returns
    # the winners (if present) and number of active players
    def make_move(self) -> [[Player], int]:
        bag_item = self.bag.get_one()
        print(f'bag item is: {bag_item}')

        self.print_cards()

        # every player
        for num, player in enumerate(self.players):
            if player.state != self.PLAYER_CONTINUE:
                continue

            # promting the move, updating playes's state
            print(f'{player.name}''s move:')
            decision = player.decide_how_to_play(bag_item)
            player.state = self.check_player_state(player, bag_item, decision)

            # cross out the number on player's bag if necessary
            if decision == Player.PLAY_CROSS_OUT:
                player.card.cross_out(bag_item)

        # returns winners's list and number of active players
        return [player for player in self.players if player.state == self.PLAYER_WIN], \
            len([player for player in self.players if player.state == self.PLAYER_CONTINUE])


def main():
    game = Game()

    # promting to input players
    user_input = 1
    while user_input != 0:
        print('Add player. Type:')
        print('1: Human')
        print('2: Computer')
        print('0: To stop adding players')

        user_input = int(input())

        if user_input == 1: # Human. Asking name and adding to a game
            game.add_player(HumanPlayer(input().strip()))
            print('Added Human player')

        elif user_input == 2:  # Computer. Adding to a game
            game.add_player(ComputerPlayer())
            print('Added Computer player')
        elif user_input == 0:  # Exit
            if len(game.players) > 0:
                print(f'Having {len(game.players)} players')
            else:
                print('No players added, add at lest one player')
                user_input = -1

    # playing while have no winners and have active players
    winners_list, players_left = game.make_move()
    while len(winners_list) == 0 and players_left > 0:
        winners_list, players_left = game.make_move()

    if len(winners_list) > 0: # have winners
        print('Winners: ')
        for winner in winners_list:
            print(winner)
    else:                     # no winners, everybody lost
        print('No winners...')


if __name__ == '__main__':
    main()
