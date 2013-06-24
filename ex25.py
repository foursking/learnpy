def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

#print break_words('abc')

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

#print sort_words("sen")

def print_first_word(words):
    """Prints the first word after poppint it off."""
    word = words.pop(0)
    return word

#word = ['a','b','c']
#print print_first_word(word)

def print_last_word(words):
    """Print the last word after poppint it off."""
    word = words.pop(-1)
    return word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
#    return words
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one."""
    word = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)




