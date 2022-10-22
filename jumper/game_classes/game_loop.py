from game_classes.output import Output
from game_classes.input import Input
from game_classes.word import Word
from game_classes.jumper import Jumper

class Game_loop:
    """The main game play loop.
    
        responsibility: to control the sequence of game play.

        attributes:
            -output: an instance of the the output class
            -input: an instance of the input class
            -word: an instance of the word class
            -jumper: an instance of the jumper class
        
    """
    def __init__(self):
        """
        constructs new game loop

        args: self (Game_loop): an instance of Game_loop.
        """
        self.word = Word()
        self.jumper = Jumper()
        self.input = Input()
        self.output = Output()

    def start_game(self):
        blanks = []
        the_wordArray = self.word.get_letters()
        for i in the_wordArray:
            blanks.append("_")
        while (len(self.jumper.steve) > 0):
            self.output.getLetters(blanks)
            self.output.getSteve(self.jumper)
            self.output.getGround()
            self.input.set()
            if self.input.get() in the_wordArray:
                #I discovered that using self.word.get_letters() directly will
                #result in an infinite while loop since it will reset the array of letters
                #in self.word.get_letters() instead of turning every instance of the letter to zero
                #so I created a variable the_wordArray that we could use.
                while self.input.get() in the_wordArray:
                    x = the_wordArray.index(self.input.get())
                    blanks[x] = self.input.get()
                    the_wordArray[x] = 0
            else:
                self.jumper.update()
        print("Thanks for playing")