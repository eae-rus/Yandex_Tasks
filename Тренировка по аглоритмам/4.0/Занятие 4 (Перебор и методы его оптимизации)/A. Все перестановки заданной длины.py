def main():
    '''
    '''
    def permutation(answer, arr):
        if len(arr) == 1:
            answer.append(arr[0])
            return print("".join(map(str, answer)))
        for i in range(len(arr)):
            new_arr = arr[:i] + arr[i+1:]
            new_answer = answer.copy() + [arr[i]]
            permutation(new_answer, new_arr)
    
    N = int(input())
    arr = [i+1 for i in range(N)]
    permutation([], arr)
        
if __name__ == '__main__':
	main()