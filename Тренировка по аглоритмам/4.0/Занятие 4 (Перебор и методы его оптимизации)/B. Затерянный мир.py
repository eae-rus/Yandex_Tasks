def is_safe(board, row, col):
    # Проверка, может ли ферзь быть размещен на данной позиции
    # Проверяем вертикали, горизонтали и диагонали
    # Если есть конфликт, то возвращаем False
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def count_queen_placements(n):
    # Рекурсивная функция для подсчета количества расстановок ферзей
    def backtrack(board, col):
        if col >= n:
            # Базовый случай: все ферзи размещены
            return 1

        count = 0
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                count += backtrack(board, col + 1)
                board[i][col] = 0

        return count

    # Создаем пустую доску
    board = [[0] * n for _ in range(n)]

    # Вызываем рекурсивную функцию
    return backtrack(board, 0)

def main():
    # Вводим ширину поля
    n = int(input())

    # Вызываем функцию для подсчета количества расстановок ферзей
    count = count_queen_placements(n)
    print(count)

if __name__ == '__main__':
    main()