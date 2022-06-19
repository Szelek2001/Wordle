import tkinter as tk
from tkinter import ttk
import text_file.config

from DB.DaoWordle import DaoWordle


# klasa do wyswietlania statystyk
class StatsScreen(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.icons = None
        self.controller = controller
        self.dao = DaoWordle()
        self.init_ui()

    def init_ui(self):
        self.icons = {
            "help": tk.PhotoImage(file="../icons/help.png"),
            "close": tk.PhotoImage(file="../icons/close.png").subsample(15),
            "detail": tk.PhotoImage(file="../icons/detail.png").subsample(5)}

        # górny pasek

        container = tk.Frame(self, bg=text_file.config.COLOR_BACKGROUND, height=40)
        container.grid(sticky="we")
        container.grid_columnconfigure(1, weight=1)

        # przycisk zamykania
        tk.Button(container, image=self.icons["close"], bg=text_file.config.COLOR_BACKGROUND, border=0, cursor="hand2",
                  command=lambda: self.controller.show_frame("WordleScreen"), ).grid(row=0, column=0)
        # napis wordle
        tk.Label(
            container, text="WORDLE", fg=text_file.config.Color_FONT, bg=text_file.config.COLOR_BACKGROUND,
            font=("Helvetica Neue", 28, "bold"), ).grid(row=0, column=1)

        # przycisk pomocy
        tk.Button(
            container, image=self.icons["help"], bg=text_file.config.COLOR_BACKGROUND, border=0, cursor="hand2",
            command=lambda: self.controller.show_frame("HelpScreen"),
        ).grid(row=0, column=2)

        ttk.Separator(self).grid(sticky="we")
        tk.Frame(self, bg=text_file.config.COLOR_BACKGROUND, height=40).grid()
        self.rowconfigure(3, weight=1)
        container = tk.Frame(self, bg=text_file.config.COLOR_BACKGROUND)
        container.grid()

        # wyświetlanie zależnie czy użtkownik jest zaalogowany
        if text_file.config.USER == 'gosc':
            self.gosc_view(container)
        else:
            self.user_view(container)

        # widok dla gościa

    def gosc_view(self, container):

        tk.Button(
            container, text="Logowanie", fg=text_file.config.Color_FONT, bg="#1d1d1f", border=0, cursor="hand2",
            font=("Helvetica Neue", 28, "bold"),
            command=lambda: self.controller.show_frame("LoginScreen"),
        ).grid(row=2, column=0)

        tk.Label(container, text="", fg="#f0f3f5", bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 50, "bold"), ).grid(row=4, column=0)

        tk.Label(container, text="Nie masz konta?", fg="#f0f3f5", bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 30, "bold"), ).grid(row=5, column=0)

        tk.Label(container, text="", fg="#f0f3f5", bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 50, "bold"), ).grid(row=6, column=0)

        tk.Button(
            container, text="Rejestracja", fg=text_file.config.Color_FONT, bg="#1d1d1f", border=0, cursor="hand2",
            font=("Helvetica Neue", 28, "bold"),
            command=lambda: self.controller.show_frame("RegisterScreen"),
        ).grid(row=7, column=0)

        tk.Label(container, text="", fg="#f0f3f5", bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 50, "bold"), ).grid(row=8, column=0)

        tk.Label(container, text="  Zarejestruj się teraz, aby mieć dostęp do cudownych statystyk!  ", fg="#f0f3f5",
                 bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 13,), ).grid(row=9, column=0)

        # widok dla użytkownika

    def user_view(self, container):
        tk.Label(container, text="Jesteś zalogowany jako:", fg="#f0f3f5", bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 30, "bold"), ).grid(row=1, column=0)
        tk.Label(container, text=self.dao.get(text_file.config.USER).player_name, fg="#f0f3f5",
                 bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 30, "bold"), ).grid(row=2, column=0)
        tk.Label(container, text=" ", fg="#f0f3f5", bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 20, "bold"), ).grid(row=3, column=0)
        tk.Label(container, text="Twoje statystyki:", fg="#f0f3f5", bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 20, "bold"), ).grid(row=4, column=0)

        tk.Label(container, text=" ", fg="#f0f3f5",
                 bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 30,), ).grid(row=5, column=0, sticky="w")

        tk.Label(container, text=" Zagrane       Wygrane       Przegrane", fg="#f0f3f5",
                 bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 20, "bold"), ).grid(row=6, column=0, )

        tk.Label(container,
                 text="        " + str(self.dao.get(text_file.config.USER).game) + "                   " + str(
                     self.dao.get(text_file.config.USER).win) + "                   " + str(
                     self.dao.get(text_file.config.USER).lose),
                 fg="#f0f3f5", bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 20,), ).grid(row=7, column=0, sticky="w")

        tk.Label(container, text=" ", fg="#f0f3f5",
                 bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 30,), ).grid(row=8, column=0, sticky="w")

        # przycisk większej ilosci statystyk
        tk.Button(
            container, image=self.icons["detail"], bg=text_file.config.COLOR_BACKGROUND, border=0, cursor="hand2",
            command=lambda: self.detail(container),
        ).grid(row=9, column=0, sticky="w")

        # wyświetlanie większej ilości statystyk

    def detail(self, container):

        tk.Label(container, text=" ", fg="#f0f3f5",
                 bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 30,), ).grid(row=11, column=0, sticky="w")
        tk.Label(container, text=" Za pierwszym: " + str(self.dao.get(text_file.config.USER).A1), fg="#f0f3f5",
                 bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 15,), ).grid(row=12, column=0, sticky="w")
        tk.Label(container, text=" Za drugim: " + str(self.dao.get(text_file.config.USER).A2), fg="#f0f3f5",
                 bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 15,), ).grid(row=13, column=0, sticky="w")
        tk.Label(container, text=" Za trzecim: " + str(self.dao.get(text_file.config.USER).A3), fg="#f0f3f5",
                 bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 15,), ).grid(row=14, column=0, sticky="w")
        tk.Label(container, text=" Za czwartym: " + str(self.dao.get(text_file.config.USER).A4), fg="#f0f3f5",
                 bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 15,), ).grid(row=15, column=0, sticky="w")
        tk.Label(container, text=" Za piątym: " + str(self.dao.get(text_file.config.USER).A5), fg="#f0f3f5",
                 bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 15,), ).grid(row=16, column=0, sticky="w")
        tk.Label(container, text=" Za szóstym: " + str(self.dao.get(text_file.config.USER).A6), fg="#f0f3f5",
                 bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 15,), ).grid(row=17, column=0, sticky="w")
