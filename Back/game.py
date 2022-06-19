import random

from bs4 import BeautifulSoup
import requests

import text_file.config

from DB.DaoWordle import DaoWordle


class WordleGame:

    # Konstruktor klasy game
    def __init__(self):
        self._ALL_WORDS = []
        self._ANSWERS = (
            set(word.upper() for word in open("../text_file/Odpowiedzi", encoding='utf-8').read().splitlines()))
        self._ANSWER = []
        self._guesses = [""] * 6
        self._correct_letters = set()
        self._half_correct_letter = set()
        self._incorrect_letters = set()
        self._attempt_number = 0

    @property
    def all_words(self):
        return self.all_words

    @property
    def answer(self):
        return self._ANSWER

    @property
    def answers(self):
        return self.answers

    @property
    def attempt_number(self):
        return self._attempt_number

    @attempt_number.setter
    def attempt_number(self, value):
        self._attempt_number = value

    @property
    def guesses(self):
        return self._guesses

    @property
    def correct_letters(self):
        return self._correct_letters

    @property
    def half_correct_letter(self):
        return self._half_correct_letter

    @property
    def incorrect_letters(self):
        return self._incorrect_letters

    # losowanie słowa będącego odpowiedzią
    def choose_answer(self):
        self._ANSWER = random.choice(list(self._ANSWERS)).upper()

    # wykorzystując web scraping tworzę listę słów z SJP
    def create_list_words(self):
        url = 'https://sjp.pl/sl/growe/?d=5'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        main_div = soup.find(style='overflow-y: auto; margin-bottom: 2em;text-transform: uppercase;')
        words = main_div.text.split('\n')[2:][:-2]
        self._ALL_WORDS = set(word.upper() for word in words)

    # Sprawdzanie poprawności słowa
    def check_word(self):
        if len(self._guesses[self._attempt_number]) < text_file.config.WORD_LEN:
            return "Zbyt mało liter"

        if self._guesses[self._attempt_number] not in self._ALL_WORDS:
            return "Nie ma takiego słowa"

        return " "

    # aktulizacja poprawności liter po próbie zgadnięcia
    def update_letters(self):
        colors = []
        freq = {c: self._ANSWER.count(c) for c in self._ANSWER}
        for x, y in zip(self._guesses[self._attempt_number], self._ANSWER):
            if x == y:
                colors.append(text_file.config.COLOR_CORRECT)
                self._correct_letters.add(x)
            elif freq.get(x, 0) > 0:
                colors.append(text_file.config.COLOR_HALF_CORRECT)
                self._half_correct_letter.add(x)
                freq[x] -= 1
            else:
                self._incorrect_letters.add(x)
                colors.append(text_file.config.COLOR_INCORRECT)

        return colors

    # sprawdzanie wygranej / ewentualnej porażki
    def check_win(self):
        if self._guesses[self._attempt_number - 1] == self._ANSWER:
            dao = DaoWordle()
            dao.update_win(text_file.config.USER, self._attempt_number)
            return "Win"

        elif self._attempt_number == text_file.config.MAX_ATTEMPTS:
            dao = DaoWordle()
            dao.update_lost(text_file.config.USER)
            return "lose"
        else:
            return "play"
