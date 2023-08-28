with open("input.txt", "r", encoding="utf-8") as f:
    symbol_dict = {}
    max_symbol = 0
    for line in f.readlines():
        for symbol in line:
            if symbol == " " or symbol == "\n":
                continue
            if symbol not in symbol_dict:
                symbol_dict[symbol] = 0
            symbol_dict[symbol] += 1
            if max_symbol < symbol_dict[symbol]:
                max_symbol = symbol_dict[symbol]
    
    keys = list(symbol_dict.keys())
    keys.sort()
    for i in range(max_symbol, 0, -1):
        line = []
        for key in keys:
            if symbol_dict[key] < i:
                line.append(" ")
            else:
                line.append("#")
        print(''.join(line))
    
    print(''.join(keys))
    