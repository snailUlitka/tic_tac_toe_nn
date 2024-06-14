# TODO: Write doc here
import numpy as np


class Figure:
    # TODO: Write doc here
    EMPTY = 0
    CROSS = 1
    ZERO = 2
    
    @staticmethod
    def get_str_repr(figure: int):
        match figure:
            case 0:
                return " "
            case 1:
                return "X"
            case 2:
                return "O"
        
        raise ValueError("Unknown figure")
    


class TicTacToe:
    # TODO: Write doc here
    def __init__(self):
        gf = ((Figure.EMPTY, Figure.EMPTY, Figure.EMPTY),
              (Figure.EMPTY, Figure.EMPTY, Figure.EMPTY),
              (Figure.EMPTY, Figure.EMPTY, Figure.EMPTY))

        self.game_field = np.array(gf, dtype=object)
        self.turn = 0
        
    def set_figure(self, x: int, y: int) -> bool:
        """Puts the figure on the playing field and returns True or False, 
        depending on whether it was possible to put the figure.

        Parameters
        ----------
        x : int
            number from 0 to 2 (included)
        y : int
            number from 0 to 2 (included)

        Returns
        -------
        bool
            Is the figure placed on the playing field or not.
        """
        if self.game_field[y, x] != Figure.EMPTY:
            return False
        
        if self.turn % 2 == 0:
            figure = Figure.CROSS
        else:
            figure = Figure.ZERO
        
        self.game_field[y, x] = figure
        self.turn += 1
        
        return True
    
    def get_figure(self, x: int, y: int) -> int:
        """Returns a shape by its coordinates

        Parameters
        ----------
        x : int
            number from 0 to 2 (included)
        y : int
            number from 0 to 2 (included)

        Returns
        -------
        int
            Figure (numerical representation)
        """
        return self.game_field[y, x]
    
    def check_win(self) -> bool:
        """Returns True if once of players wins."""
        dia_win = True
        inv_dia_win = True
        h_win = True
        v_win = True
        
        for i in (1, 2):
            dia_win &= self.get_figure(i, i) == self.get_figure(0, 0) \
                and self.get_figure(0, 0) != 0
            inv_dia_win &= self.get_figure(2 - i, i) == self.get_figure(2, 0) \
                and self.get_figure(2, 0) != 0
            
        if dia_win or inv_dia_win:
            return True
        
        for i in range(3):
            for j in (1, 2):
                h_win &= self.get_figure(j, i) == self.get_figure(0, i) \
                    and self.get_figure(0, i) != 0
                v_win &= self.get_figure(i, j) == self.get_figure(i, 0) \
                    and self.get_figure(i, 0) != 0

            if h_win or v_win:
                return True
        
        return False

    def __str__(self):
        res_str = ""

        for row in self.game_field:
            res_str += "[ "

            for figure in row:
                res_str += f"{Figure.get_str_repr(figure)} "

            res_str += "]\n"

        return res_str
