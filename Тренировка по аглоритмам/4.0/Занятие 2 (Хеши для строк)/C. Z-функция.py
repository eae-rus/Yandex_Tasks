def main():
    '''
    Источник идеи:
    https://e-maxx.ru/algo/z_function
    '''
    S = input()
    n = len(S)
    
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while (i + z[i] < n and S[z[i]] == S[i+z[i]]):
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
        
    print(' '.join(map(str, z)))
        
if __name__ == '__main__':
	main()