def main():
    '''
    '''
    N = int(input())
    letter_dict = {}
    word = input()
    for letter in word:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    
    letter_arr = sorted(letter_dict.items(), key=lambda x: x[0])
    
    is_odd = False
    odd_letter = ''
    polydrom_arr = []
    for letter, count in letter_arr:
        if not is_odd and count % 2 == 1:
            is_odd = True
            odd_letter = letter
        
        count_2 = count // 2    
        if count_2 > 0:
            for i in range(count_2):
                polydrom_arr.append(letter)
    
    polydrom_arr = polydrom_arr + [odd_letter] + polydrom_arr[::-1]
    print(''.join(polydrom_arr))
    
    

    
if __name__ == '__main__':
	main()