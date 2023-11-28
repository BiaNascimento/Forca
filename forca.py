import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def forca():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6


    while len(word_letters) > 0 and lives > 0:

        print("Você tem", lives, "vidas restantes e você usou as letras: ", ''.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Palavra atual: ', ''.join(word_list))

        user_letter = input('Escolha uma letra: ').upper()
        if user_letter in alphabet - used_letters:
           used_letters.add(user_letter)
           if user_letter in word_letters:
               word_letters.remove(user_letter)

           else:
               lives = lives -1
               print("Essa letra não faz parte da palavra")

        elif user_letter in used_letters:
            print("Você já usou essa letra! Por favor, escolha outra")

        else:
            print("Caractere inválido. Por favor, digite apenas uma letra")

    if lives == 0:
        print(f"Você morreu! A palavra correta era {word}.")
    else:
        print(f"Você acertou! A palavra é {word}!")

forca()


