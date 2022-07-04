Probability
=============================================

This folder contains scripts that simulate large iterations of events to approximate the probability of those events occurring.


-------------------------------------------
monopoly.py
-------------------------------------------
Run:
python monopoly.py

Short: Simulates user-defined amount of dice rolls around a board of monopoly (including the effects of 3x 
double rolls, chance cards, community chest, etc.) and tracks how often each square is landed.
These results are printed out sorted and on a bar graph where 1 represents square 1 to square 40 (41 is in 
jail).

Long: Monopoly is a popular board game where players buy and pay each other based on the properties they land on. 
This script attempts to show that the probability of landing on any given square is not uniform. This program 
simulates as many rolls as the user desires and keeps track of the frequency of landing on any particular 
square. Jail is the most popular square to land on and the most landed on property is Illinois Avenue. 


-------------------------------------------
moreSuccessful.py
-------------------------------------------

Run (if the user wants to only use hardcoded data):

python moreSuccessful.py 

Run (if the user wants to input data from terminal):

python moreSuccessful.py user

Short: This program develops confidence intervals on a list of player's population proportions of a Bernoulli event (ideally skill-based), 
compares player's point estimates to indicate if there is statistically significant evidence to suggest that not all proportions are the 
same (Chi-squared Hypothesis Testing), and if there is evidence, isolate which differences in the player's point estimates are statistically significant using the Marascuilo Procedure.

Long: Willing to ruin friendships by having statistically significant evidence that one is better than their friends at a skill-based game (which is also a Bernoulli event). This is the program to run. A hypothetical scenario:

Say a group of 3 (or more) friends wants to determine who is the better free-throw shooter. Each person should conduct a series of Bernoulli trials where a “success” is a person making a free throw and a “failure” is a person missing a free throw. Each friend should input their name, sample proportion of successes (call it p1 for friend 1), and trials they conducted into the program. Then after choosing some alpha levels, the following information will be displayed:

1. A confidence interval on the population proportion of each player's free throw percentage if and only if the Central Limit Theorem is applicable (ensure the friends make and miss at least 5 free throws)
2. A Hypothesis Test's results where the null hypothesis is p1 = p2 = p3 (the proportions are all equal) and the alternate hypothesis is Not all proportions are equal. This will use a Chi-Squared Distribution and compare each proportion to the hypothetical average proportion between all of the players.
3. If there is statistically significant evidence that the free throw point percentages are not all equal, a Marasculio Procedure will run to determine between which friends is there a statistically significant difference in proportions (technically making the case that there is evidence that one friend is a better free throw shooter than the other).


-------------------------------------------
shutTheBox.py
-------------------------------------------
Run:
python shutTheBox.py

Short: Simulates user-defined games of Shut the Box and records how many instances the user successfully shuts 
the box. Depicts additional statistics.

Long: Shut the box is a game where there is a set of 9 integers [1,2,3,4,5,6,7,8,9] and two dice. In each round, the 
two dice are rolled and the player must use a combination of the set of integers that results in the summation 
of the two dice. After this, all of the integers used for that round are removed from the set. If all integers 
are successfully removed from the set then you win and have "shut the box." If you end up with a dice roll that 
cannot be added up with the remaining integers in the set then you lose that game. 
This program was an attempt to find an optimal algorithm to win.

The generating function for the summation of two die is: A(z) = z^2 + 2z^3 + 3z^4 + 4z^5 + 5z^6 + 6z^7 + 5z^8 + 
4z^9 + 3z^10 + 2z^11 + z^12 where the exponent represents the summation of two dice and the coefficient is the 
number of ways two dice can sum up to the corresponding exponent. This can be used to determine the probability of 
rolling two dice and the sum equaling the exponent (coefficient/36). 

A brute force approach was used to generate all of the possible combinations of the numbers 1 through 9 
that sum to all of the possible dice rolls (2 through 12). Then, each number (1-9) is used as a key in a python 
dictionary. After a number is used in a potential summation (say of the number A), that corresponding number's
dictionary index was incremented by the weight or probability of rolling an A. The algorithm then will roll two 
dice and loop over all the possible combinations that the player can use. The algorithm will pick the combination 
of numbers that have the least weight (based on the dictionary).

Three other common methods are used (always pick the least amount of numbers and closest to the middle, pick the 
most amount of numbers, and randomly select a combination that works). As of now, the weight method described 
above has the best win rate (~6%). 

More accurate statistical conclusions are in the program (developing a confidence interval, showing statistics 
on games lost).

The second best was the "use least amount of numbers and closest to the center of the box" method at ~5.88%. To show 
this is a statistically significant difference, these two proportions can be compared with the  
comparingProportion.py file that performs a hypothesis test (the null hypothesis was rejected under 5% alpha level). 


-------------------------------------------
blackjack.py
-------------------------------------------
Run:
python blackjack.py

Short: Simulates user-defined number of rounds of blackjack. The user inserts 2 components that dictate the user's 
strategy. 1] Percentage of certainty that the user will not bust on any given hand 2] The absolute minimum 
amount of points the user is willing to get on any given hand (will override component 1).

Long: Simulates the game blackjack where a player continuously receives cards from the dealer (hit) until the sum 
of the player's cards is as close to 21 as possible (without going over). This simulates a player vs dealer 
scenario.

The dealer will win in the following situations:
- Both players bust (go over 21)
- User busts and Dealer does not
- Dealer has the same score or higher than the player (without busting)

Note: Dealer has no strategy except the dealer MUST hit until their score is >= 17 (will stop hitting after it 
meets this condition).

The user will win in the following situations:
- The user has a higher score than the dealer (without busting)
- The dealer busts and the player does not


-------------------------------------------
DreamProb.java
-------------------------------------------
Compile and Run:

javac DreamProb.java

java DropRatesTest

Short: Simulates 262 ender pearl and 305 blaze rod drop chances for user-defined iterations and compares them 
to popular Youtuber Dream's odds.

Long: A popular Minecraft Youtuber named Dream was accused of cheating during some of his Minecraft Speedruns
(playing through a game of Minecraft as fast as possible) by modifying the drop rate of two essential items 
needed to complete the game: Ender Pearls and Blaze Rods. This was suspected as Dream's drop rates were
significantly higher than the expected drop rate. The Minecraft Speedrunning Moderators published a youtube 
video (https://www.youtube.com/watch?v=-MYw9LcLCb4&t=615s) and a paper that showed how unlikely Dream's situation 
was.

Their paper used the Binomial Distribution as a basis to show the likelihood of getting 42/262 ender pearls 
(when the population proportion is ~5%) and getting 211/305 blaze rods (when the population proportion is 50%). 
This script simply runs as many iterations as the user desires and depicts how many instances of those 
iterations got the same blaze drop rate, the same ender pearl drop rate, and both.

Note: Minecraft uses Java's Random class as its random generator (for nearly everything). So I used it as well 
as a method of getting a different seed for the Random object. This simulation is a naive recreation of the 
issue at hand and does not EXACTLY represent Minecraft's method of determining blaze rod or ender pearl drops. 
However, I did my best to replicate the Moderator Team's published paper's description of Minecraft's usage of 
Java's Linear Congruential Generators.

