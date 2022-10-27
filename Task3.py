# Создайте программу для игры в ""Крестики-нолики"".
#
# ---Объявление переменных---
from tkinter import *
import random
root = Tk()
root.title('Крестики-нолики')
game_run = True      # Если False - конец игры
field = []           # Двумер-й массив для кнопок игрового поля
cross_count = 0      # Кол-во ходов крестиком. При 5-ти - ничья
#
# ---Обработка нажатия кнопок---
def new_game():      # Вызов новой игры при нажатии кнопки
    for row in range(3):
        for col in range(3):
            field[row] [col] ['text'] = ' '     # Очищение полей от крестиков и нулей
            field[row] [col] ['background'] = 'lavender'  # Заполнение полей цветом
    global game_run   # Обращение к клобальным переменным 
    game_run = True   # и их обнуление
    global cross_count
    cross_count = 0
def click(row, col):    #  Функция нажатия на поле
    if game_run and field[row][col]['text'] == ' ':  # Если поле пустое
        field[row][col]['text'] = 'X'      # то ставим крестик
        global cross_count     # Считаем кол-во крестиков
        cross_count += 1
        check_win('X')     # Проверка победы
        if game_run and cross_count < 5:
            computer_move()   
            check_win('O')
#
# ---Проверка победы---
def check_win(smb):   # smb- Х или О 
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

def check_line(a1,a2,a3,smb):  # Проверка линий
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False

def can_win(a1,a2,a3,smb):  # Проверка попбеды
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res

def computer_move():   # Ход компьютера
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'X'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'X'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'X'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'X'):
        return
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break
#
# ---Графический интерфейс---
for row in range(3):
    line = []
    for col in range(3):
        button = Button(root, text=' ', width=4, height=2, 
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row,col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='new game', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew') # Упаковщик
root.mainloop()   # Бесконечный цикл