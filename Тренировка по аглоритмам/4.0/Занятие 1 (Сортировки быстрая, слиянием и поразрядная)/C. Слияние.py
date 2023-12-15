import random
 
def main():
    '''
    '''
    
    N = int(input())
    arr_N = list(map(int, input().split()))
    M = int(input())
    arr_M = list(map(int, input().split()))
    
    arr = []
    i, j = 0, 0
    while i < N and j < M:
        if arr_N[i] < arr_M[j]:
            arr.append(arr_N[i])
            i += 1
        else:
            arr.append(arr_M[j])
            j += 1

    while i < N:
        arr.append(arr_N[i])
        i += 1
    
    while j < M:
        arr.append(arr_M[j])
        j += 1
    
    print(" ".join(map(str, arr)))
            
if __name__ == '__main__':
	main()