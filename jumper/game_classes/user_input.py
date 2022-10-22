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
        # set_input(self.player_input)
        return self.player_input
    
    def set_input(self):
        while True:
            user_input = input('Guess a letter (a-z): ').lower()
            if len(user_input) > 1:
                print(f"One letter only Thank you!")
            elif len(user_input) == 0:
                print(f"Provide at least one letter Thank you!")
            else:
                self.player_input = user_input
                break
        return self.player_input