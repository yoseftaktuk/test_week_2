import cort.player_io
#הפונקצייה מקבלת את היד וגם בודקת למי היא שייכת ולפי זה מחשבת
def calculate_hand_value(hand:list[dict],player = bool,dealer = bool):
     intrele_valyo = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':1}
     total_valyo = 0
     for index in range(len(hand)):
         if hand[index]['rank'] == 'A' and player and not dealer:
             player_input = cort.player_io.selection_of_ace()
             total_valyo += player_input
             continue
         elif hand[index]['rank'] == 'A'  and dealer:
             if 10 + total_valyo > 21:
                 total_valyo += 1
                 continue
             else:
                 total_valyo += 10
                 continue
         total_valyo += intrele_valyo[hand[index]['rank']]
     return total_valyo

def deal_two_each(deck:list[dict],player:dict,dealer:dict):
    player_card_1 = deck.pop()
    player_card_2 = deck.pop()
    dealer_card_1 = deck.pop()
    dealer_card_2 = deck.pop()
    player['hand'].append(player_card_1)
    print('you get',player_card_1['rank'],end=' ')
    player['hand'].append(player_card_2)
    print('and', player_card_2['rank'])
    dealer['hand'].append(dealer_card_1)
    dealer['hand'].append(dealer_card_2)
    #מדפיס את סכום הקלפים שיש לכל אחד
    cort.player_io.print_status_player(player)
    cort.player_io.print_status_dealer(dealer)
    return None

def dealer_play(deck: list[dict], dealer: dict):
    size_hand = calculate_hand_value(dealer['hand'],False,True)
    while size_hand < 17:
        dealer_card_1 = deck.pop()
        dealer['hand'].append(dealer_card_1)
        size_hand = calculate_hand_value(dealer['hand'], False,True)
    if size_hand <= 21:
        return True
    return False

def run_game(deck: list[dict], player: dict, dealer: dict):
    deal_two_each(deck,player,dealer)
    player_hand = calculate_hand_value(player['hand'], True, False)
    dealer_hand = calculate_hand_value(dealer['hand'], False, True)
    while True:
        player_input = cort.player_io.ask_player_action()
        if player_input == 'H':
            player_card_1 = deck.pop()
            player['hand'].append(player_card_1)
            print('you get', player_card_1['rank'], end=' ')
            player_hand = calculate_hand_value(player['hand'], True, False)
            dealer_hand = calculate_hand_value(dealer['hand'], False, True)
            print('player hand is',player_hand)
            if player_hand == 21:
                print('player won')
                break
            if player_hand > dealer_hand:
                print('you lost')
                break
        elif player_input == 'S':
            if dealer_play(deck,dealer):
                if player_hand > dealer_hand:
                    cort.player_io.print_status_players(player, dealer)
                    print('you won')
                    break
                elif calculate_hand_value(player['hand'],True,False) == calculate_hand_value(dealer['hand'],False,True):
                    print('Its a draw')
                    break
                else:
                    cort.player_io.print_status_players(player, dealer)
                    print('you lost')
                    break
            else:
                cort.player_io.print_status_players(player, dealer)
                print('you won')
                break
    return None