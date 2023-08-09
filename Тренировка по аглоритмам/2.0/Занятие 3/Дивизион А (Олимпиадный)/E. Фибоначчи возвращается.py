from decimal import Decimal

def main():
    '''
    '''
    mods = [10**9 + 7, 10**9 + 11, 10**9 + 13]
    max_Fibonachi_count = 40000
    
    used_hash = []
    for _ in range(len(mods)):
        used_hash.append(set())

    for i in range(len(mods)):
        Fibonachi_1 = 1
        Fibonachi_2 = 1
        used_hash[i].add(1)
        for j in range(max_Fibonachi_count):
            Fibonachi_1, Fibonachi_2 = Fibonachi_2, (Fibonachi_1 + Fibonachi_2) % mods[i]
            used_hash[i].add(Fibonachi_2)

    N = int(input())

    answer = []

    for i in range(N):
        number = Decimal(input())
        is_Fibonachi = True
        for i in range(len(mods)):
            if number % mods[i] not in used_hash[i]:
                is_Fibonachi = False
                break
        if is_Fibonachi:
            answer.append('Yes')
        else:
            answer.append('No')
            
    for i in answer:
        print(i)
    
if __name__ == '__main__':
	main()