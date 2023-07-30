def main():
    '''
    '''
    def is_parallegramm(points):
        def number_x_equal(sorted_points):
            # по x первая линия
            diff_x_line_1_2 = sorted_points[1][0] - sorted_points[0][0]
            diff_x_line_1_3 = sorted_points[2][0] - sorted_points[0][0]
            # по x вторая линия
            diff_x_line_2_4 = sorted_points[3][0] - sorted_points[1][0]
            diff_x_line_3_4 = sorted_points[3][0] - sorted_points[2][0]
            
            if diff_x_line_1_2 == diff_x_line_3_4:
                return (0, 1, 2, 3)
            elif diff_x_line_1_3 == diff_x_line_2_4:
                return (0, 2, 1, 3)
            else:
                return (-1, -1, -1, -1)
        
        def is_y_line_equal(sorted_points, points_number):
            if points_number[0] == -1:
                return False
            
            diff_x_line_1 = sorted_points[points_number[1]][0] - sorted_points[points_number[0]][0]
            
            diff_y_line_1 = sorted_points[points_number[1]][1] - sorted_points[points_number[0]][1]
            diff_y_line_2 = sorted_points[points_number[3]][1] - sorted_points[points_number[2]][1]
            if (diff_y_line_1 == diff_y_line_2):
                return True
            elif (diff_y_line_1 == - diff_y_line_2) and (diff_x_line_1 == 0):
                return True
            else:
                return False
        
        set_x = set((points[0][0], points[1][0], points[2][0], points[3][0]))
        set_y = set((points[0][1], points[1][1], points[2][1], points[3][1]))
        if len(set_x) <= 2 or len(set_y) <= 2 or len(set_x) != len(set_y):
            False

        sorted_points = sorted(points)
        # поиск линий по оси "x"
        points_number = number_x_equal(sorted_points)
        # проверка условий параллелаграмма
        return is_y_line_equal(sorted_points, points_number)

    N = int(input())
    list_points = []
    for _ in range(N):
        x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
        points_local = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
        list_points.append(points_local)

    for points in list_points:
        if is_parallegramm(points):
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
	main()