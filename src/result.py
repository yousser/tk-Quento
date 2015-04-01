
# libs import
import tkinter as TK
from tkinter import ttk


class Result(ttk.Frame):
    "Generic Head component;"
    # details display under label result
    DETAILS = "2 numbers"
    # default global config values
    CONFIG = {"padding": 10}

    def __init__ (self, master=None, **kw):
        # super class inits
        ttk.Frame.__init__ (self, master)
        self.configure(self.CONFIG)
        # member inits
        self.details = kw.get("details", self.DETAILS)
        self.font = kw.get("font", "sans 45")
        self._tk_owner = master
        self._result = TK.IntVar()
        self._stars = TK.StringVar()
        # widget inits
        self.init_widget(**kw)



    def init_widget(self, **kw):
        "widget's main inits;"
        # shortcuts
        _ft = self.font     # font style
        _dt = self.details  # details
        _st = self._stars   # number stars
        _rt = self._result  # result
        # create label result
        self.result = ttk.Label(
            self, textvariable=_rt, font=_ft
        )
        # create label stars
        self.stars = ttk.Label(
            self, textvariable=_st, font="sans 10"
        )
        # create label details
        ttk.Label(
            self, text=_dt, font="sans 12"
        ).pack(side=TK.BOTTOM)
        # layouts label
        self.result.pack(side=TK.TOP)
        self.stars.pack(side=TK.TOP)



