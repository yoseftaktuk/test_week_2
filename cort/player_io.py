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

def selection_of_ace():
    while True:
        player_input = input('Do you want an Ace worth 1 or an Ace worth 10 (10/1)?')
        if player_input == '1':
            return 1
        elif player_input == '10':
            return 10
        else:
            continue

def print_status_players(player,dealer):
    print('player hand is',cort.game_logic.calculate_hand_value(player['hand'],True,False),'and the dealer hand is',cort.game_logic.calculate_hand_value(dealer['hand'],False,True))

def print_status_player(player):
    print('player hand is', cort.game_logic.calculate_hand_value(player['hand'], True, False))

def print_status_dealer(dealer):
    print('and the dealer hand is',cort.game_logic.calculate_hand_value(dealer['hand'],False,True))