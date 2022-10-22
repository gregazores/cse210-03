class Output:
    """
    responsibilty:
        -display the jumper figure
    attributes:
        -
    methods:
        -display letter spaces (getLetters) -- prints out the letter array
        -display jumper figure (getSteve) --
        prints our the steve parachute array from jumper class
        -display ground (getGround) -- print the person figure and "^^^^^^^" under the jumper
    """
    def __init__(self):
        pass

    def getLetters(self, blanks):
        print(*blanks, sep=" ")

    def getSteve(self, array, index):
        pic = array[index]
        print(pic)


    