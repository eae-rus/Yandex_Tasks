

def main():
    def count_sequences(N):
        if N == 1:
            return 2
        elif N == 2:
            return 4
        
        dp0 = 2
        dp1 = 1
        dp2 = 1
        for _ in range(2, N):
            dp0, dp1, dp2 = dp0 + dp1 + dp2, dp0, dp1

        return dp0 + dp1 + dp2

    N = int(input())
    result = count_sequences(N)
    print(result)

if __name__ == '__main__':
	main()