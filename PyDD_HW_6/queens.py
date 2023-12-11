# 3. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# 4. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
import random

# Выглядит адекватно на досках меньше 10х10
def create_board(size: int):
    board = []
    for i in range(size + 1):
        if i == size:
            board.append([])
            for k in range(size + 1):
                if k == 0:
                    board[i].append("   ")
                else:
                    board[i].append(f" {k} ")
        else:
            board.append([])
            for j in range(size + 1):
                if j == 0:
                    board[i].append(f" {size - i} ")
                else:
                    board[i].append("[ ]")
    return board

# Для заданных пар чисел
def custom_placement(placement: list[int]):
    board = create_board(len(placement))
    for i in placement:
        board[len(placement) - i[0]][i[1]] = "[Q]"
    return board

# Случайная расстановка на заданной доске
def random_placement(board: list[int]):
    for i in range(len(board)):
        while i:
            j = random.randint(0, len(board) - 2)
            k = random.randint(1, len(board) - 1)
            if board[j][k] != "[Q]":
                board[j][k] = "[Q]"
                break
    return board

# Проверка расстановки
def queens_check(board: list[int]):
    row = set()
    column = set()
    pos_diag = set()
    neg_diag = set()
    
    for i in range(0, len(board) - 1):
        for j in range(1, len(board)):
            if board[i][j] == "[Q]":
                if i in row or j in column or (i + j) in pos_diag or (i - j) in neg_diag:
                    return False
                else:
                    row.add(i)
                    column.add(j)
                    pos_diag.add(i + j)
                    neg_diag.add(i - j)
    return True

# Четыре успешных расстановки на доске заданного размера
def four_valid_placements(size: int):
    
    for i in range(1, 5):
        print(i)
        while i:
            board = random_placement(create_board(size))
            if queens_check(board):
                print(queens_check(board))
                print_board(board)
                break
    
# Печать доски
def print_board(board: list[int]):
    print()
    for i in board:
        print(' '.join(i))
    print()
    

# Печать пустой доски:
print_board(create_board(8))

# Печать заданной расстановки:
print_board(custom_placement(placement = [[1, 3], [2, 5], [3, 2], [4, 8], [5, 1], [6, 7], [7, 4], [8, 6]]))

# Печать случайной расстановки:
print_board(random_placement(create_board(8)))

# С размером доски от 7 и более процесс очень долгий. Пример проверки случайных расстановок и вывода 4-х успешных на доске 5х5:
four_valid_placements(5)