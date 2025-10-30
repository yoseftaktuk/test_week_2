import cort.game_logic

def ask_player_action():
    while True:
        player_input = input('What action would you like to take (h/s)?')
        if player_input == 's':
            return 'S'
        elif player_input == 'h':
            return 'H'
        else:
            continue

def print_status_players(player,dealer):
    print('player hand is',cort.game_logic.calculate_hand_value(player['hand']),'and the dealer hand is',cort.game_logic.calculate_hand_value(dealer['hand']))

