import tkinter as tk
from tkinter import ttk
import text_file.config


# klasa do wyświetlania pomocy
class HelpScreen(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.icons = None
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.icons = {
            "stats": tk.PhotoImage(file="../icons/stats.png").subsample(15),
            "close": tk.PhotoImage(file="../icons/close.png").subsample(15)}

        # górny pasek
        container = tk.Frame(self, bg=text_file.config.COLOR_BACKGROUND, height=40)
        container.grid(sticky="we")
        container.grid_columnconfigure(1, weight=1)

        # przycisk zamykania
        tk.Button(
            container,
            image=self.icons["close"],
            bg=text_file.config.COLOR_BACKGROUND,
            border=0,
            cursor="hand2",
            command=lambda: self.controller.show_frame("WordleScreen"),
        ).grid(row=0, column=0)

        # napis wordle
        tk.Label(
            container, text="WORDLE", fg=text_file.config.Color_FONT, bg=text_file.config.COLOR_BACKGROUND,
            font=("Helvetica Neue", 28, "bold"), ).grid(row=0, column=1)

        #  przycisk statystyk
        tk.Button(
            container, image=self.icons["stats"], bg=text_file.config.COLOR_BACKGROUND, border=0, cursor="hand2",
            command=lambda: self.controller.show_frame("StatsScreen"),
        ).grid(row=0, column=2)

        # napisy
        ttk.Separator(self).grid(sticky="ew")
        tk.Frame(self, bg=text_file.config.COLOR_BACKGROUND, height=40).grid()
        self.rowconfigure(3, weight=1)
        container = tk.Frame(self, bg=text_file.config.COLOR_BACKGROUND)
        container.grid()
        tk.Label(container, text="Zasady", fg="#f0f3f5", bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 24, "bold"), ).grid(row=1, column=0)
        tk.Label(container, text=" ", fg=text_file.config.Color_FONT, bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 20), ).grid(row=2, column=0)
        tk.Label(container, text="Wpisz 5-literowe słowo, by spróbować odgadnąć hasło.", fg=text_file.config.Color_FONT,
                 bg=text_file.config.COLOR_BACKGROUND, font=("Helvetica Neue", 12, "bold"), ).grid(row=3, column=0)
        tk.Label(container, text=" ", fg=text_file.config.Color_FONT, bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 20), ).grid(row=4, column=0)
        tk.Label(container, text="Po każdej próbie, litery zostaną odpowiednie zaznaczone:",
                 fg=text_file.config.Color_FONT, bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 12, "bold")).grid(row=5, column=0)
        tk.Label(container, text=" ", fg=text_file.config.Color_FONT, bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 20), ).grid(row=6, column=0)
        tk.Label(container, text="Litera podświetlona jest na zielono, występuje ona w haśle w tym samym miejscu",
                 fg=text_file.config.Color_FONT, bg=text_file.config.COLOR_BACKGROUND, font=("Helvetica Neue", 10),
                 ).grid(row=7, column=0)
        cell = tk.Frame(container, width=55, height=55, highlightthickness=1,
                        highlightbackground=text_file.config.COLOR_BACKGROUND)
        cell.grid(row=8, column=0)
        btn = tk.Button(cell, text='R', justify="center", font=("Helvetica Neue", 20), bg="#3c4042", fg="#19bf1e",
                        cursor="hand2", border=0, )
        btn.grid(sticky="nswe")

        tk.Label(container, text="Litera podświetlona jest na żółto, występuje ona w haśle, lecz w innym miejscu",
                 fg=text_file.config.Color_FONT, bg=text_file.config.COLOR_BACKGROUND, font=("Helvetica Neue", 10),
                 ).grid(row=9, column=0)
        cell = tk.Frame(container, width=55, height=55, highlightthickness=1,
                        highlightbackground=text_file.config.COLOR_BACKGROUND)
        cell.grid(row=10, column=0)
        btn = tk.Button(cell, text='Y', justify="center", font=("Helvetica Neue", 20), bg="#3c4042", fg="#fff200",
                        cursor="hand2", border=0, )
        btn.grid(sticky="nswe")

        tk.Label(container, text="Jeśli litera nie jest podświetlona, nie występuje w haśle",
                 fg=text_file.config.Color_FONT, bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 10), ).grid(row=11, column=0)
        cell = tk.Frame(container, width=55, height=55, highlightthickness=1,
                        highlightbackground=text_file.config.COLOR_BACKGROUND)
        cell.grid(row=12, column=0)
        btn = tk.Button(cell, text='B', justify="center", font=("Helvetica Neue", 20), bg="#3c4042",
                        fg='#615f55', cursor="hand2", border=0, )
        btn.grid(sticky="nswe")
        tk.Label(container, text="", fg=text_file.config.Color_FONT, bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 14, "bold"), ).grid(row=20, column=0)
        tk.Label(container, text="Na odgadnięcie masz 6 prób, powodzenia!", fg=text_file.config.Color_FONT,
                 bg=text_file.config.COLOR_BACKGROUND, font=("Helvetica Neue", 14, "bold"), ).grid(row=14, column=0)
        tk.Label(container, text="", fg=text_file.config.Color_FONT, bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 14), ).grid(row=15, column=0)
        tk.Label(container, text="Hasło może być rzeczownikiem w mianowniku liczby pojedynczej, czasownikiem ",
                 fg=text_file.config.Color_FONT, bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 10,), ).grid(row=16, column=0)
        tk.Label(container,
                 text=" w bezokoliczniku, lub przymiotnikiem męskoosobowym w liczbie pojedynczej.",
                 fg=text_file.config.Color_FONT, bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 10,), ).grid(row=17,
                                                      column=0)
