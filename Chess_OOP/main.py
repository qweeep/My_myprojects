import GameClass
import os
from IPython.display import clear_output
import chess_hexa

class MainClass:

    def __init__(self, game):
        if game == 1:
            print('')
            print()
            print('Пример хода для атака: a5:c7')
            print('Пример обычного хода: a5-b6')
            print()
            self.session = GameClass.Game()

        elif game == 2:
            print('Пример обычного хода: a2 a4 или А2 А4')
            import Lehchess
        elif game == 3:
            print('Пример обычного хода: А.4.А.5')
            print()
            chess_hexa.Geks.go_game()

if __name__ == '__main__':
    print('1 -> Шашки')
    print('2 -> Шахматы')
    print('3 -> Гекагональные Шахматы')
    Game = int(input('Выберите игру: '))
    MainClass(Game)