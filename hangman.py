import random

words = ["dog"]
guessed_letters = set()


# This function selects a random word from the words list, prints it, and then returns it.


def random_word():
    random_word = random.choice(words)
    # print("random_word -> ", random_word)
    return random_word


# This function creates a dictionary mapping each character in the provided word to a list of its indexes in the word.


def random_word_dict(word):
    word_dict = {}
    for index, char in enumerate(word):
        if char in word_dict:
            word_dict[char].append(index)
        else:
            word_dict[char] = [index]
    return word_dict


# This function returns a string of underscores and spaces, representing the masked version of the word.


def show_dashes(word):
    return "_ " * len(word)


# This function prompts the user to input a letter and returns the letter.


def ask_letter(guessed_letters):
    while True:  # Loop until a non-duplicate, valid input is received
        chosen_letter = input("Pick a letter --> ")
        if chosen_letter.isalpha() and len(chosen_letter) == 1:
            if chosen_letter in guessed_letters:
                print("You already guessed that letter. Try a different one.")
            else:
                return chosen_letter  # Valid and not a duplicate
        else:
            print("You must enter one letter")


def update_guessed_letters(letter):
    global guessed_letters
    is_updated = False
    if letter in guessed_letters:
        print("You already guessed that letter. Choose a different letter")
        print("guessed_letters", guessed_letters)
        print("letter", letter)
    elif letter not in guessed_letters:
        is_updated = True
        guessed_letters.add(letter)
        print("is_updated ", is_updated)
        print("guessed_letters", guessed_letters)
    return guessed_letters, is_updated


# This function returns the indexes of a given letter in the word_dict. If the letter is not found, it returns an empty list


def find_letter_indexes(word_dict, letter):
    return word_dict.get(letter, [])


# This function calculates the number of letters in the word that haven't been guessed yet


def remaining_letters(word, guessed_letters):
    return len([char for char in word if char not in guessed_letters])


# This function updates the masked word (template) with correctly guessed letters based on their indexes from replacement_dict


def update_masked_word(template, replacement_dict):
    template_list = list(template.replace(" ", ""))
    for char, indexes in replacement_dict.items():
        for index in indexes:
            template_list[index] = char
    return " ".join(template_list)


# This is the main function where the game logic is implemented. It controls the game flow, keeps track of guessed letters, lives, and determines the game's result


def play_game():
    word = random_word()
    word_dict = random_word_dict(word)
    # print("word_dict --------> ", word_dict)
    masked_word = show_dashes(word)
    # print("masked_word --------> ", masked_word)
    lives = 6
    game_result = ""

    while game_result != "won" and game_result != "dead":
        print(masked_word)
        letter_guess = ask_letter(guessed_letters)
        print("letter_guess", letter_guess)
        update_guessed_letters(letter_guess)

        # Get the first element in a tuple

        if letter_guess in word:
            right_indexes = find_letter_indexes(word_dict, letter_guess)
            replacement_dict = {letter_guess: right_indexes}
            masked_word = update_masked_word(masked_word, replacement_dict)
            if remaining_letters(word, guessed_letters) == 0:
                game_result = "won"
                print("You've won! The word was:", word)
                break
        else:
            lives -= 1
            if lives == 0:
                game_result = "dead"
                print("Game over! The word was:", word)
                break
            print(f"Wrong guess. Lives remaining: {lives}")


play_game()
