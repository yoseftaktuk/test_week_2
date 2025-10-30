import cort.player_io

def calculate_hand_value(hand:list[dict]):
     intrele_valyo = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':1}
     total_valyo = 0
     for index in range(len(hand)):
         total_valyo += intrele_valyo[hand[index]['rank']]
     return total_valyo

def deal_two_each(deck:list[dict],player:dict,dealer:dict):
    player_card_1 = deck.pop()
    player_card_2 = deck.pop()
    dealer_card_1 = deck.pop()
    dealer_card_2 = deck.pop()
    player['hand'].append(player_card_1)
    player['hand'].append(player_card_2)
    dealer['hand'].append(dealer_card_1)
    dealer['hand'].append(dealer_card_2)
    #מדפיס את סכום הקלפים שיש לכל אחד
    cort.player_io.print_status_players(player,dealer)
    return None

def dealer_play(deck: list[dict], dealer: dict):
    size_hand = calculate_hand_value(dealer['hand'])
    while size_hand <= 17:
        dealer_card_1 = deck.pop()
        dealer['hand'].append(dealer_card_1)
        size_hand = calculate_hand_value(dealer['hand'])
    if size_hand <= 21:
        return True
    return False

def run_game(deck: list[dict], player: dict, dealer: dict):
    deal_two_each(deck,player,dealer)
    while True:
        player_input = cort.player_io.ask_player_action()
        if player_input == 'H':
            player_card_1 = deck.pop()
            player['hand'].append(player_card_1)
            print('player hand is',calculate_hand_value(player['hand']))
            if calculate_hand_value(player['hand']) > 21:
                print('you lost')
                break
        elif player_input == 'S':
            if dealer_play(deck,dealer):
                if calculate_hand_value(player['hand']) > calculate_hand_value(dealer['hand']):
                    cort.player_io.print_status_players(player, dealer)
                    print('you won')
                    break
                elif calculate_hand_value(player['hand']) == calculate_hand_value(dealer['hand']):
                    print('Its a draw')
                else:
                    cort.player_io.print_status_players(player, dealer)
                    print('you lost')
                    break
            else:
                cort.player_io.print_status_players(player, dealer)
                print('you won')
                break
    return None