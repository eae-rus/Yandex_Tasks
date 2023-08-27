import sys

def main():
    '''
    '''
    def add_descendant(tree, parent, descendant):
        if parent == tree[0]:
            descendant_tree = [descendant, []]
            tree[1].append(descendant_tree)
            return True
        else:
            for child in tree[1]:
                if add_descendant(child, parent, descendant):
                    return True
            return False
    
    def find_parant(tree, parent):
        if parent == tree[0]:
            return tree
        else:
            for child in tree[1]:
                new_tree = find_parant(child, parent)
                if new_tree is not None:
                    return new_tree
            return None
           
    def find_descendant(tree, descendant):
        if descendant == tree[0]:
            return True
        else:
            for child in tree[1]:
                if find_descendant(child, descendant):
                    return True
            return False
    
    N = int(input())
    descendant, parent = input().split()
    descendant_tree = [descendant, []]
    tree = [parent, [descendant_tree]]
    for i in range(N-2):
        descendant, parent = input().split()
        if add_descendant(tree, parent, descendant):
            continue
        else:
            print("ERROR")
    
    answer = []
    query = sys.stdin.readline()[0:-1].split()
    while not (query[0] == ""):
        descendant, parent = query[0], query[1]
        
        new_tree = find_parant(tree, parent)
        if find_descendant(new_tree, descendant):
            answer.append(2)
            query = sys.stdin.readline()[0:-1].split()
            continue
        
        new_tree = find_parant(tree, descendant)
        if find_descendant(new_tree, parent):
            answer.append(1)
            query = sys.stdin.readline()[0:-1].split()
            continue
        
        answer.append(0)
        query = sys.stdin.readline()[0:-1].split()
        
    print(' '.join(map(str, answer)))
     
if __name__ == '__main__':
	main()