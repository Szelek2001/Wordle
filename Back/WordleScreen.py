import string
import tkinter as tk
from tkinter import ttk
import text_file.config
from Back.game import WordleGame
from text_file.config import Polish_Latter


# klasa główna z grą
class WordleScreen(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.game_over_dialog = None
        self.icons = None
        self.game_over_dialog_message = None
        self.game_over_dialog_title = None
        self.keyboard_buttons = None
        self.labels = None
        self.top_separator = None
        self.controller = controller
        # zbindowane przyciski
        self.bind("<Return>", self.check_word)
        self.bind("<BackSpace>", self.remove_letter)
        self.bind("<Key>", self.enter_letter_standard)
        self.bind("<Control-Key-c>", self.enter_letter_c)
        self.bind("<Control-Key-a>", self.enter_letter_a)
        self.bind("<Control-Key-e>", self.enter_letter_e)
        self.bind("<Control-Key-l>", self.enter_letter_l)
        self.bind("<Control-Key-o>", self.enter_letter_o)
        self.bind("<Control-Key-s>", self.enter_letter_s)
        self.bind("<Control-Key-n>", self.enter_letter_n)
        self.bind("<Control-Key-z>", self.enter_letter_z)
        self.bind("<Control-Key-x>", self.enter_letter_x)

        self._game = WordleGame()
        self.init_ui()
        self.new_game()

    # inicjalizacja nowej gry
    def new_game(self):
        self._game = WordleGame()
        self._game.create_list_words()
        self._game.choose_answer()

        # reset klawiatury i próby
        for i in range(text_file.config.MAX_ATTEMPTS):
            self._game._attempt_number = i
            self.update_labels()
        self._game._attempt_number = 0
        self.update_keyboard()
        # ukrywam okno dialogu
        self.game_over_dialog.place_forget()

    # informacja o wygranej
    def info_win(self):
        praises = ["Za pierwszym", "Za drugim", "Za trzecim", "Za czwartym", "Za piątym", "Za szóstym"]
        self.game_over_dialog_title.set(praises[self._game.attempt_number - 1] + "!")
        self.game_over_dialog_message.set("Chcesz zagrać ponownie?")
        self.game_over_dialog.place(relx=0.5, rely=0.5, anchor="center")

    # informacja o przegranej
    def info_lost(self):
        self.game_over_dialog_title.set("Następnym razem wygrasz!")
        self.game_over_dialog_message.set(
            f"Jeszcze raz?\n(BTW słowo to {self._game.answer})")
        self.game_over_dialog.place(relx=0.5, rely=0.5, anchor="center")

    def init_ui(self):
        # dodanie ikon
        self.icons = {
            "stats": tk.PhotoImage(file="../icons/stats.png").subsample(15),
            "help": tk.PhotoImage(file="../icons/help.png"),
            "backspace": tk.PhotoImage(file="../icons/backspace.png"),
        }

        # górny pasek
        container = tk.Frame(self, bg=text_file.config.COLOR_BACKGROUND, height=40)
        container.grid(sticky="we")
        container.grid_columnconfigure(1, weight=1)

        tk.Button(container, image=self.icons["help"], bg=text_file.config.COLOR_BACKGROUND, border=0, cursor="hand2",
                  command=lambda: self.controller.show_frame("HelpScreen"), ).grid(row=0, column=0)

        tk.Label(container, text="WORDLE", fg="#d7dadc", bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 28, "bold"), ).grid(row=0, column=1)

        tk.Button(container, image=self.icons["stats"], bg=text_file.config.COLOR_BACKGROUND, border=0, cursor="hand2",
                  command=lambda: self.controller.show_frame("StatsScreen"), ).grid(row=0, column=2)

        # zostawiam miejsce na wyświetlanie 
        ttk.Separator(self).grid(sticky="ew")
        self.top_separator = tk.Frame(self, bg=text_file.config.COLOR_BACKGROUND, height=45)
        self.top_separator.grid_rowconfigure(0, weight=1)
        self.top_separator.grid_columnconfigure(0, weight=1)
        self.top_separator.grid_propagate(False)
        self.top_separator.grid(sticky="news")

        self.rowconfigure(3, weight=1)
        container = tk.Frame(self, bg="#3d3939")
        container.grid()

        # tworzę miejsce na literki
        self.labels = []
        for i in range(text_file.config.MAX_ATTEMPTS):
            row = []
            for j in range(text_file.config.WORD_LEN):
                field = tk.Frame(container, width=text_file.config.BOX_SIZE, height=text_file.config.BOX_SIZE,
                                 highlightthickness=1,
                                 highlightbackground=text_file.config.COLOR_INCORRECT, )
                field.grid_propagate(False)
                field.grid_rowconfigure(0, weight=1)
                field.grid_columnconfigure(0, weight=1)
                field.grid(row=i, column=j, padx=text_file.config.PAD_SIZE, pady=text_file.config.PAD_SIZE)
                t = tk.Label(field, text="", justify="center", font=("Helvetica Neue", 24, "bold"),
                             bg=text_file.config.COLOR_BLANK, fg="#d7dadc", highlightthickness=1,
                             highlightbackground=text_file.config.COLOR_BLANK, )
                t.grid(sticky="news")
                row.append(t)
            self.labels.append(row)

        tk.Frame(self, bg=text_file.config.COLOR_BLANK, height=45).grid()

        # klawiatura
        container = tk.Frame(self, bg=text_file.config.COLOR_BLANK)
        container.grid()

        self.keyboard_buttons = {}
        for i, keys in enumerate(["ĄĆĘŁÓŚŃŻŹ", "QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]):
            row = tk.Frame(container, bg=text_file.config.COLOR_BLANK)
            row.grid(row=i, column=0)
            for j, c in enumerate(keys):
                if i == 3:  # dodaje miejsce na entera
                    j += 1

                field = tk.Frame(row, width=40, height=55, highlightthickness=1,
                                 highlightbackground=text_file.config.COLOR_INCORRECT, )
                field.grid_propagate(False)
                field.grid_rowconfigure(0, weight=1)
                field.grid_columnconfigure(0, weight=1)
                field.grid(row=0, column=j, padx=text_file.config.PAD_SIZE, pady=text_file.config.PAD_SIZE)
                btn = tk.Button(field, text=c, justify="center", font=("Helvetica Neue", 13),
                                bg=text_file.config.COLOR_BLANK, fg="#d7dadc", cursor="hand2", border=0,
                                command=lambda c2=c: self.enter_letter(key=c2),
                                )
                btn.grid(sticky="nswe")
                self.keyboard_buttons[c] = btn

        # Dodanie Entera

        text = "ENTER"
        func = self.check_word
        field = tk.Frame(row, width=75, height=55, highlightthickness=1,
                         highlightbackground=text_file.config.COLOR_INCORRECT, )
        field.grid_propagate(False)
        field.grid_rowconfigure(0, weight=1)
        field.grid_columnconfigure(0, weight=1)
        field.grid(row=0, column=0, padx=text_file.config.PAD_SIZE, pady=text_file.config.PAD_SIZE)
        btn = tk.Button(field, text=text, justify="center", font=("Helvetica Neue", 13),
                        bg=text_file.config.COLOR_BLANK,
                        fg="#d7dadc", cursor="hand2", border=0, command=func, )
        btn.grid(row=0, column=0, sticky="nswe")

        # Dodanie backspace
        text2 = ""
        func = self.remove_letter
        field = tk.Frame(row, width=75, height=55, highlightthickness=1,
                         highlightbackground=text_file.config.COLOR_INCORRECT, )
        field.grid_propagate(False)
        field.grid_rowconfigure(0, weight=1)
        field.grid_columnconfigure(0, weight=1)
        field.grid(row=0, column=8, padx=text_file.config.PAD_SIZE, pady=text_file.config.PAD_SIZE)
        btn = tk.Button(field, text=text2, justify="center", font=("Helvetica Neue", 13),
                        bg=text_file.config.COLOR_BLANK,
                        fg="#d7dadc", cursor="hand2", border=0, command=func, )
        btn.grid(row=0, column=0, sticky="nswe")
        btn.configure(image=self.icons["backspace"])

        # informacja o końcu gry
        self.game_over_dialog = tk.Frame(self, bg=text_file.config.COLOR_INCORRECT, highlightthickness=2)

        self.game_over_dialog_title = tk.StringVar()
        tk.Label(self.game_over_dialog, textvariable=self.game_over_dialog_title, font=("Helvetica Neue", 22),
                 bg=text_file.config.COLOR_INCORRECT, fg="white", ).grid(sticky="news", padx=10, pady=10)
        ttk.Separator(self.game_over_dialog).grid(sticky="ew")

        # wiadomości
        self.game_over_dialog_message = tk.StringVar()
        tk.Label(self.game_over_dialog, textvariable=self.game_over_dialog_message, font=("Arial", 16),
                 bg=text_file.config.COLOR_INCORRECT, fg="white", ).grid(sticky="news", padx=10, pady=10)
        ttk.Separator(self.game_over_dialog).grid(sticky="ew")

        # tak/nie
        self.game_over_dialog.grid_rowconfigure(4, weight=1)
        f = tk.Frame(self.game_over_dialog, bg=text_file.config.COLOR_INCORRECT)
        f.grid(sticky="news")
        f.grid_columnconfigure(0, weight=1)
        f.grid_columnconfigure(2, weight=1)
        for col in (0, 2):
            btn_text = "PEWNIE" if col == 0 else "NIE :("
            func = self.new_game if col == 0 else self.controller.destroy
            btn = tk.Button(f, text=btn_text, bg=text_file.config.COLOR_INCORRECT, fg="white",
                            font=("Helvetica Neue", 13), border=0, cursor="hand2", command=func, )
            btn.grid(row=0, column=col, sticky="ew")

        ttk.Separator(f, orient="vertical").grid(row=0, column=1, sticky="ns")

        # komunikat

    def toast(self, message, duration=3):
        t = tk.Label(self.top_separator, text=message, font=("Helvetica Neue", 16))
        t.grid(row=0, column=0, sticky="news", padx=5, pady=5)
        # usuniecie po jakim czasie
        self.master.after(duration * 1000, lambda: t.grid_remove())

        # aktulizacja klawiatury

    def update_keyboard(self):

        for key, btn in self.keyboard_buttons.items():
            if key in self._game.correct_letters:
                btn["bg"] = text_file.config.COLOR_CORRECT
            elif key in self._game.half_correct_letter:
                btn["bg"] = text_file.config.COLOR_HALF_CORRECT
            elif key in self._game.incorrect_letters:
                btn["bg"] = text_file.config.COLOR_INCORRECT
            else:
                btn["bg"] = text_file.config.COLOR_BLANK

    # aktulizacja kafelków
    def update_labels(self, colors=None):

        word = self._game.guesses[self._game.attempt_number]

        for i, label in enumerate(self.labels[self._game.attempt_number]):
            try:
                letter = word[i]
            except IndexError:
                letter = ""
            label["text"] = letter
            if colors:
                label["bg"] = colors[i]
                label["highlightbackground"] = colors[i]
            else:
                label["bg"] = text_file.config.COLOR_BLANK
                label["highlightbackground"] = (
                    text_file.config.COLOR_BORDER_HIGHLIGHT if letter else text_file.config.COLOR_BLANK
                )

        # sprawdzenia słowa

    def check_word(self, event=None):
        if self._game.check_word() != " ":
            self.toast(self._game.check_word())
            return

        self.update_labels(self._game.update_letters())
        self.update_keyboard()

        self._game.attempt_number += 1
        self.announcement()

        # ogłoszenie jeśli zwycięzca

    def announcement(self):
        score = self._game.check_win()
        if score == "Win":
            self.info_win()
        elif score == "lose":
            self.info_lost()

        #usuniecie litery
    def remove_letter(self, event=None):
        if self._game.guesses[self._game.attempt_number]:
            self._game.guesses[self._game.attempt_number] = self._game.guesses[self._game.attempt_number][:-1]
            self.update_labels()

        #wprowadzanie liter
    def enter_letter_standard(self, event=None, key=None):
        key = event.keysym.upper()
        self.enter_letter(key)

    def enter_letter_c(self, event=None, key=None):

        key = 'Ć'
        self.enter_letter(key)

    def enter_letter_a(self, event=None, key=None):

        key = 'Ą'
        self.enter_letter(key)

    def enter_letter_e(self, event=None, key=None):

        key = 'Ę'
        self.enter_letter(key)

    def enter_letter_l(self, event=None, key=None):

        key = 'Ł'
        self.enter_letter(key)

    def enter_letter_o(self, event=None, key=None):

        key = 'Ó'
        self.enter_letter(key)

    def enter_letter_s(self, event=None, key=None):

        key = 'Ś'
        self.enter_letter(key)

    def enter_letter_n(self, event=None, key=None):

        key = 'Ń'
        self.enter_letter(key)

    def enter_letter_z(self, event=None, key=None):

        key = 'Ż'
        self.enter_letter(key)

    def enter_letter_x(self, event=None, key=None):

        key = 'Ź'
        self.enter_letter(key)

    def enter_letter(self, key):
        if key in string.ascii_uppercase or Polish_Latter.__contains__(key):
            self._game.guesses[self._game.attempt_number] += key
            # brak możliwości wpisania zbyt dużej ilość liter
            self._game.guesses[self._game.attempt_number] = self._game.guesses[self._game.attempt_number][
                                                            :text_file.config.WORD_LEN]
            self.update_labels()
