def main():
    N = int(input())
    carnations = list(map(int, input().split()))
    carnations.sort()
    # обработка левой границы
    smin_len_thread = carnations[1] - carnations[0]
    i = 2
    # основной цикл
    while i < N-1:
        if carnations[i] - carnations[i-1] < carnations[i+1] - carnations[i]:
            smin_len_thread += carnations[i] - carnations[i-1]
            i += 1
        else:
            smin_len_thread += carnations[i+1] - carnations[i]
            i += 2
    # обработка правой границы
    if i == N-1:
        smin_len_thread += carnations[i] - carnations[i-1]
        
    print(smin_len_thread)
    
        
if __name__ == '__main__':
	main()
