def count_palindromic_substrings(strings):
    N = len(strings)
    dp = [[False] * N for _ in range(N)]
    count = 0

    # Подстроки длины 1 всегда являются палиндромами
    for i in range(N):
        dp[i][i] = True
        count += 1

    # Проверяем подстроки длины 2
    for i in range(N - 1):
        if strings[i] == strings[i + 1]:
            dp[i][i + 1] = True
            count += 1

    # Проверяем подстроки длины больше 2
    for length in range(3, N + 1):
        for i in range(N - length + 1):
            j = i + length - 1
            if strings[i] == strings[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                count += 1

    return count

def main():
    strings = input()
    answer = count_palindromic_substrings(strings)
    print(answer)

if __name__ == '__main__':
    main()