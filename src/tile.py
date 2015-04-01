
class Tile:
    """Generic Tile component;"""

    def __init__(self, master, **kw):
    
        # public inits
        self.bgcolor = kw.get("bgcolor", "black")
        self.ftcolor = "white" if self.bgcolor=="black" else "black"
        self.font = kw.get("font", "sans 35")
        self.width = kw.get("width", 100)
        self.x = kw.get("x", 0)
        self.y = kw.get("y", 0)

        # private members
        self.__tk_owner = master
        self.__txt_tile = kw.get("text", 0)

        # widget inits
        self.init_widget(**kw)

    def init_widget(self, **kw):
        ""
        
        # coords
        _x, _y = self.x, self.y

        # width and height tile
        _wid = self.width

        # background color
        _bg = self.bgcolor

        # font color
        _fc = self.ftcolor

        # font style
        _fs = self.font

        # create rectangle (exactly square)
        self.rectangle = self.__tk_owner.create_rectangle(
            _x, _y, _x + _wid, _y + _wid, fill = _bg, width = 0
        )

        # create text in centre of rectangle
        self.__tk_owner.create_text (
            _x + _wid/2, _y + _wid/2, text = self.txt_tile, font=_fs, fill=_fc
            )

    @property
    def txt_tile(self):
        "returns value of private txt_tile;"

        return self.__txt_tile


    @txt_tile.setter
    def txt_tile(self, value):
        "set new value to private txt_tile;"

        self.__txt_tile = value


    def bgcolor(self, value):
        "set new value color to tile."

        self.bgcolor = value


