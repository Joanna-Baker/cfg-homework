"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you can generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.
"""


# # # without user input:
def generate_phrase(characters, phrase):
    character_list = []
    phrase_characters = []
    characters = characters
    characters_no_space = characters.replace(" ", "") # separate this so that the print characters keeps case
    characters_lower = characters_no_space.lower()  # separate this so that the print characters keeps case
    phrase = phrase
    phrase_no_space = phrase.replace(" ", "") # separate this so that the print characters keeps case
    phrase_lower = phrase_no_space.lower()  # separate this so that the print characters keeps case
    if len(characters) >= len(phrase):
        for character in phrase_lower:
            if character in characters_lower:
                # print(character_list)
                character_list.append(character)
        for letter in phrase_lower:
            # print(phrase_characters)
            phrase_characters.append(letter)
    elif len(characters) < len(phrase):
        print("Sorry there are not enough characters for that phrase")
        return False
    if character_list == phrase_characters:
        print(f"You can make the word {phrase} from your characters: {characters}")
        return True
    else:
        print("Sorry you cannot make that phrase")
        return False


# # # successful phrase
generate_phrase("12345helloiwouldlikesomeorangesandapplesandbananas!!!!???", "HeLlO I would likE SOme OranGES!")

# # # not enough characters
generate_phrase("oran", "orange")

# # # cannot make the phrase
generate_phrase("olanga", "orange")


# # # with user input:
def generate_phrase():
    character_list = []
    phrase_characters = []
    characters = input("Please enter your characters: ")
    characters_no_space = characters.replace(" ", "") # separate this so that the print characters keeps case
    characters_lower = characters_no_space.lower()  # separate this so that the print characters keeps case
    phrase = input("Please enter your phrase: ")
    phrase_no_space = phrase.replace(" ", "") # separate this so that the print characters keeps case
    phrase_lower = phrase_no_space.lower()  # separate this so that the print characters keeps case
    if len(characters) >= len(phrase):
        for character in phrase_lower:
            if character in characters_lower:
                # print(character_list)
                character_list.append(character)
        for letter in phrase_lower:
            # print(phrase_characters)
            phrase_characters.append(letter)
    elif len(characters) < len(phrase):
        print("Sorry there are not enough characters for that phrase")
        return False
    if character_list == phrase_characters:
        print(f"You can make the word {phrase} from your characters: {characters}")
        return True
    else:
        print("Sorry you cannot make that phrase")
        return False


generate_phrase()

# # # Usage # # #
"""
Successfully makes the phrase:

Input: 12345helloiwouldlikesomeorangesandapplesandbananas!!!!???
Input: HeLlO I would likE SOme OranGES!

Not enough characters:

Input: oran
Input: orange

Cannot make phrase:

Input: olange
Input: orange
"""
