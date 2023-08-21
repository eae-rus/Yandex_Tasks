def main():
    '''
    '''
    X_name = input()
    X_letter_dict = {}
    X_letter_set = set()
    for letter in X_name:
        X_letter_set.add(letter)
        if letter not in X_letter_dict:
            X_letter_dict[letter] = 1
        else:
            X_letter_dict[letter] += 1
    
    Y_name = input()
    Y_letter_dict = {}
    Y_letter_set = set()
    for letter in Y_name:
        Y_letter_set.add(letter)
        if letter not in Y_letter_dict:
            Y_letter_dict[letter] = 1
        else:
            Y_letter_dict[letter] += 1
    
    XY_letter_set = X_letter_set.intersection(Y_letter_set)
    XY_letter_arr = sorted(XY_letter_set)
    i, k = 0, 0
    answer = []
    while i < len(X_name) and k < len(Y_name) and len(XY_letter_arr) > 0:
        letter = XY_letter_arr.pop()
        count_letter = min(X_letter_dict[letter], Y_letter_dict[letter])
        for j in range(count_letter):
            answer.append(letter)
        
        X_count = 0
        while X_count < count_letter:
            X_letter_dict[X_name[i]] -= 1
            if letter == X_name[i]:
                X_count += 1
            i += 1
        
        Y_count = 0
        while Y_count < count_letter:
            Y_letter_dict[Y_name[k]] -= 1
            if letter == Y_name[k]:
                Y_count += 1
            k += 1
            
    print(''.join(answer))


    
if __name__ == '__main__':
	main()