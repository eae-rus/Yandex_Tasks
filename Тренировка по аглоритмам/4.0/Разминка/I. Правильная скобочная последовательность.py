def main():
    '''
    '''
    square = input()
    stack = []
    
    for i in range(len(square)):
        if square[i] in ['(', '[', '{']:
            stack.append(square[i])
        elif square[i] in [')', ']', '}']:
            if len(stack) == 0:
                print('no')
                return
            
            last_bracket = stack.pop()
            
            if (square[i] == ')' and last_bracket != '(') or \
                (square[i] == ']' and last_bracket != '[') or \
                (square[i] == '}' and last_bracket != '{'):
                print('no')
                return
    
    if len(stack) == 0:
        print('yes')
    else:
        print('no')

if __name__ == '__main__':
    main()