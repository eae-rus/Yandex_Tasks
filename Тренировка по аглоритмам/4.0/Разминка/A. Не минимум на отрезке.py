def main():
    N, M  = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    
    # делаем поиск без оптимизации
    
    for _ in range(M):
        L, R = list(map(int, input().split()))
        is_found = False
        for i in range(L+1, R+1):
            if arr[i] < arr[L]:
                is_found = True
                print(arr[L])
                break
            elif arr[i] > arr[L]:
                is_found = True
                print(arr[i])
                break
        if not is_found:
            print("NOT FOUND")
            
if __name__ == '__main__':
	main()