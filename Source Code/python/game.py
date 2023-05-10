say = Print()
players, deck, count = setup()
center = Center()

while count < 49:
    temp = False
    for player in players:
        if player.hand:
            temp = False
            break
        else:
            temp = True
    if temp:
        deal_cards(deck, players)

    player = players[count % len(players)]

    for pile in center.pile:
        for card in pile.pile:
            card.wasLastPlayed = False
    
    playersTurn(player)

    count += 1

print('game finished')
compare_players(players)
for player in players:
    player.show_points()
