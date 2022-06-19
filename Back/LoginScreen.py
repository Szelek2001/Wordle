import tkinter as tk
from tkinter import ttk
import text_file.config
from DB.DaoWordle import DaoWordle


# klasa do logowania
class LoginScreen(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.top_separator = None
        self.icons = None
        self.password = None
        self.login = None
        self.controller = controller
        self.bind('<Return>', lambda event: self.check())

        self.init_ui()

    def init_ui(self):

        self.icons = {
            "user": tk.PhotoImage(file="../icons/user.png").subsample(2),
            "close": tk.PhotoImage(file="../icons/close.png").subsample(15)
        }

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

        #  przycisk statystyk
        tk.Button(
            container, image=self.icons["user"], bg=text_file.config.COLOR_BACKGROUND, border=0, cursor="hand2",
            command=lambda: self.controller.show_frame("StatsScreen"),
        ).grid(row=0, column=2)

        # zostawiam miejsce na wyświetlanie
        ttk.Separator(self).grid(sticky="ew")
        self.top_separator = tk.Frame(self, bg=text_file.config.COLOR_BACKGROUND, height=45)
        self.top_separator.grid_rowconfigure(0, weight=1)
        self.top_separator.grid_columnconfigure(0, weight=1)
        self.top_separator.grid_propagate(False)
        self.top_separator.grid(sticky="news")

        self.rowconfigure(3, weight=1)
        container = tk.Frame(self, bg=text_file.config.COLOR_BACKGROUND)
        container.grid()

        # napisy i pola do wypełeninia
        tk.Label(container, text="Logowanie", fg="#f0f3f5", bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 30, "bold"), ).grid(row=4, column=0)
        tk.Label(container, text="                                           ", fg="#f0f3f5",
                 bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 30, "bold"), ).grid(row=5, column=0)

        tk.Label(container, text="login:", fg="#f0f3f5", bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 30, "bold"), ).grid(row=6, column=0)

        self.login = tk.Entry(container, fg="#f0f3f5", bg='#1d1d1f',
                              font=("Helvetica Neue", 30, "bold"), )

        self.login.grid(row=7, column=0, sticky='we')

        tk.Label(container, text="Hasło:", fg="#f0f3f5", bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 30, "bold"), ).grid(row=8, column=0)

        self.password = tk.Entry(container, fg="#f0f3f5", bg='#1d1d1f',
                                 font=("Helvetica Neue", 30, "bold"), show='*')

        self.password.grid(row=9, column=0, sticky='we')

        tk.Label(container, text="", fg="#f0f3f5", bg=text_file.config.COLOR_BACKGROUND,
                 font=("Helvetica Neue", 30, "bold"), ).grid(row=10, column=0)

        # przycisk logowania

        tk.Button(
            container, text="Zaloguj się", fg=text_file.config.Color_FONT, bg="#1d1d1f", border=0, cursor="hand2",
            font=("Helvetica Neue", 28, "bold"),
            command=lambda: self.check(),
        ).grid(row=11, column=0)

        self.bind('<Return>', lambda event: self.check())

    # sprawdzanie poprawności logowania
    def check(self):
        dao = DaoWordle()
        if not dao.check_usr(self.login.get()):
            self.toast("Nie ma takiego użytkownika!", 3)
            return False

        if not dao.checkpass(self.login.get(), self.password.get()):
            self.toast("Niepoprawne haslo", 3)
            return False

        text_file.config.USER = self.login.get()
        self.controller.show_frame("StatsScreen")

    # komunikaty
    def toast(self, message, duration=3):
        t = tk.Label(self.top_separator, text=message, font=("Helvetica Neue", 16))
        t.grid(row=0, column=0, sticky="news", padx=5, pady=5)
        # usuniecie po jakim czasie
        self.master.after(duration * 1000, lambda: t.grid_remove())
