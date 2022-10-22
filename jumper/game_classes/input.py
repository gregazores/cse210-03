class Input:
    """
    responsibility:
        -gather and store the player's inputs

    attributes:
        -input: the player's input

    methods:
        -get: returns the player's input as a string 
        -set: sets the input attribute 
    """
    def __init__(self):
        self.player_input = ''
    
    def get_input(self):
        set_input(self.player_input)
        return self.player_input
    
    def set_input(self):
        self.player_input = input('Guess a letter (a-z): ')
        return self.player_input