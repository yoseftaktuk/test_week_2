import cort.deck
import cort.game_logic


if __name__ == "__main__":
    deck = cort.deck.build_standart_beck()
    shuffle_deck = cort.deck.shuffle_by_suit(deck)
    player = {'hand':[]}
    dealer = {'hand':[]}
    cort.game_logic.run_game(deck,player,dealer)