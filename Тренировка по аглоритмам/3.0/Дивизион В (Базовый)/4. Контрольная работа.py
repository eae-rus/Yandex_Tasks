def main():
    '''
    '''
    def calculate_row_and_column(position):
        row_and_column = [-1, -1]
        if position > 0:
            if position % 2 == 0:
                row_and_column[0] = position // 2
                row_and_column[1] = 2
            else:
                row_and_column[0] = 1 + position // 2
                row_and_column[1] = 1
        return row_and_column

    
    N = int(input())
    K = int(input())
    row_number_Petya = int(input())
    left_or_right = int(input())
    
    position_Petya = 0
    if left_or_right == 1:
        position_Petya = 2 * row_number_Petya - 1
    else:
        position_Petya = 2 * row_number_Petya
    
    position_Vasya_before, position_Vasya_after = -1, -1
    row_and_column_before, row_and_column_after = [-1, -1], [-1, -1]
    if position_Petya + K <= N:
        position_Vasya_before = position_Petya + K
        row_and_column_before = calculate_row_and_column(position_Vasya_before)
    if position_Petya - K >= 1:
        position_Vasya_after = position_Petya - K
        row_and_column_after = calculate_row_and_column(position_Vasya_after)
    
    row_and_column_best = [-1, -1]
    if row_and_column_before[0] != -1 and row_and_column_after[0] != -1:
        len_before = row_and_column_before[0] - row_number_Petya
        len_after = row_number_Petya - row_and_column_after[0]
        if len_before > len_after:
            row_and_column_best = row_and_column_after
        else: # len_1 <= len_2:
            row_and_column_best = row_and_column_before
    elif row_and_column_before[0] != -1:
        row_and_column_best = row_and_column_before
    elif row_and_column_after[0] != -1:
        row_and_column_best = row_and_column_after
    
    
    if row_and_column_best[0] == -1:
        print(-1)
    else:
        print(' '.join(map(str, row_and_column_best)))

     
if __name__ == '__main__':
	main()