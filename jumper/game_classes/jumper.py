class Jumper:
    """
    responsiblity:
        -store the array for the display of the jumper figure and adjust the array according to player letter choice

    attributes:
        -steve: array of the pieces of the parachute

    methods:
        -update: removes a piece of the parachute from the array and returns the new smaller array to the attrubute steve.
        -get: returns the steve array
    """
    def __init__(self):


        self.index = 0
        self.steve = self.parachute[self.index]
        self.parachute = [
                    
"""
            ___  
           /___\ 
           \   / 
            \ /               
             0   
            /|\  
            / \  
          
           ^^^^^^^""",

"""                 
           /___\ 
           \   / 
            \ /  
             0   
            /|\  
            / \  
                    
           ^^^^^^^""",
                   
"""          
           \   / 
            \ /  
             0   
            /|\  
            / \  
          ^^^^^^^""",

"""          
            \ /  
             0   
            /|\  
            / \  
          ^^^^^^^""",

"""
             x   
            /|\  
            / \  
          
          ^^^^^^^"""]

    def update(self):
        if self.index <= self.parachute.length:
            self.index = self.index +1
            self.steve = self.parachute[self.index]

    def get(self):
        return self.steve
