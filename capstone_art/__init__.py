logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

class Card(object):
    deck = {
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10
    }

    def __init__(self, suit, rank):
        self.suit = suit.capitalize()
        self.rank = rank
        self.points = self.deck[rank]


card_format = """\
┌──────────┐
│ {}       │
│    {}   │
│       {} │
└──────────┘
""".format('{rank: <2}', '{suit: <2}', '{rank: >2}')


hidden_card_format = """\
┌──────────┐
│░░░░░░░░░░│ 
│░░░░░░░░░░│
│░░░░░░░░░░│
└──────────┘
"""


def join_lines(strings):
    multi_line = [string.splitlines() for string in strings]
    return '\n'.join(''.join(lines) for lines in zip(*multi_line))


def ascii_version_of_card(*cards):
    name_to_symbol = {
        'Spades':   '♠',
        'Diamonds': '♦',
        'Hearts':   '♥',
        'Clubs':    '♣',
    }

    def card_to_string(card):
        # 10 is the only card with a 2-char rank abbreviation
        rank = card.rank if card.rank == '10' else card.rank[0]

        return card_format.format(rank=rank, suit=name_to_symbol[card.suit])

    return join_lines(map(card_to_string, cards))


def ascii_version_of_hidden_card(*cards):
    name_to_symbol = {
        'Spades':   '♠',
        'Diamonds': '♦',
        'Hearts':   '♥',
        'Clubs':    '♣',
    }

    def hidden_card_to_string(card):
        rank = card.rank[0]
        return hidden_card_format.format(rank=rank, suit=name_to_symbol[card.suit])

    return join_lines(map(hidden_card_to_string, cards))


# test_case_one = Card('Diamonds', 'A')
# print(ascii_version_of_card(test_case_one))
# print(ascii_version_of_hidden_card(test_case_one))
