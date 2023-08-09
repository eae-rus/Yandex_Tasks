def main():
    '''
    '''
    def find_min_number(A):
        for i in range(0, 100):
            if A[i] == 1:
                return i
        return -1
    
    def calc_points(players_points, numbers_players_list, min_number):
        new_players_points = players_points[:]
        if min_number == -1:
            return new_players_points
        
        for i in range(len(numbers_players_list)):
            if numbers_players_list[i] == min_number:
                new_players_points[i] += min_number
        return new_players_points
    
    N = int(input())
    players_points = list(map(int, input().split()))
    numbers_players_list = list(map(int, input().split()))
    
    count_players_lower = 0
    min_number = 101
    
    A = [0] * 101
    for i in numbers_players_list:
        A[i] += 1
    
    max_number = max(numbers_players_list)
    if max_number < 100:
        max_number += 1
        
    for i in range(max_number, 0, -1):
        A[i] += 1
        numbers_players_list.append(i)
        min_i = find_min_number(A)
        new_players_points = calc_points(players_points, numbers_players_list, min_i)
        
        local_count_players_lower = 0
        for j in range(len(new_players_points)-1):
            if new_players_points[j] < new_players_points[-1]:
                local_count_players_lower += 1
        
        if local_count_players_lower >= count_players_lower:
            count_players_lower = local_count_players_lower
            min_number = i

        numbers_players_list.pop() 
        A[i] -= 1
    
    print(min_number)
    

    

    
if __name__ == '__main__':
	main()