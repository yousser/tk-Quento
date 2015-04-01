
# lib imports
import tkinter as TK
from math import ceil
from src.tile import *


class Plate(TK.Canvas):
    "Generic Plate component;"

    # default global config values
    CONFIG = {
            "background" :  "white",
            "highlightthickness": 0,
            "borderwidth": 0,
            "width": 300,
            "height": 300,
    }

    def __init__ (self, master, **kw):

        # super class inits
        TK.Canvas.__init__ (self, master)
        self.configure(self.CONFIG)

        # inits member
        self.bgcolor = kw.get("bgcolor", self.CONFIG["background"])
        self.width = kw.get("width", self.CONFIG["width"])
        self.height = kw.get("height", self.CONFIG["height"])

        # private members
        self._tk_owner = master
        self._tiles = [0]*9
        self._numbers = [0]*5
        self._input = str()
        self._active_tiles = list()

        # widget inits
        self.draw_tiles()
        

    def draw_tiles(self):
        "widget's main inits;"

        # shurtcuts
        _n = self._numbers
        
        # all args for any tile in tuples
        _infos = [
                (0, 0, 0, _n[0], 'black'), (1, 100, 0, '+', 'white'), (2, 200, 0, _n[1], 'black'),
                (3, 0, 100, '-', 'white'), (4, 100, 100, _n[2], 'black'), (5, 200, 100, '-', 'white'),
                (6, 0, 200, _n[3], 'black'), (7, 100, 200, '+', 'white'), (8, 200, 200, _n[4], 'black'),
        ]
        
        for n, x, y, t, c in _infos:
            self._tiles[n] = Tile(self, x=x, y=y, text=t, bgcolor=c)



    def clear_all(self):
        "clears up canvas entirely;"

        # clears up canvas
        self.delete(TK.ALL)

        # zeroing numbers
        self._numbers = [0]*5

        # zeroing tiles
        self._tiles = [0]*9

        # zeroing input user

  



    def mouse_down(self, event):

        """event bind click;"""

        # coords

        _x, _y = event.x, event.y

        _t = self.clicked_tile(_x, _y)

        if self.neighboring(_t):

            self.procedure(_x, _y)




    def clicked_tile (self, x, y):

        """ determinr tile cliked;"""

        # determine row and column

        row = ceil(y/100)

        column = ceil(x/100)

        # exception

        row = 1 if row == 0 else row

        column = 1 if column == 0 else column

        # dict of paire (rown column) : tile

        _dict = {

            (1,1):0, (1,2):1, (1,3):2,

            (2,1):3, (2,2):4, (2,3):5,

            (3,1):6, (3,2):7, (3,3):8,

        }

        return _dict.get((row, column))



    def procedure(self, x, y):

        """all procedure well be after click."""

        # determin tile

        _tile = self.clicked_tile(x, y)

        # return text tile

        _text = str(self._tiles[_tile].txt_tile)

        # if _tile active don't

        if _tile not in self._active_tiles:

            # add text to input

            self._input += _text

            # add tile to active tiles

            self._active_tiles.append(_tile)

            return

        self._input = self._input[:-1]

        self._active_tiles.remove(_tile)

    


    def neighboring(self, tile):

        """التأكد من أن المربع المنقور عليه

           مجارو للمنقور سلفا
        """

        # shurtcut

        _i = self._input        

        # dict neighboring tiles

        dict_neighboring = {

             0: (0, 1, 3),

             1: (0, 1, 2, 4),

             2: (1, 2, 5),

             3: (0, 3, 4, 6),

             4: (1, 3, 4, 5, 7),

             5: (2, 4, 5, 8),

             6: (3, 6, 7),

             7: (4, 6, 7, 8),

             8: (5, 7, 8),

        }

        # the first tile will be a number
        
        if len (_i) == 0 and tile%2 == 0: # tile contiens number

            return True
            
        elif len(_i) == 0 and tile%2 == 1: # tile contiens sign

            return False

        # last tile actived

        else:

            _l = self._active_tiles[-1]

            # after number is sign (or after sign is a number)
        
            if tile in dict_neighboring.get(_l):

                return True

        return False

