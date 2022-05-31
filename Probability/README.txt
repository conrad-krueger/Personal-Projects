Probability
=============================================

This folder contains small programs that are used to simulate large iterations of events to approximate or provide evidence to vailidate a probability claim.

-------------------------------------------
DreamProb.java
-------------------------------------------
Compile and Run:
javac DreamProb.java
java DropRateTest

Short: Simulates 262 ender pearl and 305 blaze rod drops chances for [insert amount] iterations and compares them to popular Youtuber Dream's odds.

Long: A popular Minecraft Youtuber named Dream was accused of cheating during some of his Minecraft Speedruns (playing through a game of minecraft as fast as possible) 
by modifying the drop rate of two essential items needed to complete the game: Ender Pearls and Blaze Rods. This was suspected as Dream's drop rates were significantly
higher than the expected drop rate. The minecraft speedrunning moderators published a youtube video (https://www.youtube.com/watch?v=-MYw9LcLCb4&t=615s) and paper that showed how 
unlikely Dream's situation was. Their paper was primarily centered around using a Binomial Distribution to show the likelyhood of getting 42/262 ender pearls (when the population proportion is ~5%)
and getting 211/305 blaze rods (when the population proportion is 50%). This script simply runs as many iterations as the user desires and depicts how many instances
of those iterations got the same blaze drop rate, the same ender pearl drop rate, and both.
Note: Minecraft uses Java's Random class as its random generator (for nearly everything). So I used it as well as a method of getting a different seed for the Random object. This simulation is a naive recreation of the issue
at hand and does not EXACTLY represent Minecraft's method of determining blaze rod or ender pearl drops. However, I did my best to replicate the Moderator Team's published paper's description of Minecraft's usage of Java's Linear Congruential Generators.



-------------------------------------------
shutTheBox.py
-------------------------------------------
Run:
python shutTheBox.py

Short: Simulates [insert amount] games of Shut the Box and records how many instances the user sucessfully shuts the box. Also, depicts additional statistics.

Long: Shut the box is a game where there is a set of 9 integers [1,2,3,4,5,6,7,8,9] and 2 dice. Each round the two die are rolled and the player must use a combination of the 
set of integers that results in the summation of the two die. After this all of the integers used for that round are removed from the set. If all integers are successfully removed from the set
then you win and have "shut the box." If you end up with a dice roll that cannot be added up with the remaining integers in the set then you lose that game. 
This program was an attempt to find an optimal algorithm to win.

To start off we know the generating function for the summation of two die is:
A(z) = z^2 + 2z^3 + 3z^4 + 4z^5 + 5z^6 + 6z^7 + 5z^8 + 4z^9 + 3z^10 + 2z^11 + z^12 where the exponent represents the summation of two dice and the coefficent is the number of ways 2 dice
can sum up to the corresponding exponent. This can be used to determine the probability of rolling 2 dice and the sum equaling the exponent (coefficent/36). My method is a brute force approach where I generate all of the possible 
combinations of the numbers 1 through 9 that sum to all of the possible dice rolls (2 through 12). Then, each number (1-9) is used as a key in a python dictionary. After a number is used in a potential summation (say of the number A), that corresponding number's
dictionary index was incremented by the weight or probability of rolling an A. The algorithm then will role two die and loop over all the possible combinations that the player can use. The algorithm will pick the combination of numbers that have the least weight (based on the dictionary).
Three other common methods are used (always pick least amount of numbers and closest to the middle, pick the most amount of numbers, and randomly select a combination that works). As of now, the weight method described above has the best win rate (~6%). 
More accurate statistical conclusions are in the program (developing a confidence interval, showing statistics on games lost).
The second best was the "use least amount of numbers and closest to center of box" method at ~5.88%. I also wrote a quick comparingProportion.py file that performed a hypothesis test that indicates if there is statistically significant evidence to suggest that these two methods 
do not have the same population proportion (they did not under 5% alpha level). 



-------------------------------------------
blackjack.py
-------------------------------------------
Run:
python blackjack.py

Short: Simulates [insert amount] of rounds of blackjack. User inserts 2 components that dictate the users' strategy. 1] Percentage of certainty that the user will not bust on any given hand 2] The absolute minimum amount of points the user is willing to get on any given hand (will override component 1).

Long: Simulates the game blackjack where a player continously recieves cards from the dealer (hit) until the sum of the players cards is as close to 21 as possible (without going over). This simulates a player vs dealer scenario.
Dealer will win in the following situations:
- Both players bust (go over 21)
- User busts and Dealer does not
- Dealer has same score or higher than the player (without busting)
Note: Dealer has no strategy except the dealer MUST hit until their score is >= 17 (will stop hitting after it meets this condition).

User will win in the following situations:
- User has higher score than dealer (without busting)
- Dealer busts and player does not

Yes this is unlikely to help out in actual blackjack (since the percentage of certainty requires doing a linear comparison of each of the remaining cards). But still an interesting game.


-------------------------------------------
monopoly.py
-------------------------------------------
Run:
python monopoly.py

Short: Simulates [insert amount] of dice rolls around a board of monopoly (including the effects of 3x double rolls, chance cards, community chest, etc.) and tracks how often each square is landed.
These results are printed out sorted and on a bar graph where 1 represents square 1 to square 40 (41 is in jail).

Long: I was playing a game and wanted to see if there is any evidence that the probability of landing on any square is not uniform. This program simulates as many rolls as one wants
and keeps track of the frequency of landing on any particular square. Results vary slightly but it seems that Jail is the most popular square to land on (pretty obvious) but the most landed on property is Illinois Avenue. 


