def main():
    '''
    '''
    sequence = input()
    stack = []
    
    answer = 'yes'
    for symbol in sequence:
        if symbol == '(' or symbol == '[' or symbol == '{':
            stack.append(symbol)
        else: # symbol == ')' or symbol == ']' or symbol == '}':
            if len(stack) == 0:
                answer = 'no'
                break
            if symbol == ')' and stack[-1] == '(':
                stack.pop()
            elif symbol == ']' and stack[-1] == '[':
                stack.pop()
            elif symbol == '}' and stack[-1] == '{':
                stack.pop()
            else:
                answer = 'no'
                break
    if len(stack) != 0:
        answer = 'no'
    
    print(answer)
    
        
if __name__ == '__main__':
	main()