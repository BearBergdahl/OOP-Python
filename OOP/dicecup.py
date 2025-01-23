import dice

class DiceCup():
    dice_sum = 0
    dice_list = []
    
    def __str__(self):
        if self.dice_sum:
            return f"The sum of the dice rolls are {self.dice_sum}"
        else:
            return "No dices rolled"
    
    def roll(self):
        for a_dice in self.dice_list:
            self.dice_sum = self.dice_sum+a_dice.roll()
            print(a_dice)
        return self.dice_sum
    
    def add_dice(self, a_dice):
        self.dice_list.append(a_dice)


a_cup = DiceCup()

for i in range(5):
    a_cup.add_dice(dice.Dice(i+4))

print(a_cup.roll())

print(a_cup)
