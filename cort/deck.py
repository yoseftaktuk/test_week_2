import random

def create_card(rank:str,suite:str):
    upper_case_rank = rank.upper()
    upper_case_suite = suite.upper()
    card = {'rank':upper_case_rank,'suite':upper_case_suite}
    return card


def build_standart_beck():
    rank = ['A','D','C','H']
    list_card = []
    for suit in rank:
        for j in range(2,15):
            if j <= 10:
                list_card.append(create_card(str(j),suit))
            else:
                if j == 11:
                    list_card.append(create_card('J',suit))
                elif j == 12:
                    list_card.append(create_card('Q',suit))
                elif j == 13:
                    list_card.append(create_card('K',suit))
                elif j == 14:
                    list_card.append(create_card('A',suit))
    return list_card

def shuffle_by_suit(deck:list[dict],swaps = 5000):
    while swaps:
        random_index_i = random.randint(0, 51)
        random_index_j = random.randint(0, 51)
        if random_index_i == random_index_j or random_index_j % 3 != 0 or random_index_j % 5 != 0 or random_index_j % 2 != 0 or random_index_j % 7 != 0:
            continue
        else:
            deck[random_index_i], deck[random_index_j] = deck[random_index_j], deck[random_index_i]
            swaps -= 1
    return deck