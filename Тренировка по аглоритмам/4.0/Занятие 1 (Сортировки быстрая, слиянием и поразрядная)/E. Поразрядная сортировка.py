def main():
    '''
    '''
    N = int(input())
    arr_str = [input() for _ in range(N)]
    print("Initial array:")
    print(", ".join(arr_str))
    print("**********")
    
    len_str = len(arr_str[0]) # так как длины всех элементов одинаковы
    bucket = [[] for _ in range(10)]
    for bitwise in range(len_str):
        for k in range(N):
            bucket[int(arr_str[k][-1-bitwise])].append(arr_str[k])
        arr_str = []
        
        print("Phase {}".format(bitwise+1))
        for k in range(10):
            arr_str.extend(bucket[k])
            if len(bucket[k]) > 0:
                print("Bucket {}: ".format(k) + ", ".join(bucket[k]))
            else:
                print("Bucket {}: ".format(k) + "empty")
            bucket[k] = []
            
        print("**********")
    
    print("Sorted array:")
    print(", ".join(arr_str))
        
if __name__ == '__main__':
	main()