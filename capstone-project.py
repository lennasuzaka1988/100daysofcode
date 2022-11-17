import random
from capstone_art import ascii_version_of_hidden_card
from capstone_art import ascii_version_of_card
from capstone_art import Card
from capstone_art import logo

print(logo)


deck = Card.deck
current_cash = 1000
total_bet = 0
game = True

while game:
    random.seed()

    def bet_query():
        list_of_chips = ["1", "5", "10", "25", "50", "100", "200", "500"]
        global total_bet

        def call_bet():
            global total_bet
            bet = input(f"You have {'${:,.2f}'.format(current_cash - total_bet)}. "
                                     f"Place your bet! Which betting chip would you like to use? "
                                     f"Type the numbers: '1', '5', '10', '25', '50', '100', '200', or '500' ")
            while bet not in list_of_chips:
                bet = input(f"Please enter the proper betting chip amount: '1', '5', '10', '25', '50', '100', '200', or '500' ")
            total_bet += int(bet)
            if total_bet > current_cash:
                total_bet = 0
                print("Total bet is more than what you have in your account. Your bet has been reset. ")
                call_bet()
            else:
                more_bets()

        def more_bets():
            more_bet = input(f"You\'ve bet {'${:,.2f}'.format(int(total_bet))}. "
                             f"You now have {'${:,.2f}'.format((current_cash - total_bet))}. "
                             f"Would you like to bet more? Type 'yes' or 'no': ").lower()
            if more_bet == 'no':
                return
            elif more_bet == 'yes':
                call_bet()
            while more_bet != 'no' and more_bet != 'yes':
                more_bet = input("Please enter 'yes' or 'no' to choose whether you'd like to bet more: ")
        call_bet()
        more_bets()

    full_deck = {}

    symbols = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
    symbols_extended = list(symbols * 13)
    for k, v in deck.items():
        full_deck.update({k: [v] * 4})


    def starting_hand():
        drawn_rank = []
        drawn_symbols = []
        drawn_card_values = []

        while len(drawn_card_values) < 2:
            chosen_card = random.choice(list(full_deck))
            chosen_symbol = random.choice(symbols_extended)
            drawn_symbols.append(chosen_symbol)
            drawn_rank.append(chosen_card)
            if chosen_card == 'A':
                chosen_card_value = full_deck[chosen_card].pop() + 10
            else:
                chosen_card_value = full_deck[chosen_card].pop()
            symbols_extended.remove(chosen_symbol)
            drawn_card_values.append(chosen_card_value)
        return drawn_rank, drawn_symbols, drawn_card_values


    def card_art(symbol, rank):
        chosen_card_art = Card(symbol, rank)
        card_face = ascii_version_of_card(chosen_card_art)
        return card_face


    def hidden_card_art(symbol, rank):
        chosen_card_art = Card(symbol, rank)
        hidden_card = ascii_version_of_hidden_card(chosen_card_art)
        return hidden_card


    player_first_hand_rank, player_first_hand_symbol, player_first_hand_value = starting_hand()
    player_first_draw_art = card_art(player_first_hand_symbol[0], player_first_hand_rank[0])
    player_second_draw_art = card_art(player_first_hand_symbol[1], player_first_hand_rank[1])

    dealer_first_hand_rank, dealer_first_hand_symbol, dealer_first_hand_value = starting_hand()
    dealer_first_draw_art = card_art(dealer_first_hand_symbol[0], dealer_first_hand_rank[0])
    dealer_second_hidden_art = hidden_card_art(dealer_first_hand_symbol[1], dealer_first_hand_rank[1])


    def keep_going_question():
        print(full_deck)
        global game
        global total_bet
        total_bet = 0
        continue_the_game_question = input(f"Want to keep going? You now have {'${:,.2f}'.format(current_cash)}. "
                                           f"Type 'yes' or 'no'. ")
        if continue_the_game_question == 'yes':
            game = True
        else:
            game = False

    def game_start():
        player_hand_drawn = player_first_hand_rank[0] + ' and ' + player_first_hand_rank[1]
        player_hand = sum(player_first_hand_value)

        print(f'You draw {player_hand_drawn}, totaling {player_hand}.')
        print(player_first_draw_art + '\n' + player_second_draw_art)

        dealer_hand_drawn = dealer_first_hand_rank[0]
        dealer_hand = sum(dealer_first_hand_value)

        print(f'Dealer draws {dealer_hand_drawn}.')
        print(dealer_first_draw_art + '\n' + dealer_second_hidden_art)
        return player_hand, dealer_hand


    def stand_result(player_h, dealer_h):
        global game
        global current_cash
        if dealer_h < player_h:
            print(dealer_first_draw_art)
            print(card_art(dealer_first_hand_symbol[1], dealer_first_hand_rank[1]))
            print(f'Dealer\'s hand is {dealer_first_hand_rank}, totaling {dealer_h}. '
                  f'Because you have a higher hand, you win!')
            current_cash += total_bet
            keep_going_question()
        elif dealer_h > player_h:
            print(dealer_first_draw_art)
            print(card_art(dealer_first_hand_symbol[1], dealer_first_hand_rank[1]))
            print(f'Dealer\'s hand is {dealer_first_hand_rank[0]} and {dealer_first_hand_rank[1]}, totaling {dealer_h}. '
                  f'Because your hand is valued less, you lose!')
            current_cash -= total_bet
            keep_going_question()
        else:
            print(f'Wow, you both tied!')


    bet_query()
    current_hand, dealer_hand = game_start()
    while game:
        if current_hand == 21:
            print(f"{current_hand}. You win!")
            current_cash += total_bet
            keep_going_question()
        elif current_hand > 21:
            print(f"{current_hand}. Bust! You lose!")
            current_cash -= total_bet
            keep_going_question()
        else:
            call = input('Type "hit" or "stand": ').lower()
            if call == 'hit':
                drawn_card = random.choice(list(full_deck))
                drawn_symbol = random.choice(symbols_extended)
                symbols_extended.remove(drawn_symbol)
                print(card_art(drawn_symbol, drawn_card))
                print(f"{drawn_card} drawn. Your current total is {current_hand}.")
                drawn_card_values = full_deck[drawn_card].pop()
                if drawn_card == 'A':
                    if 20 > current_hand > 10:
                        current_hand += 1
                    else:
                        current_hand += 11
                elif drawn_card in list(full_deck):
                    current_hand += drawn_card_values
            elif call == 'stand':
                stand_result(current_hand, dealer_hand)


# Bug, uses the same cards over and over after another round