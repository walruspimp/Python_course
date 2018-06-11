import numpy.random as random

class RockPaperScissors:
    """
    Implementation of the game Rock, Paper, Scissors
    """
    def __init__(self):
        self.scissors = {'rock': False, 'paper': True}
        self.rock = {'scissors': True, 'paper': False}
        self.paper = {'scissors': False, 'rock': True}
    
        self.choices = {'scissors': self.scissors, 'rock': self.rock, 'paper': self.paper}
    
        self.answer = None
    
    def begin_game_prompt(self):
        while self.answer not in self.choices:
            self.answer = input("'rock', 'paper', or 'scissors'? ")

    def computer_answer(self):
        self.computer_answer = random.choice(['rock', 'paper', 'scissors'])

    def game_result(self):
        if self.answer == self.computer_answer:
            print('Computer has {} as well!'.format(self.computer_answer))
            print('TIED GAME')
        elif self.choices[self.answer][self.computer_answer]:
            print('Computer has {}'.format(self.computer_answer))
            print('YOU WON')
        else:
            print('Computer has {}'.format(self.computer_answer))
            print('YOU LOST')

    def new_game(self):
        self.new_game = input("Another round? (y/n) ")
        if self.new_game in ['y', 'Y', 'yes', ]:
            RockPaperScissors()

if __name__ == "__main__":
    RockPaperScissors()

