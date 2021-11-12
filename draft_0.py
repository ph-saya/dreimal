"""Representation of a game"""
import random

from enum import Enum

from dice_list import DiceList

COLORS = Enum("colors", "pink green yellow blue white black")


class Board:
    def __init__(self):
        self.pink_list = []
        self.blue_list = []
        self.green_list = []
        # TODO: add others

    # Equivalent to marking on the scoring sheet (die value for now)
    def add_to_list(self, die):
        if get_color(die) == COLORS.pink:
            self.pink_list.append(get_number(die))
        elif get_color(die) == COLORS.blue:
            self.blue_list.append(die)
        elif get_color(die) == COLORS.green:
            self.green_list.append(die)


class Game:
    """Representation of a game"""

    def __init__(self, player_list):
        if len(player_list) > 4 or len(player_list) < 1:
            raise Exception(
                f"Player count is wrong! {len(player_list)} players were input. Please input between 1 and 4 players."
            )
        self.is_over = False

        # run chwazi = generate ordered list
        random.shuffle(player_list)
        self.player_order = player_list
        print(
            f"Order of player is: {[player.get_name() for player in self.player_order]}"
        )

        self.active_player_number = 0
        self.active_player = self.player_order[self.active_player_number]
        print(f"First player is: {self.active_player}")

        self.platter = DiceList()
        self.selected_die_list = DiceList()
        self.field = DiceList()

    def get_is_over(self):
        """Return whether the game has concluded"""
        return self.is_over

    def reroll_check(self, active_player):
        """Verify whether a reroll should be performed"""
        while get_reroll_count(active_player) > 0:
            print(
                f"{get_name(active_player)} you have {get_reroll_count(active_player)} rerolls left"
            )
            player_reroll = input("Want to reroll? y/n")
            if player_reroll == "y":
                active_player.reroll_count -= 1
                reroll = dielist(get_colors(self.field))
                self.field = reroll
                print(self.field)
            elif player_reroll == "n":
                break
            else:
                pass

    def putback_check(self, active_player):
        """Verify whether a die should be put back into the field"""
        while get_putback_count(active_player) > 0 and len(get_list(self.platter)) > 0:
            print(
                f"{get_name(active_player)} you have {get_putback_count(active_player)} putbacks left"
            )
            player_putback = input("Want to putback? y/n")
            if player_putback == "y":
                active_player.putback_count -= 1
                # player selects which die to putback from platter
                # select die
                has_selected = False
                while not has_selected:
                    selected_die_string = input("Which die would you like to select?")
                    # TODO: Check that color exists in self.field first
                    # TODO: cast str selected_die into enum value
                    selected_die_enum_value = COLORS.pink
                    chosen_die = self.platter.pop_die(selected_die_enum_value)
                    if chosen_die is not None:
                        self.field.add_die(chosen_die)
                        has_selected = True
                    else:
                        continue
            elif player_putback == "n":
                break
            else:
                pass

    def plus_one_check(self, player):
        """Verify whether a die should be counted again"""
        while get_plus_one_count(active_player) > 0:
            print(
                f"{get_name(active_player)} you have {get_plus_one_count(active_player)} +1s left."
            )
            player_plus_one = input("Do you want to use a +1? y/n")
            if player_plust_one == "y":
                active_player.plus_one_count -= 1
                # player selects which die to use a plus one
                # select die
                has_selected = False
                while not has_selected:
                    print(self.platter)
                    print(self.selected_die_list)
                    selected_die_string = input("Which die would you like to select?")
                    # TODO: Check that color exists in self.field first
                    # TODO: cast str selected_die into enum value
                    selected_die_enum_value = COLORS.pink
                    # TODO: find where the selected die is
                    # TODO: check platter
                    # TODO: check selected_die_list
                    # TODO: check whether selection is valid with their player board
                    has_selected = True
            elif player_plus_one == "n":
                break
            else:
                pass

    def do_platter_select(self, player):
        raise NotImplemented

    # TODO: decide whether or not to just use the self.active_player instead of passing it in as an argument
    def take_turn(self, active_player):
        """A single active player's turn"""
        print(f"Starting {get_name(active_player)}'s turn!")
        while len(get_list(selected_die_list)) < 4 and len(get_list(self.field)) > 0:
            # start of first turn, player rolls to generate self.field.
            new_roll = dielist(COLORS)
            self.field = new_roll
            print(self.field)

            # after each roll, a player may: 1) select die, 2) reroll until player.rerollcount = 0
            reroll_check(self, active_player)

            # select die
            has_selected = False

            while not has_selected:
                selected_die_string = input("Which die would you like to select?")
                # TODO: Check that color exists in self.field first
                # TODO: cast str selected_die into enum value
                selected_die_enum_value = COLORS.pink
                chosen_die = pop_die(self.field, selected_die_enum_value)
                if chosen_die is not None:
                    add_die(self.selected_die_list, chosen_die)
                    has_selected = True
                else:
                    continue

            while (
                not get_lower_value_die(self.field, chosen_die) is None
            ):  # if is not lowest value die
                lower_value_die = self.field.get_lower_value_die(
                    chosen_die
                )  # move all lower val die to platter
                self.field.remove_die(lower_value_die)
                self.platter.add_die(lower_value_die)

        # after each selection, a player may put back any die that have been moved to the platter if able.
        putback_check(self, active_player)

        # Passive players select die from center
        for player in self.player_order:
            if player != active_player:
                do_platter_select(player)

        # Passive players to check plus_one_check
        for player in self.player_order:
            plus_one_check(self, player)

        # Return dice to field
        self.selected_die_list = DiceList()
        self.platter = DiceList()

        # Increment the active player
        self.active_player_number += 1
        self.active_player = self.player_order[
            self.active_player_number % len(self.player_order)
        ]


if __name__ == "__main__":
    print("Begin game")
    # paul = Player("Paul")
    # nayeon = Player("Nayeon")
    # game = Game([paul, nayeon])
    # while not is_over(game):
    #    game.is_over = True
#  next_action(game)
# a_single_roll_of_all_colors = DiceList([list(COLORS)])
# reroll_pink = DiceList([COLORS.pink])
