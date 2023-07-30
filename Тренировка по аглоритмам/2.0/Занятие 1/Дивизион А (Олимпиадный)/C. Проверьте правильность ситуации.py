def main():
    '''
    '''
    def is_right_situation(list_points):
        def is_count_points_correct(list_points):
            '''
            проверка на количество точек
            '''
            count_1 = 0
            count_2 = 0
            for points in list_points:
                for point in points:
                    if point == 1:
                        count_1 += 1
                    elif point == 2:
                        count_2 += 1
            if abs(count_1 - count_2) > 1:
                return False
            return True
        
        def is_correct_lines_count(list_points):
            '''
            проверка на ситуацию по количеству линий одинаковых цифр
            '''
            count_equal_lines = 0
            for i in range (3):
                # проверка по x
                equal_lines_x = True
                for j in range(2):
                    if (list_points[i][j] != list_points[i][j+1]) or list_points[i][j] == 0:
                        equal_lines_x = False
                        break
                if equal_lines_x:
                    count_equal_lines += 1
                    
                # проверка по y
                equal_lines_y = True
                for j in range (2):
                    if (list_points[j][i] != list_points[j+1][i]) or list_points[j][i] == 0:
                        equal_lines_y = False
                        break
                if equal_lines_y:
                    count_equal_lines += 1
                    
            if count_equal_lines > 1:
                return False
            return True

        if is_count_points_correct(list_points) and is_correct_lines_count(list_points):
            return True
        else:
            return False
    
    
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