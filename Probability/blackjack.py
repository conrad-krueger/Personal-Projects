import random

def main():
  cards = [x for x in range(1,11)] *4 + [10] * 12
  print(len(cards))


  random.shuffle(cards)


  def hit():
    a = cards[0]
    cards.pop(0)
    return a


  #keep track of wins and losses
  deal_W = 0
  deal_W_tie = 0
  deal_W_2bust = 0
  deal_W_bust = 0
  player_W = 0
  player_W_bust = 0

  #how many iterations will we do
  iter = int(input("Enter the amount of iterations: "))
  prob = int(input("Enter percentage of certainty (int): "))
  minScore = int(input("Enter minimum score you must have (this may contradict and override percentage of certainty): "))
  verbose = True

  #loop for inputted amount of iterations
  for _ in range(iter):
    if (len(cards)== 0):
      cards = [x for x in range(1,11)] *4 + [10] * 12
      random.shuffle(cards)



    #4 mandatory cards drawn
    cards_inplay = []
    players_hand = []
    dealers_hand = []

    deal_hand_total = 0
    player_hand_total = 0

    for draw in range(4):
      card = hit()
      cards_inplay.append(card)

      if (len(cards)== 0):
          cards = [x for x in range(1,11)] *4 + [10] * 12
          for y in cards_inplay:
              cards.remove(y)
          random.shuffle(cards)



      if draw < 2: 
          player_hand_total += card
          players_hand.append(card)
      else: 
          deal_hand_total += card
          dealers_hand.append(card)



    #dealer 17 rule
    while (deal_hand_total < 17):
      card = hit()
      cards_inplay.append(card)
      dealers_hand.append(card)
      deal_hand_total += card
      if (len(cards)== 0):
        cards = [x for x in range(1,11)] *4 + [10] * 12
        for y in cards_inplay:
          cards.remove(y)
        random.shuffle(cards)
    #player probability of certainty. ie if there is a 60% chance that the next hit wont break and the player inputted 60 or lower. player will hit


    y = 0
    n = 0
    while True:
      for x in cards:
        #print(cards)
        if (x + player_hand_total <= 21):
          y += 1
        else:
          n += 1

      if ((y/(y+n)) * 100 >= prob or player_hand_total < minScore):
        card = hit()
        cards_inplay.append(card)
        players_hand.append(card)
        player_hand_total += card
        if (len(cards)== 0):
          cards = [x for x in range(1,11)] *4 + [10] * 12
          for y in cards_inplay:
            cards.remove(y)
          random.shuffle(cards)
      else: 
        break

    # assign a dub
    if (player_hand_total > 21 and deal_hand_total > 21):
      if verbose: print("L - Both Bust")
      deal_W_2bust += 1
    elif (player_hand_total > 21 and not deal_hand_total > 21):
      if verbose: print("L - Player Bust")
      deal_W_bust += 1
    elif (player_hand_total <= 21 and deal_hand_total > 21):
      if verbose: print("W - Dealer Bust")
      player_W_bust += 1 
    elif (player_hand_total == deal_hand_total):
      if verbose: print("L - Same Amount")
      deal_W_tie += 1
    elif (player_hand_total < deal_hand_total):
      if verbose: print("L - Dealer had better hand")
      deal_W += 1 
    elif (player_hand_total > deal_hand_total):
      if verbose: print("W - You had better hand")
      player_W += 1 
    if verbose:
        print("Player's hand:", players_hand)
        print("Dealer's hand:", dealers_hand)



  #output results
  print(f"After {iter} iterations and a {prob}% chance of certainty...")
  print()
  print()
  print(f"The dealer won {deal_W+deal_W_tie+deal_W_2bust+deal_W_bust} times ({(deal_W+deal_W_tie+deal_W_2bust+deal_W_bust)/iter*100}%).")
  print()
  print("Beating player and both under 21:",deal_W)
  print("Tying with player:",deal_W_tie)
  print("Both dealer and player busting:",deal_W_2bust)
  print("Beating player because they busted:",deal_W_bust)
  print()
  print()
  print(f"The player won {player_W+player_W_bust} times.")
  print("Beat dealer because they busted and player didn't:",player_W_bust)
  print()

if __name__ == "__main__":
  main()


