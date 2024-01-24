def generate_valid_bracket_sequences(N_max, number = 1, sequences = [], open_brackets = []):
    '''
    '''
    # FIXME: напишите ваш код здесь
    if number > N_max and len(open_brackets) == 0:
        print(''.join(sequences))
    else:
        if len(open_brackets) < N_max - number:
            sequences.append('(')
            open_brackets.append('(')
            generate_valid_bracket_sequences(N_max, number + 1, sequences, open_brackets)
            sequences.pop()
            open_brackets.pop()
            
            sequences.append('[')
            open_brackets.append('[')
            generate_valid_bracket_sequences(N_max, number + 1, sequences, open_brackets)
            sequences.pop()
            open_brackets.pop()
            
        if len(open_brackets) > 0:
            if open_brackets[-1] == '(':
                sequences.append(')')
                open_brackets.pop()
                generate_valid_bracket_sequences(N_max, number + 1, sequences, open_brackets)
                sequences.pop()
                open_brackets.append('(')
            else: # open_brackets[-1] == '[':
                sequences.append(']')
                open_brackets.pop()
                generate_valid_bracket_sequences(N_max, number + 1, sequences, open_brackets)
                sequences.pop()
                open_brackets.append('[')
    
    return sequences

def main():
    '''
    '''
    N = int(input())
    if N % 2 == 0:
        generate_valid_bracket_sequences(N)
    
if __name__ == '__main__':
    main()