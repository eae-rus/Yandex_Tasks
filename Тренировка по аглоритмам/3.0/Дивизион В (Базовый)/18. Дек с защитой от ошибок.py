from collections import deque

def main():
    mydeque = deque()
    command = input().split()
    
    while command[0] != 'exit':
        if command[0] == 'push_front':
            n = int(command[1])
            mydeque.appendleft(n)
            print('ok')
        elif command[0] == 'push_back':
            n = int(command[1])
            mydeque.append(n)
            print('ok')
        elif command[0] == 'pop_front':
            if mydeque:
                print(mydeque.popleft())
            else:
                print('error')
        elif command[0] == 'pop_back':
            if mydeque:
                print(mydeque.pop())
            else:
                print('error')
        elif command[0] == 'front':
            if mydeque:
                print(mydeque[0])
            else:
                print('error')
        elif command[0] == 'back':
            if mydeque:
                print(mydeque[-1])
            else:
                print('error')
        elif command[0] == 'size':
            print(len(mydeque))
        elif command[0] == 'clear':
            mydeque.clear()
            print('ok')
            
        command = input().split()
        
    print("bye")
    
if __name__ == '__main__':
	main()