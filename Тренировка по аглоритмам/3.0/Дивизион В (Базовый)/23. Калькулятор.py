def main():
    n = int(input())
    if n == 1:
        print(0, '\n', 1, sep="")
        return
    elif n == 2:
        print(1)
        print(1, 2)
        return
    elif n == 3:
        print(1)
        print(1, 3)
        return

    a = [0, 0, 1, 1]
    b = [0, 0, 1, 1]    
    for i in range(4, n + 1):
        mn = 10**7
        if i % 3 == 0:
            mn = a[i // 3]
        if i % 2 == 0:
            mn = min(mn, a[i // 2])
        mn = min(a[i - 1], mn)
        a.append(mn + 1)
        if i % 3 == 0 and a[i // 3] == mn:
            b.append(i // 3)
        elif i % 2 == 0 and a[i // 2] == mn:
            b.append(i // 2)
        else:
            b.append(i - 1)
            
    lt = [n]
    t = b[n]
    c = a[n]
    while c != 0:
        lt.append(t)
        t = b[t]
        c = a[t]
    lt += [1]
    print(len(lt) - 1)
    print(*lt[::-1])
        
if __name__ == '__main__':
	main()
