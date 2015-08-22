# p_example.py -- example bot to read history

import random
import monkeystud

class Bot:

    def __init__(self):
        pass

    def parse_history(self, history):
        g = Game()
        g.players = {}
        g.pot = 0
        g.player_count = 0
        for i in history.split():
            player_id, code, x = i.split(':')
            if not g.players.has_key(player_id):
                p = Player()
                p.seat = len(g.players)
                p.player_id = player_id
                p.chips = 0
                p.bet = 0
                p.hand = []
                p.history = []
                p.folded = True
                g.players[player_id] = p
            g.players[player_id].history.append((code, x))
            if 0:
                pass
            elif 'S' == code:
                p.chips = int(x)
                g.player_count += 1
                pass
            elif 'A' == code:
                g.pot += int(x)
                g.players[player_id].chips -= int(x)
                g.players[player_id].bet += int(x)
            elif 'D' == code:
                g.players[player_id].hand.append(monkeystud.INVALID_CARD)
            elif 'U' == code:
                g.players[player_id].hand.append(monkeystud.str_to_card(x))
            elif 'C' == code:
                pass
            elif 'F' == code:
                g.players[player_id].folded = True
                g.player_count -= 1
            elif 'B' == code:
                g.players[player_id].bet += int(x)
            elif 'R' == code:
                hand = monkeystud.str_to_hand(x)
                g.players[player_id].cards = hand
                g.players[player_id].best_hand = monkeystud.best_hand_value(hand)
            elif 'W' == code:
                g.players[player_id].chips += int(x)
            elif 'Z' == code:
                g.players[player_id].chips += int(x)

    def get_play(self):
        ##
        ## TODO: do stuff here
        ##
        return random.choice(('F', 'C', 'B'))


# the global singleton Bot class
#
g_bot = Bot()

# our play() implementation for the harness. it just 
# passes the request into the Bot class's implementation.
#
def play(player_id, hand, history):
    global g_bot
    return g_bot.play(player_id, hand, history)
