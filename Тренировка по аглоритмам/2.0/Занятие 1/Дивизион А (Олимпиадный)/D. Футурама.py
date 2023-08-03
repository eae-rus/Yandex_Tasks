def main():
    '''
    '''
    def bodyswap(a, b):
        print(a, b)
        body[a], body[b] = body[b], body[a]
        return body[b]
    
    n, m = map(int, input().split())
    body = [0] * (n+1)   
    for i in range(1, n+1):
        body[i] = i
    for _ in range(m):
        a, b = map(int, input().split())
        body[a], body[b] = body[b], body[a]
        
    for i in range(1, n-1):
        if body[i] != i:
            now = i
            while body[now] != i:
                now = bodyswap(now, n-1)
            now = bodyswap(now, n)
            now = bodyswap(now, n)
            bodyswap(body[n-1], n-1)
    
    if body[n-1] == n:
        bodyswap(n-1, n)

if __name__ == '__main__':
	main()