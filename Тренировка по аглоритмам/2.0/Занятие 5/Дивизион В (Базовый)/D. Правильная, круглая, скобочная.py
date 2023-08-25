def main():
    '''
    '''
    bracket_string = input()
    is_correct = True
    bracket_counter = 0
    for bracket in bracket_string:
        if bracket == '(':
            bracket_counter += 1
        elif bracket == ')':
            bracket_counter -= 1
        if bracket_counter < 0:
            is_correct = False
            break
    
    if is_correct and bracket_counter == 0:
        print('YES')
    else:
        print('NO')        

    
if __name__ == '__main__':
	main()