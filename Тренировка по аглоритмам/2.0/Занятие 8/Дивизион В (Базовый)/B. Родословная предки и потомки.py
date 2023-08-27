import sys

def main():
    '''
    '''
    N = int(input())
    child_to_parant_dict = {}
    for i in range(N-1):
        descendant, parent = input().split()
        child_to_parant_dict[descendant] = parent     

    answer = []
    query = sys.stdin.readline()[0:-1].split(" ")
    while not (query == ""):
        try:
            descendant, parent = query[0], query[1]
        except:
            break
        is_find = False
        
        parent_i = descendant
        while parent_i in child_to_parant_dict and not is_find:
            parent_i = child_to_parant_dict[parent_i]
            if parent_i == parent:
                answer.append(2)
                is_find = True
                query = sys.stdin.readline()[0:-1].split(" ")
                break
        
        parent_i = parent
        while parent_i in child_to_parant_dict and not is_find:
            parent_i = child_to_parant_dict[parent_i]
            if parent_i == descendant:
                answer.append(1)
                is_find = True
                query = sys.stdin.readline()[0:-1].split(" ")
                break
            
        if not is_find:
            answer.append(0)
            query = sys.stdin.readline()[0:-1].split(" ")

        
    print(' '.join(map(str, answer)))
     
if __name__ == '__main__':
	main()