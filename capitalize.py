"""
This program is used to capitalize the beginning of EVERY WORD in a string(capitalizeFirst), or to
capitalize all the letters in a string(capitalizeAll)
It also can make every letter a lowercase(lowercaseAll)
"""
newString = []

capitals = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lowers = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

dict_capitalize = {
    lowers[0]:capitals[0], lowers[1]:capitals[1], lowers[2]:capitals[2], lowers[3]:capitals[3], lowers[4]:capitals[4], lowers[5]:capitals[5], lowers[6]:capitals[6], lowers[7]:capitals[7], lowers[8]:capitals[8], lowers[9]:capitals[9], lowers[10]:capitals[10], lowers[11]:capitals[11], lowers[12]:capitals[12], lowers[13]:capitals[13], lowers[14]:capitals[14], lowers[15]:capitals[15], lowers[16]:capitals[16], lowers[17]:capitals[17], lowers[18]:capitals[18], lowers[19]:capitals[19], lowers[20]:capitals[20], lowers[21]:capitals[21], lowers[22]:capitals[22], lowers[23]:capitals[23]
    } 
# same as: {"a":"A"}

dict_lowcase = {
    capitals[0]:lowers[0], capitals[1]:lowers[1], capitals[2]:lowers[2], capitals[3]:lowers[3], capitals[4]:lowers[4], capitals[5]:lowers[5], capitals[6]:lowers[6], capitals[7]:lowers[7], capitals[8]:lowers[8], capitals[9]:lowers[9], capitals[10]:lowers[10], capitals[11]:lowers[11], capitals[12]:lowers[12], capitals[13]:lowers[13], capitals[14]:lowers[14], capitals[15]:lowers[15], capitals[16]:lowers[16], capitals[17]:lowers[17], capitals[18]:lowers[18], capitals[19]:lowers[19], capitals[20]:lowers[20], capitals[21]:lowers[21], capitals[22]:lowers[22], capitals[23]:lowers[23]
    } 
# same as: {"A":"a"}


def changeToCap(letter, word):
    """
    (string,string) -> string
    Takes in a letter and the word that the letter comes from. It capitalizes the letter and adds it to the first position in the word.
    """

    word = word[1:]
     # Grab the capital letter from the dictionary, rather than doing a huge if/elif statement to get the capital letter.
     # the .get() method is set to return the first letter if the first letter in the word is not a regular letter in the English alphabet
    new_letter = dict_capitalize.get(letter, letter)
    word = new_letter + word

    return word


def changeToUpper(letter):
    """
    (string) -> string
    Grabs the accompaning uppercase letter from the uppercase dictionary.
    """

    return dict_capitalize.get(letter,letter)


def changeToLower(letter):
    """
    (string) -> string
    Grabs the accompaning lowercase letter from the lowercase dictionary. 
    """
    
    return dict_lowcase.get(letter,letter)


def capitalWork(modifiedString):
    """
    (string) -> None
    Does the actual work of capitalizing the first letter of a string. Called from splitOnSpaces().
    """

    global newString
    newString = [] # Resets the newString variable, so as not to carry over words from previous work
    for word in modifiedString:
        if word[0] not in capitals:
            cap_word = changeToCap(word[0], word)
            newString.append(cap_word)
        else: # The word already starts with a capital letter
            newString.append(word)

    newString = " ".join(newString) # join using spaces


def capitalAllWork(modifiedString):
    """
    (string) -> None
    Does the actual work of uppercasing a string. Called from splitOnSpaces().
    """

    global newString
    newString = [] # Resets the newString variable, so as not to carry over words from previous work
    listOfWords = []
    for word in modifiedString:
        index = 0

        letters = list(word)
        for letter in letters:
            if letter in lowers:
                letters[index] = changeToUpper(letters[index])
            index += 1
        letters = "".join(letters)
        listOfWords.append(letters)
    newString = " ".join(listOfWords) # join using spaces


def capitalFirstWork(modifiedString):
    """
    (string) -> None
    Does the actual work of uppercasing the first letter of a string. Called from splitOnSpaces().
    """

    global newString
    newString = [] # Resets the newString variable, so as not to carry over words from previous work
    words = modifiedString
    if words[0][0] not in capitals: # If the first letter of the first word is not in the capitals list
        cap_word = changeToCap(words[0][0], words[0])
        words[0] = cap_word
    else: # The word already starts with a capital letter
        pass

    newString = " ".join(words) # join using spaces


def lowercaseWork(modifiedString):
    """
    (string) -> None
    Does the actual work of lowercasing a string. Called from splitOnSpaces().
    """

    global newString
    newString = [] # Resets the newString variable, so as not to carry over words from previous work
    listOfWords = []
    for word in modifiedString:
        index = 0

        letters = list(word)
        for letter in letters:
            if letter in capitals:
                letters[index] = changeToLower(letters[index])
            index += 1
        letters = "".join(letters)
        listOfWords.append(letters)
    newString = " ".join(listOfWords) # join using spaces


def splitOnSpaces(option, theString):
    """
    (string, string) -> string
    Splits the words up and decides, based on the option argument, to capitalize the first letter or lowercase all of the letters. Called from capitalizeFirst() and lowercaseAll()
    """

    inputString = theString
    modifiedString = inputString.split(" ") # Split on spaces
    if option == "up":
        capitalWork(modifiedString)
    elif option == "allup":
        capitalAllWork(modifiedString)
    elif option == "firstup":
        capitalFirstWork(modifiedString)
    elif option == "down":
        lowercaseWork(modifiedString)
    else:
        raise TypeError(
            f"'{option}' does not exist as a valid option for splitOnSpaces()."
        )

    return newString


def capitalizeFirst(theString):
    """
    (string) -> string
    Takes in a string of words and splits them at the spaces. Then it checks if the first letter of every word is capitalize, if it is not then it capitalizes it. It returns the same string with the capital letters.
    """

    return splitOnSpaces("up", theString)


def capitalizeAll(theString):
    """
    (string) -> string
    Takes in a string of words and splits them at the spaces. Then capitalizes every letter in the string.
    """

    return splitOnSpaces("allup", theString)


def capitalizeFirstOnly(theString):
    """
    (string) -> string
    Takes in a string of words and splits them at the spaces. Then it checks if the first letter of the first word is capitalize, if it is not then it capitalizes it. It returns the same string with the capital letter.
    """

    return splitOnSpaces("firstup", theString)


def lowercaseAll(theString):
    """
    (string) -> string
    Lowercases all of the letters in a string.
    """

    return splitOnSpaces("down", theString)