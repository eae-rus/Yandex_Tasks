import sys

sys.setrecursionlimit(25000)

def main():
    '''
    '''
    def find_max_chain(node, neighbors, best_length, visited):
        visited[node], best_length[node] = True, 1
        best_answer, max_1, max_2 = 1, -1, -1
        for neigh in neighbors[node]:
            if not visited[neigh]:
                best_answer = max(find_max_chain(neigh, neighbors, best_length, visited), best_answer)
                if best_length[neigh] > max_1:
                    max_2 = max_1
                    max_1 = best_length[neigh]
                elif best_length[neigh] > max_2:
                    max_2 = best_length[neigh]
        
        best_answer = max(best_answer, max_1 + 1) # вырожденная цепочка
        best_answer = max(best_answer, max_1 + max_2 + 1) # когда есть 2 соседа
        best_length[node] = max(best_length[node], max_1 + 1)
        return best_answer
    
    N = int(input())
    neighbors = [[] for _ in range(N+1)]
    
    while True:
        query = sys.stdin.readline()[0:-1].split(" ")
        try:
            bead_1, bead_2 = int(query[0]), int(query[1])
        except:
            break

        neighbors[bead_1].append(bead_2)
        neighbors[bead_2].append(bead_1)
    
    best_length = [0] * (N+1)
    visited = [False] * (N+1)
        
    print(find_max_chain(1, neighbors, best_length, visited))
     
if __name__ == '__main__':
	main()