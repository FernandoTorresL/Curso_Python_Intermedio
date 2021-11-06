def read_file():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        palabras = f.readlines()
    #     for word in f:
    #         # words.append((word, end=''))
    #         words.append(print(word, end=''))
    # print(words)
    print(palabras)

def run():
    # Read word's file
    read_file()
    # Get one random word
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
