#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# lib imports
import tkinter as TK
from tkinter import ttk

from src.plate import * 
from src.head import * 
from src.result import *
from src.tile import *
from src.fonctions import *



# main class def

class TkQuento (TK.Tk):
    r"""
       Quento puzzlz game;
       Python3-Tkinter port by yousser
    """
    # comonent disposal padding
    PADDING = 10

    def __init__ (self, **kw):
        # super class inits
        TK.Tk.__init__(self)
        # inits member
        self.list_results_2 = list()
        self.list_results_3 = list()
        # widget inits
        self.init_widget(**kw)
        self.new_game()
        # events
        self.plate.bind('<Button-1>', self.mouse_down)
    # end def
    

    def init_widget (self, **kw):
        r"""
            widget's main inits;
        """
        # main window inits
        self.title("Tk QUENTO")
        self.resizable(width=False, height=False)
        # look'n'fell
        ttk.Style().configure(".", font="sans 10")
        # inits
        _pad = self.PADDING
        _r = ttk.Frame(self)  #~frame layouts results
        # get quento's plate
        self.plate = Plate(self)
        # get quento's score 
        self.head = Head(self)
        # get quento's results
        self.result_2 = Result(_r, details="2 numbers")
        self.result_3 = Result(_r, details="3 numbers")
        # layout inits
        self.head.pack(side=TK.TOP, padx=_pad, pady=_pad)
        _r.pack(side=TK.TOP, padx=_pad, pady=_pad)
        self.result_2.pack(side=TK.LEFT, padx=_pad, pady=_pad)
        self.result_3.pack(side=TK.RIGHT, padx=_pad, pady=_pad)
        self.plate.pack(side=TK.TOP, padx=_pad, pady=_pad)
        ttk.Button(self, text='new', command=self.new_game).pack(side=TK.BOTTOM)
    # end def

    

    def new_game(self):
        """new partie game"""
        # shortcuts
        res_2 = self.list_results_2
        res_3 = self.list_results_3
        # clean up plate
        self.plate.clear_all()
        self.plate._input = str()
        # display name game
        self.head._display.set("tk-QUENTO")
        # nbs and results
        nbs, res_2, res_3 = data()
        # send n to plate
        self.plate._numbers = nbs
        # draw tiles in plate
        self.plate.draw_tiles()
        # display new results
        self.result_2._result.set(res_2[0])
        self.result_3._result.set(res_3[0])



    def mouse_down(self, event):
        _x, _y = event.x, event.y
        self.plate.mouse_down(event)
        # shortcuts
        _i = self.plate._input
        # calcul input user
        _c = calcul_input(_i)
        self.display_in_head()


    def display_in_head (self):
        """display in label head calculation (input user),
        if none input display game name 'QUNETO'."""
        i = self.plate._input
        if i != "":
            self.head._display.set(i)
        else:
            self.head._display.set("tk-QUENTO")


# end class TkQuento


if __name__ == "__main__":
    TkQuento()

    

    


