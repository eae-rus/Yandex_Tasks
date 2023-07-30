def main():
    '''
    '''
    def is_right_situation(list_points):
        # проверка на количество точек
        count_cross = 0
        count_zero = 0
        for points in list_points:
            for point in points:
                if point == 1:
                    count_cross += 1
                elif point == 2:
                    count_zero += 1
        diff = count_cross - count_zero
        if diff > 1 or diff < 0:
            return False
        
        # проверка на ситуацию по количеству линий одинаковых цифр
        count_equal_lines = 0
        is_equal_lines_cross = False
        is_equal_lines_zero = False
        for i in range (3):
            # проверка по x
            equal_lines_x = True
            for j in range(2):
                if (list_points[i][j] != list_points[i][j+1]) or list_points[i][j] == 0:
                    equal_lines_x = False
                    break
            if equal_lines_x:
                count_equal_lines += 1
                if list_points[i][0] == 1: # крестик
                    is_equal_lines_cross = True
                else: # нолик
                    is_equal_lines_zero = True
                
            # проверка по y
            equal_lines_y = True
            for j in range (2):
                if (list_points[j][i] != list_points[j+1][i]) or list_points[j][i] == 0:
                    equal_lines_y = False
                    break
            if equal_lines_y:
                count_equal_lines += 1
                if list_points[0][i] == 1: # крестик
                    is_equal_lines_cross = True
                else: # нолик
                    is_equal_lines_zero = True
                
        if count_equal_lines > 1:
            return False
        
        # проверка обобщения
        if is_equal_lines_cross and (diff != 1):
            return False
        elif is_equal_lines_zero and (diff != 0):
            return False
                
        return True
    
    
    list_points = []
    for _ in range(3):
        x1, x2, x3 = map(int, input().split())
        points_local = [x1, x2, x3]
        list_points.append(points_local)

    if is_right_situation(list_points):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
	main()