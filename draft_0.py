import random

from enum import Enum

from dice_list import DiceList
from player import Player, ACTIONS

COLORS = Enum("colors", "pink green yellow blue white black")


class Game:
    def __init(self, playerList):
        if len(playerList) > 4 or len(playerList) < 1:     
            raise Exception(f"Player count is wrong! {len(playerList)} players were input. Please input between 1 and 4 players.")
        self.is_over = False   

        #run chwazi = generate ordered list
        self.player_order = random.shuffle(playerList) 
        print(f"Order of player is: {[get_name(player) for player in self.player_order]}")

        self.active_player_number = 0
        self.active_player = self.player_order[self.active_player_number]
        print(f"First player is: {self.active_player}")

        self.platter = DiceList()
        self.selected_die_list = DiceList()
        self.field = DiceList()
    
    def is_over(self):
        return self.is_over
  
    def reroll_check(self, active_player):
        while get_reroll_count(active_player) > 0:
	    print(f"{get_name(active_player)} you have {get_reroll_count(active_player)} rerolls left") 
            player_reroll = input("Want to reroll? y/n")
            if player_reroll == 'y':
                active_player.reroll_count -= 1
                reroll = dielist(get_colors(self.field))
                self.field = reroll
                print(self.field)
            elif player_reroll == 'n':
                break
            else:
                pass

    def putback_check(self, active_player):
        while get_putback_count(active_player) > 0 and len(get_list(self.platter)) > 0:
            print(f"{get_name(active_player)} you have {get_putback_count(active_player)} putbacks left")
    		player_putback = input("Want to putback? y/n")
            if player_putback == 'y':
                active_player.putback_count -= 1
            # player selects which die to putback from platter
            # select die
            has_selected = False
            while not has_selected:
                selected_die_string = input("Which die would you like to select?")
                # TODO: Check that color exists in self.field first
                # TODO: cast str selected_die into enum value
                selected_die_enum_value = COLORS.pink
                chosen_die = pop_die(self.platter, selected_die_enum_value)
                if chosen_die is not None:
                    add_die(self.field, chosen_die)
                    has_selected = True
                else:
                    continue
        elif player_reroll == 'n':
            break
        else:
            pass
  
    def plus_one_check(self, player):
        while get_plus_one_count(active_player) > 0:
            print(f"{get_name(active_player)} you have {get_plus_one_count(active_player)} +1s left.")
            player_plus_one = input("Do you want to use a +1? y/n")
            if player_plust_one == 'y':
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
            elif player_plus_one == 'n':
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

            while not get_lower_value_die(self.field, chosen_die) is None: # if is not lowest value die
                lower_value_die = get_lower_value_die(self.field, chosen_die) # move all lower val die to platter
                remove_die(self.field, lower_value_die)
                add_die(self.platter, lower_value_die)

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
        self.active_player = self.player_order[self.active_player_number % len(self.player_order)]  

class Die:
    def __init__(self, color, number=None):
		# TODO validate color
		self.color = color
		self.number = random.randint(1,7) if number is None else number
        
	def get_number(self):
        return self.number
  
    def get_color(self):
        return self.color
  
    def __repr__(self):
        return f"{self.color}: {self.number}"
  
    def __str__(self):
        return f"{self.color}: {self.number}"

if __name__ == "__main__":
    paul = Player('Paul')
    nayeon = Player('Nayeon')
	game = Game([paul, nayeon])
    while not is_over(game):
        game.is_over = True
  #  next_action(game)
# a_single_roll_of_all_colors = DiceList([list(COLORS)])
# reroll_pink = DiceList([COLORS.pink])
