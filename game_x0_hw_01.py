# Итоговое практическое задание «Крестики-нолики»
# https://github.com/dikobr
# ПРАВИЛА: todo_&_rules.txt

# Функционал печати поля
game_board = list(range(1, 10))  # создаем игровое поле


def print_game_board(board):
    # Выводим игровое поле в консоль
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-' * 13)


# Функция хода игрока
def player_input(player_symbol):
    valid = False
    # Проверка корректности ввода
    while not valid:
        request_position = input(f'Ходит игрок {player_symbol}. Введите номер поля: ')
        if request_position.isalnum():
            if request_position.isdecimal():
                request_position = int(request_position)
            else:
                print('Некорректный ввод. Нужно ввести число.')
                continue
        else:
            print('Некорректный ввод. Нужно ввести число.')
            continue

        if 1 <= request_position <= 9:
            if str(game_board[request_position - 1]) not in 'XO':
                game_board[request_position - 1] = player_symbol
                valid = True
            else:
                print('Это поле уже занято.')
        else:
            print('Некорректный ввод. Нужно ввести число от 1 до 9.')


# Функция проверяет, выиграл ли игрок
def check_win(board):
    # инициализация выигрышных координат
    win_coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    win_player = False
    for i in win_coordinates:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            win_player = board[i[0]]
    return win_player


# старт игры
def start_game(board):
    steps = 0  # Ходы
    win = False
    while not win:
        print_game_board(board)
        # Первым будет ходить всегда 'X'
        if steps % 2 == 0:
            player_input('X')
        else:
            player_input('O')
        steps += 1

        # Ждем, когда шагов станет больше 4, чтобы раньше времени не вызывать check_win
        if steps > 4:
            win_pl = check_win(board)
            if win_pl:
                print(f'Победил игрок {win_pl}!')
                win = True
                break

            if steps == 9:
                print('Игра окончена. Ничья!')
                break
    print_game_board(board)


print('*' * 5, 'Добро пожаловать в игру "Крестики-нолики"!', '*' * 5)
start_game(game_board)
