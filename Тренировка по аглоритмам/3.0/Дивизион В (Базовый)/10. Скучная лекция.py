def main():
    '''
    '''
    word = input()
    symbol = {}
    for i in range(len(word)):
        combination = (i + 1) * (len(word) - i)
        if word[i] not in symbol:
            symbol[word[i]] = combination
        else:
            symbol[word[i]] += combination
            
    array = []
    for key, value in symbol.items():
        array.append((key, value))
    array.sort()
    for key, value in array:
        print(key + ': ' + str(value))
        
if __name__ == '__main__':
	main()