def main():
    '''
    '''
    X_str = input()
    Z_str = input()
    
    X_print_str = X_str
    #FIXME: можно сперва посчитать требуемое увеличение
    while len(X_print_str) < len(Z_str):
        X_print_str = X_print_str + X_str 
        
    tear_off_count = 0
    is_found_tear_off = False
    for i in range(len(X_print_str)):
        if len(X_print_str) - i <= len(Z_str):
            if X_print_str[i:] == Z_str[:len(X_print_str) - i]:
                tear_off_count = i
                is_found_tear_off = True
                break
    
    left_len = 0
    if is_found_tear_off:
        left_len = len(X_print_str) - tear_off_count
    print(Z_str[left_len:])
    
if __name__ == '__main__':
	main()