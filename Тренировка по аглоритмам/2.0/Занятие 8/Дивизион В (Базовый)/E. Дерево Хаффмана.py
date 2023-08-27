import sys

def main():
    '''
    '''
    def create_tree(huffman_codes, code, h_s_s):
        if len(h_s_s) == 0:
            huffman_codes.append(code)
            return
        
        symbol = h_s_s.pop()
        if symbol == "U":
            huffman_codes.append(code)
            return
        else: # D
            create_tree(huffman_codes, code + "0", h_s_s)
            create_tree(huffman_codes, code + "1", h_s_s)
            
    
    N = int(input())
    for _ in range(N):
        h_s_s = input() # huffman_short_symbol
        huffman_codes = []
        # преобразуем в обратный список, чтобы было удобно удалять и обрабатывать.
        h_s_s = [h_s_s[-i-1] for i in range(len(h_s_s))]
        
        create_tree(huffman_codes, "", h_s_s)
        
        print(len(huffman_codes))
        for code in huffman_codes:
            print(code)
     
if __name__ == '__main__':
	main()