def main():
    '''
    '''
    command = input().split()
    stack = []
    
    while command[0] != 'exit':
        if command[0] == 'push':
            stack.append(int(command[1]))
            print('ok')
        elif command[0] == 'pop':
            if len(stack) != 0:
                print(stack.pop())
            else:
                print("error")
        elif command[0] == 'back':
            print(stack[-1])
        elif command[0] == 'size':
            print(len(stack))
        elif command[0] == 'clear':
            stack = []
            print('ok')
            
        command = input().split()
        
    print("bye ")
    
        
if __name__ == '__main__':
	main()