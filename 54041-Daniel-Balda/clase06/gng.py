from random import randint
class Game():
    def __init__(self):
        self.is_playing = True

    def finish(self):
        self.is_playing = False

class HumanAgainstComputerGame(Game):
    
    def __init__(self):
        self.think_number()

    def think_number(self):
        self.secret_number = randint(1,100)

    def play(self,human_number):
        if self.secret_number > human_number:
            return "My number is bigger"
        elif self.secret_number < human_number:
            return "My number is smaller"
        else:
            self.finish()
            return "You win"
class ComputerAgainstHumanGame(Game):
    
    def __init__(self):
        self.cota_min = 1
        self.cota_max = 100

    def input_text(self):
        pass
    def play(self,answer):
        pass
