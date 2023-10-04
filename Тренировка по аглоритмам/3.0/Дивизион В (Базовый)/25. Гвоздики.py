def main():
    N = int(input())
    carnations = list(map(int, input().split()))
    carnations.sort()
    # обработка левой границы
    number_connections_the_thread = [0, 0] # достаточно помнить 2 точки: 0 - две назад, 1 - одна назад
    smin_len_thread = carnations[1] - carnations[0]
    number_connections_the_thread[0], number_connections_the_thread[1] = 1, 1
    i = 2
    # основной цикл
    while i < N-1:
        if carnations[i] - carnations[i-1] < carnations[i+1] - carnations[i]:
            smin_len_thread += carnations[i] - carnations[i-1]
            number_connections_the_thread[1] += 1
            if number_connections_the_thread[0] == 2:
                smin_len_thread -= carnations[i-1] - carnations[i-2]
            
            number_connections_the_thread[0], number_connections_the_thread[1] = number_connections_the_thread[1], 1
            i += 1
        else:
            smin_len_thread += carnations[i+1] - carnations[i]
            number_connections_the_thread[0], number_connections_the_thread[1] = 1, 1
            i += 2
    # обработка правой границы
    if i == N-1:
        smin_len_thread += carnations[i] - carnations[i-1]
        if number_connections_the_thread[0] == 2:
                smin_len_thread -= carnations[i-1] - carnations[i-2]
        
    print(smin_len_thread)
    
        
if __name__ == '__main__':
	main()
