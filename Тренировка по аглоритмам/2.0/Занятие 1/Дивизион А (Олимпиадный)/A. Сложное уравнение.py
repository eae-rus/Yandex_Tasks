def main():
    '''
    '''
    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    
    if a == 0:
        print("INF")
    elif b == 0: # answer = 0
        if d == 0:
            print("NO")
        else:
            print(0)
    else:
        answer = -b / a
        if c * answer + d == 0:
            print('NO')
        else:
            if answer % 1 == 0:
                print(int(answer))
            else:
                print("NO")

if __name__ == '__main__':
	main()