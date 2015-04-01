
class Tile:
    """Generic Tile component;"""
    # background color
    BGCOLOR = "black"
    # font style
    FONT = "sans 35"
    # dims 
    WIDTH = 100     # pixels
    # coords
    X = 0
    Y = 0

    def __init__(self, master, **kw):
    
        # public inits
        self.bgcolor = kw.get("bgcolor", self.BGCOLOR)
        self.ftcolor = "white" if self.bgcolor=="black" else "black"
        self.font = kw.get("font", self.FONT)
        self.width = kw.get("width", self.WIDTH)
        self.x = kw.get("x", self.X)
        self.y = kw.get("y", self.Y)

        # private members
        self.__tk_owner = master
        self.__txt_tile = kw.get("text", 0)

        # widget inits
        self.init_widget()

    def init_widget(self):
        "init's main widget."
        
        # shortcuts
        _x, _y = self.x, self.y       # coords
        _wid = self.width             # width and height tile  
        _bg = self.bgcolor            # background color
        _fc = self.ftcolor            # font color
        _fs = self.font               # font style

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


