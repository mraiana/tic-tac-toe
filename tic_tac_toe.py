import pygame
import sys

#импортируем pygame
pygame.init()

#переменные
width, height = 300, 300
line_widht = 15
grid_size = 3
cell_size = width // grid_size
blue = (0, 0, 255)
gray = (169, 169, 169)
white = (255, 255, 255)

#окно для игры
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Крестики-нолики")

#создаем игровое поле
board = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
turn = 'X'

#функция рисования сетки
def draw_grid():
    for i in range(1, grid_size):
        pygame.draw.line(screen, gray, (i * cell_size, 0), (i * cell_size, height), line_widht)
        pygame.draw.line(screen, gray, (0, i * cell_size), (width, i * cell_size), line_widht)

#функция рисования крестиков и ноликов
def draw_symbols():
    for row in range(grid_size):
        for col in range(grid_size):
            if board[row][col] == 'X': #крестики
                pygame.draw.line(screen, gray, (col * cell_size, row * cell_size),
                                 ((col + 1) * cell_size, (row + 1) * cell_size), line_widht)
                pygame.draw.line(screen, gray, ((col + 1) * cell_size, row * cell_size),
                                 (col * cell_size, (row + 1) * cell_size), line_widht)
            elif board[row][col] == 'O': #нолики
                pygame.draw.circle(screen, white, (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2),
                                   cell_size // 2 - line_widht)

#функция проверки победителя
def check_winner():
    #проверка строк и столбца
    for i in range(grid_size):
        if all(board[i][j] == turn for j in range(grid_size)) or all(board[j][i] == turn for j in range(grid_size)):
            return True

    #проверка диагонали
    if all(board[i][i] == turn for i in range(grid_size)) or all(board[i][grid_size - 1 - i] == turn for i in range(grid_size)):
        return True

    return False

game = True

#игровой цикл
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseY // cell_size
            clicked_col = mouseX // cell_size

            #проверка пуста ли ячейка
            if board[clicked_row][clicked_col] == ' ':
                board[clicked_row][clicked_col] = turn

                #проверка победителя
                if check_winner():
                    print(f'{turn} wins!')
                    running = False
                elif all(board[i][j] != ' ' for i in range(grid_size) for j in range(grid_size)):
                    print('It\'s a draw!')
                    game = False
                else:
                    #определение стороны
                    turn = 'O' if turn == 'X' else 'X'

    #рисуем фон и сетку
    screen.fill(blue)
    draw_grid()

    #рисуем крестики и нолики
    draw_symbols()

    #обновляем дисплей
    pygame.display.flip()

#выход Pygame
pygame.quit()
sys.exit()
