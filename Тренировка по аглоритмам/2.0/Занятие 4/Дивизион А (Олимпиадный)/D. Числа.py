def main():
    '''
    '''
    A = input()
    A_arr = [0]*10
    for letter in A:
        A_arr[int(letter)] += 1
            
    B = input()
    B_arr = [0]*10
    for letter in B:
        B_arr[int(letter)] += 1
    
    answer = []
    for i in range(9, -1, -1):
        if i == 0 and len(answer) == 0:
            numbers = min(A_arr[i],B_arr[i])
            if numbers > 0:
                answer.append(i)
        else:
            numbers = min(A_arr[i],B_arr[i])
            for j in range(numbers):
                answer.append(i)

    if len(answer) == 0:
        print(-1)
    else:
        print(''.join(map(str, answer)))
        


    
if __name__ == '__main__':
	main()