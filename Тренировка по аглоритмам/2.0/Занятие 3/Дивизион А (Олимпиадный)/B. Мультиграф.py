def main():
    '''
    '''
    n, m = list(map(int, input().split()))
    edge_graph = set()
    for _ in range(m):
        a, b = list(map(int, input().split()))
        if a == b:
            continue
        elif a < b:
            edge_graph.add((a, b))
        else: # a > b
            edge_graph.add((b, a))
    
    print(n, len(edge_graph))     
    for a, b in edge_graph:
        print(a, b)
    
if __name__ == '__main__':
	main()