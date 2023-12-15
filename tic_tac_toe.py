import pygame
import sys

#импортируем pygame
pygame.init()

#переменные
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
BLUE = (0, 0, 255)
GRAY = (169, 169, 169)
WHITE = (255, 255, 255)

#окно для игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")

#создаем игровое поле
board = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
turn = 'X'

#функция рисования сетки
def draw_grid():
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, GRAY, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)

#функция рисования крестиков и ноликов
def draw_symbols():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 'X': #крестики
                pygame.draw.line(screen, GRAY, (col * CELL_SIZE, row * CELL_SIZE),
                                 ((col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE), LINE_WIDTH)
                pygame.draw.line(screen, GRAY, ((col + 1) * CELL_SIZE, row * CELL_SIZE),
                                 (col * CELL_SIZE, (row + 1) * CELL_SIZE), LINE_WIDTH)
            elif board[row][col] == 'O': #нолики
                pygame.draw.circle(screen, WHITE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2),
                                   CELL_SIZE // 2 - LINE_WIDTH)

#функция проверки победителя
def check_winner():
    #проверка строк и столбца
    for i in range(GRID_SIZE):
        if all(board[i][j] == turn for j in range(GRID_SIZE)) or all(board[j][i] == turn for j in range(GRID_SIZE)):
            return True

    #проверка диагонали
    if all(board[i][i] == turn for i in range(GRID_SIZE)) or all(board[i][GRID_SIZE - 1 - i] == turn for i in range(GRID_SIZE)):
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
            clicked_row = mouseY // CELL_SIZE
            clicked_col = mouseX // CELL_SIZE

            #проверка пуста ли ячейка
            if board[clicked_row][clicked_col] == ' ':
                board[clicked_row][clicked_col] = turn

                #проверка победителя
                if check_winner():
                    print(f'{turn} wins!')
                    running = False
                elif all(board[i][j] != ' ' for i in range(GRID_SIZE) for j in range(GRID_SIZE)):
                    print('It\'s a draw!')
                    game = False
                else:
                    #определение стороны
                    turn = 'O' if turn == 'X' else 'X'

    #рисуем фон и сетку
    screen.fill(BLUE)
    draw_grid()

    #рисуем крестики и нолики
    draw_symbols()

    #обновляем дисплей
    pygame.display.flip()

#выход Pygame
pygame.quit()
sys.exit()
