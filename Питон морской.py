import random
 
pole =[["O"]*10 for z in range(10)]

def choose_coordinates(count):
    flat = random.randint(0, 1)
    if flat == 0:
        x = random.randint(0, 9)
        y = random.randint(0, 9-count)
        y_list = []
        t = 0
        for t in range(count):
            y_list.append(y+t)
            t += 1
        return x, y_list
    else:
        x = random.randint(0, 9-count)
        y = random.randint(0, 9)
        x_list = []
        t = 0
        for t in range(count):
            x_list.append(x+t)
            t += 1
        return x_list, y


        
def check_coordinates(count):
    coord = choose_coordinates(count)
    state = 0
    x = coord[0]
    y = coord[1]
    if type(x) == list:
        for char in x:
            if pole[char][y] == "О":
                state = 0
                break
            else:
                state = 1
    else:
        for char in y:
            if pole[x][char] == "О":
                state = 0
                break
            else:
                state = 1
    if state == 1:            
        return x, y
    
def set_coordinates(count):
    coord = check_coordinates(count)
    if coord != None:
        x = coord[0]
        y = coord[1]
        if type(x) == list:
            for char in x:
                pole[char][y] = str(count)
        else:
            for char in y:
                pole[x][char] = str(count)
        return 1
    else:
        return 0

def change_pole():
    for i in range(10):
        for j in range(10):
            if pole[i][j].isdigit() and i != 0 and pole[i-1][j] == "O":
                pole[i-1][j] = "О"
            if  pole[i][j].isdigit() and j != 0 and pole[i][j-1] == "O":
                pole[i][j-1] = "О"
            if  pole[i][j].isdigit() and i != 9 and pole[i+1][j] == "O":
                pole[i+1][j] = "О"
            if  pole[i][j].isdigit() and j != 9 and pole[i][j+1] == "O":
                pole[i][j+1] = "О"
            if  pole[i][j].isdigit() and i != 0 and j != 0 and pole[i-1][j-1] == "O":
                pole[i-1][j-1] = "О"
            if  pole[i][j].isdigit() and i != 0 and j != 9 and pole[i-1][j+1] == "O":
                pole[i-1][j+1] = "О"
            if  pole[i][j].isdigit() and i != 9 and j != 0 and pole[i+1][j-1] == "O":
                pole[i+1][j-1] = "О"
            if  pole[i][j].isdigit() and i != 9 and j != 9 and pole[i+1][j+1] == "O":
                pole[i+1][j+1] = "О"
            
             
def set_ship(decks, count):
    for w in range(count):
        state = 0
        while state == 0:
            f = set_coordinates(decks)
            if f== 1:
                state = 1
            change_pole()
    
    
set_ship(1,4)
set_ship(2, 3)
set_ship(3, 2)
set_ship(4,1)

for i in range(10):
    print(end='\n')
    for j in range(10):
        print(pole[i][j], end=' ')
print(end='\n')

alf = {0 : 'o', 1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e', 6 : 'f', 7 : 'g', 8 : 'h', 9 : 'i', 10 : 'j'}

gamer = [['o']*11 for z in range(11)]

for i in range(len(gamer)):
  for j in range(len(gamer)):
    if i == 0:
      gamer[i][j] = alf[j]
    if j == 0:
      gamer[i][j] = i

gamer[0][0]="X" 

countwhole = 0
wintrig = 0
x = 0
y = 0
print(end='\n')

while wintrig != 1:
  countwhole = 0
  for i in range(11):
    print(end='\n')
    for j in range(11):
        print(gamer[i][j], end=' ')
  print(end='\n')
  try:
    y = (input('Введите столбец '))
    x= int(input('Введите строку '))
    for i in (alf):
        if alf[i] == y:
          y = i
    if (type(x) is int) and (x > 0) and (x < 11) and (type(y) is int):
      if not pole[x-1][y-1].isdigit():
        gamer[x][y] = '*'
        print(end='\n')
        print('Мимо!')
      else:
        gamer[x][y] = '@'
        print(end='\n')
        print('Попадание!')
        wholecount = 0
        up=down=left=right=1
        if x-up > 0:
          while pole[x-up-1][y-1]==pole[x-1][y-1]:
            if gamer[x-up][y] != '@':
                wholecount += 1
            up +=1
        if x+down < 11:
          while pole[x+down-1][y-1]==pole[x-1][y-1]:
            if gamer[x+down][y] != '@':
                wholecount += 1
            down += 1
        if y-left > 0:
          while pole[x-1][y-left-1]==pole[x-1][y-1]:
            if gamer[x][y-left] != '@':
                wholecount += 1
            left += 1
        if y+right < 11:
          while pole[x-1][y+right-1]==pole[x-1][y-1]:
            if gamer[x][y+right] != '@':
              wholecount += 1
            right += 1  
            
        if wholecount > 0:
          print(end='\n')
          print('Корабль подбит')
        else:
          print(end='\n')
          print('Вы потопили корабль') 
      for i in range(10):
        for j in range(10):
            if pole[i][j].isdigit():
              countwhole += 1
      if countwhole == 0:
        wintrig = 1
      print(end='\n')
    else:
      print(end='\n')
      print('Введены неверные координаты!')
  except IndexError:
        print(end="\n" "Вы ввели неправильные координаты, попробуйте снова")
        continue
  except ValueError:
        print(end="\n" "Вы ввели неправильные координаты, попробуйте снова")
        continue 
print(end='\n')
print('Вы победили')
