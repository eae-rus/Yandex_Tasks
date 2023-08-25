def main():
    '''
    '''
    N,M = map(int, input().split())
    groups = list(map(int, input().split()))
    classrooms = list(map(int, input().split()))
    
    # Создание списка кортежей с элементами и их индексами
    indexed_groups = [(value, index+1) for index, value in enumerate(groups)]
    indexed_classrooms = [(value, index+1) for index, value in enumerate(classrooms)]
    
    # Сортировка списка кортежей по значениям элементов
    indexed_groups = sorted(indexed_groups)
    indexed_classrooms = sorted(indexed_classrooms)
    
    number_distributed_groups = 0
    groups_in_classroom = []
    i_group, i_classroom = 0, 0
    
    while i_group < N and i_classroom < M:
        if indexed_groups[i_group][0] < indexed_classrooms[i_classroom][0]:
            groups_in_classroom.append((indexed_groups[i_group][1], indexed_classrooms[i_classroom][1]))
            i_group += 1
            i_classroom += 1
            number_distributed_groups += 1
        else:
            i_classroom += 1
    
    for i in range(i_group, N):
        groups_in_classroom.append((indexed_groups[i][1], 0))
    
    print(number_distributed_groups)
    groups_in_classroom = sorted(groups_in_classroom)
    answer = []
    for _, classroom in groups_in_classroom:
        answer.append(classroom)
    print(' '.join(map(str, answer)))
    
if __name__ == '__main__':
	main()