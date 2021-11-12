from draft_0 import Die

class DiceList: # [Die1, Die2, Die 3...]
    """Representation of any collection of dice"""
    def __init__(self, colors=None):
        if colors is None:
            colors = []
        self.colors = set(colors)
        self.list = [Die(color) for color in self.colors]

    def get_list(self):
        """Return list of dice"""
        return self.list

    def get_colors(self):
        """Return colors of dice present"""
        return self.colors

    def pop_die(self, color):
        """Removes and returns the die of the given color"""
        if color in self.colors:
            for die in self.list.copy():
                if die.get_color() == color:
                    number = die.get_number()
                    self.remove_die(die)
                    return Die(color, number)
        else:
            print('This die is not present')
            return None

    def get_lower_value_die(self, die):
        """Returns a die with a smaller number than the given die if one exists"""
        for die_i in self.list:
            if die_i.get_value() < die.get_value():
                return die_i
            return None

    def add_die(self, die):
        """Put given die into location"""
        # append die to list
        if die.get_color() in self.colors:
            return
        self.colors.add(die.get_color())
        self.list.append(die)
        return

    def remove_die(self, die):
        """Take given die out of location"""
        if die.get_color() in self.colors:
            self.colors.remove(die.get_color())
            temp = []
            for die_in_list in self.list:
                if die.get_color() == die_in_list.get_color() and die.get_value() == die_in_list.get_value():
                    continue
                temp.append(die_in_list)
            self.list = temp

    def __repr__(self):
        return f"{list(self.list)}"
    def __str__(self):
        return f"{str([str(die)+', ' for die in self.list])}"
