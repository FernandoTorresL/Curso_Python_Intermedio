import random

def read_file():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for word in f:
            word = word.strip()
            words.append(word)
    print(words)
    return words

def get_random_word(words):
    upper_limit = len(words)
    print("Cantidad de palabras: ", upper_limit)

    random_index = random.randint(0, upper_limit)
    print("Indice al azar: ", random_index)

    return words[random_index]

def run():
    # Read word's file
    words = []
    words = read_file()

    # Get one random word
    word = get_random_word(words)
    print("La palabra elegida al azar es: ", word)

    print()

    # Print the game interface
        #  Print blank spaces for the choosen word
    # Get an input letter from the user
        # Validate the input letter
    # Compare the input with the letters from the choosen word
        # Show in screen if the letter was correct or not:
            # If is correct
                # ...check if it's the last letter
                    # ...if so, print WIN
                # ...or print all the correct letters on the blank spaces
            # but, if isn't correct, check the number of tries
                # If is the last try,
                    # ...print LOSE
                # ...or ask for another letter (cicle)


if __name__ == '__main__':
    run()
