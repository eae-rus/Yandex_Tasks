def main():
    '''
    '''
    S = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    C_dict = {}
    for k in range(1, len(C)):
        if C[k] not in C_dict:
            C_dict[C[k]] = k

    is_find = False
    ansewer = []
    for i in range(1, len(A)):
        for j in range(1, len(B)):
            remains = S - A[i] - B[j]
            if remains > 0:
                if remains in C_dict:
                    ansewer = [i-1, j-1, C_dict[remains]-1]
                    is_find = True
                    break
        if is_find:
            break
        
    if is_find:
        print(" ".join(map(str, ansewer)))
    else:
        print('-1')
    
if __name__ == '__main__':
	main()