# E. Подпалиндромы
# требуется изучить алгоритм Манакера
# https://e-maxx.ru/algo/palindromes_count
# Код приведённый ниже написан с применением ChatGPT


def count_palindromic_substrings(strings):
    N = len(strings)
    # Добавляем специальные символы "#" между символами строки и в начало и конец строки
    modified_string = '#' + '#'.join(strings) + '#'
    modified_length = len(modified_string)
    
    # Массив для хранения длин палиндромных подстрок в модифицированной строке
    pal_lengths = [0] * modified_length
    
    # Позиция и длина самого правого палиндрома, который был найден
    center = right = 0
    
    # Количество палиндромных подстрок
    count = 0
    
    for i in range(1, modified_length - 1):
        # Определение начальной длины палиндрома на основе уже найденных палиндромов
        if i < right:
            mirror = 2 * center - i
            pal_lengths[i] = min(right - i, pal_lengths[mirror])
        
        # Расширение палиндрома влево и вправо
        while i + 1 + pal_lengths[i] < modified_length and i - 1 - pal_lengths[i] >= 0 and modified_string[i + 1 + pal_lengths[i]] == modified_string[i - 1 - pal_lengths[i]]:
            pal_lengths[i] += 1
        
        # Обновление самого правого палиндрома
        if i + pal_lengths[i] > right:
            center = i
            right = i + pal_lengths[i]
        
        # Подсчет палиндромных подстрок
        count += (pal_lengths[i] + 1) // 2
    
    return count

def main():
    strings = input()
    answer = count_palindromic_substrings(strings)
    print(answer)

if __name__ == '__main__':
    main()