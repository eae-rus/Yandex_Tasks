# E. Подпалиндромы
# требуется изучить алгоритм Манакера
# https://e-maxx.ru/algo/palindromes_count


def count_palindromic_substrings(s):
    n = len(s)
    d1 = [0] * n
    d2 = [0] * n
    count = 0

    # Обработка нечетной длины палиндромов
    l, r = 0, -1
    for i in range(n):
        k = i > r and 1 or min(d1[l + r - i], r - i + 1)
        while i + k < n and i - k >= 0 and s[i + k] == s[i - k]:
            k += 1
        d1[i] = k
        if i + k - 1 > r:
            l, r = i - k + 1, i + k - 1
        count += (d1[i] + 1) // 2

    # Обработка четной длины палиндромов
    l, r = 0, -1
    for i in range(n):
        k = i > r and 0 or min(d2[l + r - i + 1], r - i + 1)
        while i + k < n and (i - k - 1 >= 0 if i > 0 else True) and s[i + k] == s[i - k - 1]:
            k += 1
        d2[i] = k
        if i + k - 1 > r:
            l, r = i - k, i + k - 1
        count += (d2[i] + 1) // 2

    return count

def main():
    s = input()
    answer = count_palindromic_substrings(s)
    print(answer)

if __name__ == '__main__':
    main()