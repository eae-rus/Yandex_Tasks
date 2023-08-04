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
        
        # -------------------------------------
        # поиск победителей
        is_win_cross = False
        is_win_zero = False
        # проверка по x
        for i in range (3):
            if (list_points[i][0] != 0) and (list_points[i][0] == list_points[i][1]) and (list_points[i][1] == list_points[i][2]):
                if list_points[i][0] == 1: # крестик
                    is_win_cross = True
                else: # нолик (другого быть не может, так как 0 проверили)
                    is_win_zero = True
        
        # проверка по y
        for i in range (3):
            if (list_points[0][i] != 0) and (list_points[0][i] == list_points[1][i]) and (list_points[1][i] == list_points[2][i]):
                if list_points[0][i] == 1: # крестик
                    is_win_cross = True
                else: # нолик (другого быть не может, так как 0 проверили)
                    is_win_zero = True
        
        # -------------------------------------
        # проверка по диагоналям
        if (list_points[0][0] != 0) and (list_points[0][0] == list_points[1][1]) and (list_points[1][1] == list_points[2][2]):
            if list_points[0][0] == 1: # крестик
                is_win_cross = True
            else: # нолик (другого быть не может, так как 0 проверили)
                is_win_zero = True
        if (list_points[0][2] != 0) and (list_points[0][2] == list_points[1][1]) and (list_points[1][1] == list_points[2][0]):
            if list_points[0][2] == 1: # крестик
                is_win_cross = True
            else: # нолик (другого быть не может, так как 0 проверили)
                is_win_zero = True

        # -------------------------------------
        # проверка, что нет одновременно двух победителей
        if is_win_cross and is_win_zero:
            return False

        # -------------------------------------
        # проверка  что после победы нет хода
        if is_win_cross and (diff != 1):
            return False
        elif is_win_zero and (diff != 0):
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