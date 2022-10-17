class Word:
    """
    responsibility:
        -to store a list of words and randomly pick one for game play, to turn chosen word into an array of the letters in the word

    attributes:
        -word list: an array storing the words that are possible options for game play
        -word: the word chosen for game play
        -letters: an array containing the letters in the word

    methods:
        -pick word: arguments: self. randomly chooses a word from the array based on index. store in word attribute
        -letters: arguments: self. Splits word into a array where each item is a single letter of the word in the correct order of the word. stores in letters attribute
    """