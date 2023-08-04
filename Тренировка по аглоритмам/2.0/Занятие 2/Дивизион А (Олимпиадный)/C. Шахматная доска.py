def main():
    '''
    '''
    N = int(input())
    chess_board = [[False] * 8 for _ in range(8)]
    for _ in range(N):
        x, y = map(int, input().split())
        chess_board[x-1][y-1] = True
    
    perimeter = 0
    for i in range(8):
        for j in range(8):
            if chess_board[i][j]:
                # проверка снизу
                if i == 0 or not chess_board[i-1][j]:
                    perimeter += 1
                # проверка сверху
                if i == 7 or not chess_board[i+1][j]:
                    perimeter += 1
                # проверка слева
                if j == 0 or not chess_board[i][j-1]:
                    perimeter += 1
                # проверка справа
                if j == 7 or not chess_board[i][j+1]:
                    perimeter += 1
    
    print(perimeter)
    
if __name__ == '__main__':
	main()