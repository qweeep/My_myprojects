#объявление переменных для работы
pole = [["*"] * 9 for z in range(8)]
up = ["    ","r", "n", "b", "q", "k", "b", "n", "r"] 
digit = ["8","7","6","5","4","3","2","1"]
alph = "     A  B  C  D  E  F  G  H"
alp = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]
down = ["    ", "R", "N", "B", "K", "Q", "B", "N", "R"]
first = ["    ", "p", "p", "p", "p", "p", "p", "p", "p"]
second = ["   ", "P", "P", "P", "P", "P", "P", "P", "P"]
chess = ["♖","♘" ,"♗","♕","♔","♙","♜", "♞","♝","♛", "♚", "♟︎ "]
figures = ["r","n","b","q","k","p","R","N","B","Q","K","P"]
game = 1
state = 1

#расстановка шахмат на доску
for i in range(8):
    for j in range(9):
        if i != 1 and i!=6 and i != 0 and i !=7:
            continue
        elif i == 0:
            pole[i][j] = up[j]
        elif i == 7:
            pole[i][j] = down[j]
        elif i == 1:
            pole[i][j] = first[j]
        else:
            pole[i][j] = second[j]

#установление номеров полей
for i in range(8):
    pole[i][0] = str(8-i) + "   " 

#текст при старте программы

print("Игра - шахматы")
print(end="\n")
print("Заглавными буквами обозначены белые фигуры, прописными соответвенно черные.")
print(end="\n")

#функция для движения пешек
def peshka(st, x, y, new_x, new_y, enemy):
#st=1 - белая фигура
    if st == 1:
        #проверка поля для движения на одну клетку 
        if new_x == x+1 and new_y == y and pole[8 - new_x][new_y] == "*":
            pole[8 - new_x][new_y] = "P"
            pole[8 - x][y] = "*"
            play = 0
        #проверка поля для движения на две клетки
        elif new_x == x + 2 and new_y == y and pole[8 - new_x][new_y] == "*" and x == 2:
            pole[8 - new_x][new_y] = "P"
            pole[8 - x][y] = "*"
            play = 0
        #проверка поля для атаки пешкой
        elif (new_x == x+1 and new_y == y -1 and pole[8 - new_x][new_y] in enemy) or (new_x == x +1 and new_y == y +1 and pole[8 - new_x][new_y] in enemy):
           pole[8 - new_x][new_y] = "P"
           pole[8- x][y] = "*"
           play = 0
        else:
            print("Неправильно введены координаты, попробуйте снова")
            play = 1
    #аналогичные условия для черной пешки
    else:
        if new_x == x-1 and new_y == y and pole[8 - new_x][new_y] == "*":
            pole[8 - new_x][new_y] = "p"
            pole[8 - x][y] = "*"
            play = 0
        elif  new_x == x-2 and new_y == y and pole[8 - new_x][new_y] == "*" and x == 7:
           pole[8 - new_x][new_y] = "p"
           pole[8 - x][y] = "*"
           play = 0
        elif (new_x == x-1 and new_y == y -1 and pole[8 - new_x][new_y] in enemy) or (new_x == x -1 and new_y == y +1 and pole[8 - new_x][new_y] in enemy):
           pole[8 - new_x][new_y] = "p"
           pole[8- x][y] = "*"
           play = 0
        else:
           print("Неправильно введены координаты, попробуйте снова")
           play = 1
    return play
    
#функция для движения коня
def horse(st, x, y, new_x, new_y, enemy):
    #все возможные варианты ходьбы конем
    if ((new_x == x + 2 and new_y == y + 1) or
    (new_x == x + 2 and new_y == y - 1) or
    (new_x == x - 2 and new_y == y + 1) or
    (new_x == x - 2 and new_y == y - 1) or
    (new_x == x + 1 and new_y == y + 2) or
    (new_x == x + 1 and new_y == y - 2) or
    (new_x == x - 1 and new_y == y + 2) or
    (new_x == x - 1 and new_y == y - 2)) and pole[8-new_x][new_y] == "*" or pole[8-new_x][new_y] in enemy:
        #расстановка значений в зависимости от цвета
        if st == 1:
            pole[8-new_x][new_y] = "N"
            pole[8 - x][y] = "*"
            play = 0
        else:
            pole[8-new_x][new_y] = "n"
            pole[8 - x][y] = "*"
            play = 0
    else:
        print("Неправильно введены координаты, попробуйте снова")
        play = 1
    return play
        
#функция для движения ладьи 
def rook(st, x, y, new_x, new_y, enemy):
    if st == 1:
        fig = "R"
    else:
        fig = "r"
    if new_y == y:
        if x > new_x:
            bg = x 
            lit = new_x
        else:
            bg = new_x 
            lit = x 
        for i in range(lit+1, bg):
            if (pole[8 - i][y] == "*" and (pole[8-new_x][y] == "*" or pole[8-new_x][y] in enemy)) or (pole[8-new_x][y] in enemy and abs(new_x - x) == 1):
                pole[8-new_x][y] = fig
                pole[8-x][y] = "*"
                play = 0
            else:
                print("Неправильно введены координаты, попробуйте снова")
                play = 1
                break
    return play 

#основной цикл
while game:
    if state == 1:
        #обозначение вражеских и союзных фигур
        enemy = up + first
        friend = down + second
    else:
        friend = up + first
        enemy = down + second
    #вывод игрового поля
    print(alph)
    for i in range(8):
        print(end="\n")
        for j in range(9):
            if pole[i][j] in figures:
                print(chess[figures.index(pole[i][j])].center(2), end=" ")
                continue 
            else:
                print(pole[i][j].center(2), end=" ")
            
                
    print(end="\n")
    if state == 1:
        color = "белыми"
    else:
        color = "черными"
    coord = input("Введите позицию фигуры для хода "+color+":")
    coord = coord.upper()
    #нахождение фигуры на введенной клетке
    if coord[0] in alp and len(coord) > 1 and coord[1] in digit and coord[0] != " ":
        current_unit = pole[digit.index(coord[1])][alp.index(coord[0])]
    else:
        print("Неправильно введены координаты, попробуйте снова")
        print(end="\n")
        continue 
#проверка на возможность хода введенной фигурой
    if current_unit not in friend:
        print("На указанной координате нет возможной фигуры для хода, попробуйте снова")
        print(end="\n")
        continue 
    else:
        play = 1
        #введение координат для хода фигурой
        new_coord = input("Введите координаты для хода:")
        new_coord = new_coord.upper()
        #проверка корректности координаты
        if new_coord[0] in alp and len(new_coord) > 1 and new_coord[0] != " " and coord[1] in digit:
            if current_unit == "p" or current_unit == "P":
                play = peshka(state, int(coord[1]), alp.index(coord[0]),  int(new_coord[1]), alp.index(new_coord[0]), enemy)
            elif current_unit == "N" or current_unit == "n":
                play = horse(state, int(coord[1]), alp.index(coord[0]),  int(new_coord[1]), alp.index(new_coord[0]), enemy)
            else:
                play = rook(state, int(coord[1]), alp.index(coord[0]),  int(new_coord[1]), alp.index(new_coord[0]), enemy)
        else:
            print("Неправильно введены координаты, попробуйте снова")
            play = 1
            continue
     #смена сторон для хода   
    if state == 1 and play == 0:
        state = 2
    elif state == 2 and play == 0:
        state = 1
    else:
        continue
        