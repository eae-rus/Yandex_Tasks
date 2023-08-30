def main():
    '''
    '''
    N = int(input())
    K = int(input())
    row_number_Petya = int(input())
    left_or_right = int(input())
    
    position_Petya = 0
    if left_or_right == 1:
        position_Petya = 2 * row_number_Petya - 1
    else:
        position_Petya = 2 * row_number_Petya
    
    position_Vasya = -1
    if position_Petya + K <= N:
        position_Vasya = position_Petya + K
    elif position_Petya - K >= 1:
        position_Vasya = position_Petya - K
    
    row_and_column = [-1, -1]
    if position_Vasya > 0:
        if position_Vasya % 2 == 0:
            row_and_column[0] = position_Vasya // 2
            row_and_column[1] = 2
        else:
            row_and_column[0] = 1 + position_Vasya // 2
            row_and_column[1] = 1
    
    if row_and_column[0] == -1:
        print(-1)
    else:
        print(' '.join(map(str, row_and_column)))

     
if __name__ == '__main__':
	main()