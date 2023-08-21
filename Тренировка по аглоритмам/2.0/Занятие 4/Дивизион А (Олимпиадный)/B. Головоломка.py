def main():
    '''
    '''
    N, M = map(int, input().split())
    letter_dict = {}
    for _ in range(N):
        word = input()
        for letter in word:
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1
                
    for _ in range(M):
        word = input()
        for letter in word:
            letter_dict[letter] -= 1 # проверку на наличие символа не вводим.
            
    answer = []
    for letter, count in letter_dict.items():
        if count > 0:
            for i in range(count):
                answer.append(letter)
    
    print(''.join(answer))

    
if __name__ == '__main__':
	main()