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
    def get_input():
        set_input(player_input)
        return player_input
    
    def set_input(self):
        self.player_input = input('Guess a letter (a-z): ')
        return self.player_input