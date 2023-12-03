
def main():
    '''
    '''
    str_1 = input()
    str_2 = input()
    if len(str_1) != len(str_2):
        print("NO")
    else:
        dict_1 = {}
        for symbol in str_1:
            if symbol in dict_1:
                dict_1[symbol] += 1
            else:
                dict_1[symbol] = 1
        dict_2 = {}
        for symbol in str_2:
            if symbol in dict_2:
                dict_2[symbol] += 1
            else:
                dict_2[symbol] = 1
        
        is_equal = True    
        for symbol in dict_1.keys():
            if symbol in dict_2:
                if dict_1[symbol] != dict_2[symbol]:
                    is_equal = False
                    break
            else:
                is_equal = False
                break
            
        if is_equal:
            print("YES")
        else:
            print("NO")
        
if __name__ == '__main__':
	main()