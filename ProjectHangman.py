from random import choice
from Alfabeto import alphabet
from ListaPalavras import words, invalid_letters
# importa listas e função choice


def verify_word(words):
    while True:
        word = choice(words).upper()
        if ' ' not in word and '-' not in word and str(invalid_letters)[:] not in word:
            return word
# verifica se a palavra escolhida é válida, sem espaços, traços ou acentos
# 'invalid_letters' é convertido em string e varrido totalmente para verificar se ele não está em 'word'


def create_letter_list(word):
    word_letters = set()
    for letter in word.replace('', ' ').split():
        word_letters.add(letter)
    return word_letters
# cria uma lista do tipo 'set'
# converte 'word' de string para lista e para cada letra de word, a variável 'letter' recebe essa letra e adiciona
# na lista 'set' que não vai aceitar valores repetidos, dessa forma, mantém nela apenas as letras sem repetições da
# palavra


def hangman():
    letters_used = []
    word_formed = []
    fails_Count = 0
    word = verify_word(words)
    letters_list = create_letter_list(word)
    # cria listas letras usadas e palavra formada, também variáveis contador de falhas e chama outras funções

    while True:
        user_letter = str(input('Digite uma letra: ')).strip().upper()

        while user_letter not in alphabet:
            print('Caractere inválido. ', end='')
            user_letter = str(input('Digite uma letra: ')).strip().upper()

        if user_letter in word:
            if user_letter in letters_used or user_letter in word_formed:
                print(f'Você já digitou essa letra!\nLetras tentadas: {letters_used}')
            else:
                print('Você acertou uma letra!')
                word_formed.append(user_letter)
                print(word_formed)

        elif user_letter in letters_used or user_letter in word_formed:
            print(f'você já digitou essa letra!\nLetras tentadas: {letters_used}')

        else:
            print('Você errou uma letra!')
            letters_used.append(user_letter)
            fails_Count += 1

        if fails_Count >= 6:
            print('=' * 50)
            print('Sinto muito. Você perdeu!')
            print(f'A palavra era {word}')
            break

        if letters_list.issubset(word_formed):
            print('=' * 50)
            print('Parabéns! Você venceu!')
            print(f'A palavra era {word}')
            break
        # vefifica se os items de 'letters_list' são um subcojunto de 'word_formed'
        # como 'letters_list' recebe apenas as letras sem repetições de 'word' ele verifica se as letras salvas
        # em 'word_formed' bate com as salvas em 'latters_list'


hangman()
