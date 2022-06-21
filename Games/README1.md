Games
=============================================

This folder contains recreation of popular games. 

-------------------------------------------
hangman.py
-------------------------------------------
Run:
python hangman.py

Short: Play hangman. The Player has 6 lives to guess what the hidden word is.

Long: The player is presented with an unknown word and may guess a letter or what the whole word is on each turn.
If the player guesses incorrectly, a life is deducted from the player. If the player guesses the word before their lives run out they win.


-------------------------------------------
murderMystery.py
-------------------------------------------
Run:
python murderMystery.py

Short: Play Murder Mystery where you and 9 other players (all computers) are assigned the roles of murderer (evil - kill all of the good team),
detective (good- investigate players and reveals roles), doctor (good - prevents murders from occurring toward a selected player), 
and citizen (good - does nothing). Murderers must kill all of the good team, while the good team tries to vote out the murderers.

Long: This game was inspired by the popular family game mafia where the mafia would "execute" a player every night and the players would 
wake up and discuss who should be voted out. This game was modified where innocent players could also have additional roles to aid them 
in discovering who the evildoers are. As stated in the short description, detectives are able to investigate a player every night.
If the player is a detective, they will manually select who they want to investigate. If they find someone evil, they will be prompted 
if they want to release this information to the public. This, however, may be a bad idea since every round there are 2 murderers, and if a player
reveals their identity as innocent they will be targeted by the murderers. 

A doctor is presented with a similar interface where every night they can select who to prevent from getting murdered.

A murderer has the same interface but instead chooses who to kill every night. In the morning the mayor will make some announcements on who, 
if any, players died and then ask if anyone wants to reveal any information. If a player is outed as being evil then the town will vote for 
that player. The town will vote a player out every other day. So on the first day, usually someone random, which could be the player,
will be voted out.

-------------------------------------------
battleship.py
-------------------------------------------
Run:
python battleship.py

Short: Play battleship against a naive computer.

Long: Game where you can randomly place 5 ships of size 5,4,3,3,2 on a 10x10 board and attempt to hit
the opponent's ships before the computer sinks all of your ships. The computer is running on a purely random guessing algorithm.
battleshipV2.py is in the making to have the computer develop a more intelligent guessing algorithm. Along with graphics.


