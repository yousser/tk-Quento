# libs import
import tkinter as TK
from tkinter import ttk


class Head(ttk.Frame):
    "Generic Head component;"
    # default global config values
    CONFIG = {"padding": 10}
    FONT = "sans 30"

    def __init__ (self, master=None, **kw):
        # super class inits
        ttk.Frame.__init__ (self, master)
        self.configure(self.CONFIG)
        # member inits
        self.font = kw.get("font", self.FONT)
        self.name = "QUENTO"
        self._tk_owner = master
        self._lavel = TK.IntVar()
        self._display = TK.StringVar()
        # set "QUENTO" in display
        self._display.set(self.name)
        # widget inits
        self.init_widget()
        

    def next_level (self):
        """adds 1 to cuurent level value;"""
        self._level.set(
            self._level.get() + 1
        )



    def get_level (self):
        """returns currnt level value;"""
        return self._level.get()
        


    def init_widget(self):
        "widget's main inits;"
        _ft = self.font     # shortcut font style
        # create label head
        self.head = ttk.Label(
            self, textvariable=self._display, font=_ft
        )
        self.head.pack()
