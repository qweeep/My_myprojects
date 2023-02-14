import CheckerClass
import GUIClass
import BoolClass
import numpy as np
#import const

class Table:
    def __init__(self):
        self.table = np.array([])
        for i_index in range(8):
            for j_index in range(8):
                field = GUIClass.Field(j_index, i_index)
                self.table = np.append(self.table, field)
        self.table = np.reshape(self.table, (8, 8))

    def auto_fill(self):
        for color in ('white', 'black'):
            x,y= 0,0
            count = 0
            while count != 6:
                x = np.random.randint(0, 8)
                y = np.random.randint(1, 7)
                if self.table[y][x].possible_to_set():
                    checker = CheckerClass.Checker(color, x, y)
                    self.table[y][x].set_checker(checker)
                    count += 1

    def __str__(self):
        table = self.table
        print(" A B C D E F G H")
        for i in np.arange(table.shape[0] - 1, -1, -1):
            print("{}".format(i + 1), end="")
            for j in np.arange(table.shape[1]):
                print('{}'.format(table[i][j]), end="")
            print("{}".format(i + 1))
        print(" A B C D E F G H")
        return ''