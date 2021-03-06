"""player.py"""
from enum import Enum

from draft_0 import COLORS, Die

ACTIONS = Enum("player_actions", "")
class Board:
    def __init__(self):
        self.pink_list = []
        self.blue_list = []
        self.green_list = []
        
        # Using static matric as value reference - ***DO NOT EDIT***
        self.yellow_score_increments = [3,7,11,15,19,21,22,23,24]
        self.scoring_matrix = [[0, 3, 0, 6],
                               [1, 0, 2, 0],
                               [0, 4, 0, 3],
                               [2, 0, 5, 0],
                               [0, 5, 0, 4]]
        # To edit and track (0=unfilled, 1=circled, 2=exxed)
        self.yellow_dict = {(0,1):0, (0,3):0,
                            (1,0):0, (1,2):0,
                            (2,1):0, (2,3):0,
                            (3,0):0, (3,2):0,
                            (4,1):0, (4,3):0}
    
    # Equivalent to marking on the scoring sheet (die value for now)
    def add_to_list(self, die):
        if (get_color(die) == COLORS.pink):
            self.pink_list.append(get_number(die))
        elif (get_color(die) == COLORS.blue):
            self.blue_list.append(die)
        elif (get_color(die) == COLORS.green):
            self.green_list.append(die)
        elif (get_color(die) == COLORS.yellow):
            
        
class Player:
    """Player class"""
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        
        self.fox_count = 0
        self.reroll_count = 0
        self.putback_count = 0
        self.plus_one_count = 0
        
        self.selected_die_count = 0
        self.board = Board()

    def get_name(self):
        """Returns name of player"""
        return self.name

    def get_reroll_count(self):
        """Returns number of times player may reroll all dice"""
        return self.reroll_count

    def get_putback_count(self):
        """Returns name of player"""
        return self.putback_count

    # SCORING
    def add_yellow_score(self, die):
        Board.add_to_list(self.board, die) 
        
        #TODO: print matrix before asking for selection
        row = input("select row value between 0-4")
        col = input("select col value between 0-3")

        # check if valid selection
        isValidLocation = Die.get_number(die) == self.board.scoring_matrix[row][col]
        isAvailable = self.board.yellow_dict[(row,col)] < 2 #only edit if 0 (unfilled) or 1 (circled)
        if isValidLocation and isAvailable:
            self.board.yellow_dict[(row,col)] += 1 # increment value in dictionary
            num_X = len(list(self.board.yellow_dict.values()))
            self.score += self.board.yellow_score_increments[num_x-1]
            
            filtered_dict = {key:value for key, value in a_dictionary.items() if key > 1}
            rowXCount = BLAAAAAHHHHHHHHHH TODO TODO TOD
        else:
            print("must select valid row/column - try again.")
        
        
                
    def add_black_score(self, die):
        """TODO"""
        raise NotImplementedError
    def add_green_score(self, die):
        """Simulate scoring a green die on a player's scoring mat"""
        Board.add_to_list(self.board, die) #"mark" on scoring sheet
        green_index = len(self.board.green_list) #includes new input

        if (green_index % 2) == 0: #if even numbered index, ready to score
            current_die = self.board.green_list[green_index-1]
            previous_die = self.board.green_list[green_index-2]
            current_die_value = Die.get_number(current_die)
            previous_die_value = Die.get_number(previous_die)

            if green_index == 2:
                self.reroll_count += 1
                diff = (2*previous_die_value)-(2*current_die_value)
                self.score += diff
            elif (green_index==4):
                blue_die_value = input("select blue die value between 1-6")
                self.add_blue_score(Die(COLORS.blue,int(blue_die_value)))
                diff = (2*previous_die_value)-(1*current_die_value)
                self.score += diff
            elif green_index==6:
                diff = (3*previous_die_value)-(3*current_die_value)
                self.score += diff
            elif green_index == 8:
                black_die_value = input("select black die value between 1-6")
                self.add_black_score(Die(COLORS.black,int(black_die_value)))
                diff = (3*previous_die_value)-(2*current_die_value)
                self.score += diff
            elif (green_index==10):
                diff = (3*previous_die_value)-(1*current_die_value)
                self.score += diff
            elif (green_index==12):
                yellow_die_value = input("select yellow die value between 1-6")
                add_yellow_score(self, Die(COLORS.yellow,int(yellow_die_value)))
                diff = (4*previous_die_value)-(1*current_die_value)
                self.score += diff
        else:
            if (green_index == 5):
                self.putback_count += 1
            elif (green_index == 7):
                self.fox_count += 1
            elif (green_index == 9):
                self.plus_one_count += 1
            elif (green_index == 11):
                pink_die_value = input("select pink die value between 1-6")
                add_pink_score(self, Die(COLORS.pink,int(pink_die_value)))

    def add_blue_score(self, die):
        """Simulate scoring a blue die on a player's scoring mat"""
        add_to_list(self.board, die) #"mark" on scoring sheet
        blue_index = len(self.board.blue_list) #includes new input
        self.score += blue_index
        if (blue_index == 2) or (blue_index == 10):
            self.putback_count += 1
        elif (blue_index == 3):
            yellow_die_value = input("select yellow die value between 1-6")
            add_yellow_score(self, Die(COLORS.yellow,int(yellow_die_value)))
        elif (blue_index == 5):
            self.plus_one_count += 1
        elif (blue_index == 6):
            self.reroll_count += 1
        elif (blue_index == 7):
            pink_die_value = input("select pink die value between 1-6")
            add_pink_score(self, Die(COLORS.pink,int(pink_die_value)))
        elif (blue_index == 9):
            self.fox_count += 1
        elif (blue_index == 12):
            green_die_value = input("select green die value between 1-6")
            add_green_score(self, Die(COLORS.green,int(green_die_value)))
    
    def add_pink_score(self, die):
        """Simulate scoring a pink die on a player's scoring mat"""
        add_to_list(self.board, die)
        
        die_value = Die.get_number(die)
        self.score += die_value
        
        pink_index = len(self.board.pink_list)
        if pink_index > 2:
            if (pink_index == 3 and die_value > 1) or (pink_index == 10 and die_value > 3):
                self.reroll_count += 1
                
            elif pink_index == 4 and die_value > 2:
                self.putback_count += 1
                
            elif pink_index == 5 and die_value > 3:
                self.plus_one_count += 1
                
            elif pink_index == 6 and die_value > 4:
                green_die_value = input("select green die value between 1-6")
                add_green_score(self, Die(COLORS.green,int(green_die_value)))
                
            elif (pink_index == 7 and die_value > 5) or (pink_index == 12 and die_value > 5):
                yellow_die_value = input("select yellow die value between 1-6")
                add_yellow_score(self, Die(COLORS.yellow,int(yellow_die_value)))
                
            elif pink_index == 8 and die_value > 1:
                self.fox_count += 1
                
            elif pink_index == 9 and die_value > 2:
                black_die_value = input("select black die value between 1-6")
                add_black_score(self, Die(COLORS.black,int(black_die_value)))
                
            elif  pink_index == 11 and die_value > 4:
                blue_die_value = input("select blue die value between 1-6")
                add_blue_score(self, Die(COLORS.blue,int(blue_die_value)))

