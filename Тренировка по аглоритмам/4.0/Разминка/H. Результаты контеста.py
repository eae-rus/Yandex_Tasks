def main():
    '''
    '''
    a = int(input())
    b = int(input())
    n = int(input())
    
    # a_n = a при условии, что каждый решил лишь по 1 задачке 
    b_n = b // n # при условии что все решили по n задач
    if b % n != 0: # проверка остатка
        b_n += 1
        
    if a > b_n:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
	main()