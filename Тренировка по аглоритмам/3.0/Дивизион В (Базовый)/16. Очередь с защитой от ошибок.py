from queue import Queue

def main():
    queue = Queue()
    command = input().split()
    
    while command[0] != 'exit':
        if command[0] == 'push':
            n = int(command[1])
            queue.put(n)
            print('ok')
        elif command[0] == 'pop':
            if not queue.empty():
                print(queue.get())
            else:
                print('error')
        elif command[0] == 'front':
            if not queue.empty():
                print(queue.queue[0])
            else:
                print('error')
        elif command[0] == 'size':
            print(queue.qsize())
        elif command[0] == 'clear':
            while not queue.empty():
                queue.get()
            print('ok')
            
        command = input().split()
        
    print("bye")

if __name__ == '__main__':
	main()