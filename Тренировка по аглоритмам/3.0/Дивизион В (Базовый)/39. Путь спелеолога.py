def main():
    def calculate_step(node, variant):
        variants = {
            1: [node[0] - 1, node[1]    , node[2]    ],
            2: [node[0] + 1, node[1]    , node[2]    ],
            3: [node[0]    , node[1] - 1, node[2]    ],
            4: [node[0]    , node[1] + 1, node[2]    ],
            5: [node[0]    , node[1]    , node[2] - 1],
            6: [node[0]    , node[1]    , node[2] + 1],
        }
        return variants.get(variant, [node[0], node[1]])
    
    def is_valid_node(Z, X, Y, N, visited_nodes, contets_nodes):
        if X >= 0 and X < N and Y >= 0 and Y < N and Z >= 0 and Z < N:
            if not visited_nodes[Z][X][Y] and contets_nodes[Z][X][Y] == 0:
                visited_nodes[Z][X][Y] = True
                return True
        return False    

    N  = int(input())
    visited_nodes = [[[False for _ in range(N)] for _ in range(N)] for _ in range(N)]
    contets_nodes = [[[-1 for _ in range(N)] for _ in range(N)] for _ in range(N)]
    # -1 - неизвестно,  0 - пустой (можно идти), 1 - камень (не пройти)... на будущие модификации
    
    start_coordinaties = [-1, -1, -1]
    for z in range(N):
        _  = input()
        for x in range(N):
            line  = input()
            for y in range(N):
                if line[y] == ".":
                    contets_nodes[z][x][y] = 0
                elif line[y] == "#":
                    contets_nodes[z][x][y] = 1
                elif line[y] == "S":
                    start_coordinaties = [z, x, y]
    
    is_finished = False
    
    next_node_arr = [start_coordinaties]
    distance = 0
    if start_coordinaties[0] == 0:
        is_finished = True
    
    while not is_finished:
        now_node_arr = next_node_arr.copy()
        next_node_arr = []
        
        for node in now_node_arr:
            for variant in range(1, 7):
                Z, X, Y = calculate_step(node, variant)
                if is_valid_node(Z, X, Y, N, visited_nodes, contets_nodes):
                    next_node_arr.append([Z, X, Y])
                    if Z == 0:
                        is_finished = True
                        break
            if is_finished:
                break
        
        distance += 1
        if len(next_node_arr) == 0 and not is_finished:
            is_finished = True
            distance = -1
    
    print(distance)
            
if __name__ == '__main__':
	main()