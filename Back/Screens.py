import tkinter as tk

import HelpScreen
import WordleScreen
import StatsScreen
from Back import LoginScreen
import RegisterScreen
from text_file.config import COLOR_BLANK, COLOR_BACKGROUND


# klasa do zarządzania obrazami
class WordleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Wordle")
        self.app_icon = tk.PhotoImage(file="../icons/logo.png")
        self.iconphoto(False, self.app_icon)
        self.pages_dict = {}
        self.pages = tk.Frame(self, bg=COLOR_BACKGROUND)
        self.pages.grid(sticky="news")
        self.new_ss()
        self.show_frame("WordleScreen")

    # pokazanie ramki dla podanej nazwy strony
    def show_frame(self, page_name):
        self.delstats()
        frame = self.pages_dict[page_name]

        # ustawienie focusa by można przechwycić ramkę
        frame.focus_set()
        frame.tkraise()

    # Tworzę zbiór stron, aby łatwo pomiędzy nimi "przeskakiwać"
    def new_ss(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # tworzę słownik ze stronami
        self.pages_dict = {"WordleScreen": WordleScreen.WordleScreen(
            master=self.pages, controller=self, bg=COLOR_BACKGROUND), "StatsScreen": StatsScreen.StatsScreen(
            master=self.pages, controller=self, bg=COLOR_BLANK), "HelpScreen": HelpScreen.HelpScreen(
            master=self.pages, controller=self, bg=COLOR_BACKGROUND), "LoginScreen": LoginScreen.LoginScreen(
            master=self.pages, controller=self, bg=COLOR_BACKGROUND), "RegisterScreen": RegisterScreen.RegisterScreen(
            master=self.pages, controller=self, bg=COLOR_BACKGROUND)}

        # umieszczam wszytskie strony w tym samej lokacji
        self.pages_dict["WordleScreen"].grid(row=0, column=0, sticky="news")
        self.pages_dict["StatsScreen"].grid(row=0, column=0, sticky="news")
        self.pages_dict["HelpScreen"].grid(row=0, column=0, sticky="news")
        self.pages_dict["LoginScreen"].grid(row=0, column=0, sticky="news")
        self.pages_dict["RegisterScreen"].grid(row=0, column=0, sticky="news")

    # usuwanie ramki z statystykami
    def delstats(self):
        del self.pages_dict["StatsScreen"]
        self.pages_dict["StatsScreen"] = StatsScreen.StatsScreen(
            master=self.pages, controller=self, bg=COLOR_BLANK)
        self.pages_dict["StatsScreen"].grid(row=0, column=0, sticky="news")
