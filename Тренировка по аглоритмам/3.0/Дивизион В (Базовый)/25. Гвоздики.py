def main():
    def min_len_thread(n, carnations):
        if n == 0 or n == 1:
            return carnations[1] - carnations[0]
        
        return min(min_len_thread(n-1, carnations), min_len_thread(n-2, carnations)) + (carnations[n] - carnations[n-1])
    
    N = int(input())
    carnations = list(map(int, input().split()))
    carnations.sort()
        
    print(min_len_thread(N-1, carnations))
    
        
if __name__ == '__main__':
	main()
