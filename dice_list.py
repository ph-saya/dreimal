from draft_0 import Die

class DiceList: # [Die1, Die2, Die 3...]
    def __init__(self, colors=[]):
        self.colors = set(colors)
        self.list = [Die(color) for color in self.list_colors]
 
    def get_list():
        return self.list
  
    def get_colors():
        return self.colors

    def pop_die(self, color):
        if color in self.colors:
            for die in self.list.copy():
                if get_color(die) == color:
                    number = get_number(die)
                    remove_die(self, die)
                    return Die(color, number)
        else:
            print('This die is not present')
            return None
  
    def get_lower_value_die(self, die):
        for die_i in self.list:
            if get_value(die_i) < get_value(die):
                return die_i
            else:
                return None
    
    def add_die(self, die):
        #append die to list
        if get_color(die) in self.colors:
            return
        self.color.append(get_color(die))
        self.list.append(die)
        return
    
    def remove_die(self, die):
        if get_color(die) in self.colors:
            self.colors.remove(get_color(die))
            temp = []
            for die_in_list in self.list:
                if get_color(die) == get_color(die_in_list) and get_value(die) == get_value(die_in_list):
                    continue
                else:
                    temp.append(die_in_list)

            self.list = temp
  
    def __repr__(self):
        return f"{[die for die in self.list]}"
  
    def __str__(self):
        return f"{str([str(die)+', ' for die in self.list])}"
