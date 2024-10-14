from googletrans import Translator
from bs4 import BeautifulSoup
import requests


def get_content():
    url = 'https://randomword.com/'
    response = requests.get(url=url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    word = soup.find('div', id='random_word').text.strip().title()
    definition = soup.find('div', id='random_word_definition').text.strip().title()

    return {word: definition}

def guess_the_word():
    print('Игра началась!\nУгадай слово по его определению!')
    translator = Translator()
    try:
        while True:
            content = get_content()
            word = next(iter(content))
            definition = content[word]
            translated_word = translator.translate(word, dest='ru')
            translated_def = translator.translate(definition, dest='ru')
            print(translated_def.text)
            guess = input('Напиши свое предположение: ').title()
            if guess != translated_word:
                print(f"А вот и не угадал! Загадано {translated_word.text}!")
            choice = input('Играем дальше? д/н:')
            if choice != 'д':
                print("Спасибо за игру!")
                break

    except Exception as e:
        print(f"Ошибка! {e}.")

guess_the_word()