from queue import Queue

def main():
    deck_1, deck_2 = Queue(), Queue()
    deck = list(map(int, input().split()))
    for card in deck:
        deck_1.put(card)
        
    deck = list(map(int, input().split()))
    for card in deck:
        deck_2.put(card)
    
    step = 0
    while not deck_1.empty() and not deck_2.empty() and step < 10**6:
        card_1 = deck_1.get()
        card_2 = deck_2.get()
        # карта 0 побеждает карту 9
        if card_1 == 0 and card_2 == 9:
            deck_1.put(card_1)
            deck_1.put(card_2)
        elif card_2 == 0 and card_1 == 9:
            deck_2.put(card_1)
            deck_2.put(card_2)
        # остальные карты
        elif card_1 > card_2:
            deck_1.put(card_1)
            deck_1.put(card_2)
        else:
            deck_2.put(card_1)
            deck_2.put(card_2)
        step += 1
    
    if deck_1.empty():
        print("second " + str(step))
    elif deck_2.empty():
        print("first " + str(step))
    else:
        print("botva")
    
    

if __name__ == '__main__':
	main()