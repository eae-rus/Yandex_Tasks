def main():
    '''
    '''
    n_max = int(input())
    A_list = [i+1 for i in range(n_max)]
    A_set = set(A_list)
    is_continue = True
    
    while is_continue:
        question = input()
        if question == 'HELP':
            is_continue = False
            continue
                    
        new_A_list = list(map(int, question.split()))
        count_new_A = 0
        for new_A in new_A_list:
            if new_A in A_set:
                count_new_A += 1
        
        if len(A_set) - count_new_A >= len(A_set) / 2: # больше или равно половине множества
            print('NO')
            for new_A in new_A_list:
                if new_A in A_set:
                    A_set.remove(new_A)
        else: # меньше половины множества
            print('YES')
            new_A_set = set()
            for new_A in new_A_list:
                if new_A in A_set:
                    new_A_set.add(new_A)
            A_set = new_A_set
    
    answer = ' '.join(str(x) for x in sorted(list(A_set)))
    print(answer)
    
if __name__ == '__main__':
	main()