# TODO: Write doc here
from typing import Tuple

import numpy as np


class Figure:
    def _get_num_represent(self) -> int:
        return self.num_represent

    def __int__(self) -> int:
        return self._get_num_represent()

    def __str__(self):
        if isinstance(self, Empty):
            return " "

        if isinstance(self, Cross):
            return "X"

        if isinstance(self, Zero):
            return "O"

        return "Based figure"


class Empty(Figure):
    def __init__(self):
        self.num_represent = 0


class Cross(Figure):
    def __init__(self):
        self.num_represent = 1


class Zero(Figure):
    def __init__(self):
        self.num_represent = 2


class TicTacToe:
    def __init__(self):
        gf: Tuple[Tuple[Figure]] = ((Empty(), Empty(), Empty()),
                                    (Empty(), Empty(), Empty()),
                                    (Empty(), Empty(), Empty()))

        self.game_field = np.array(gf, dtype=object)

    def __str__(self):
        res_str = ""

        for row in self.game_field:
            res_str += "[ "

            for figure in row:
                res_str += f"{figure} "

            res_str += "]\n"

        return res_str


print(TicTacToe())
