# Solutions of Question 17, Chapter 7. 
import random

# Your friend will complete this function
def play_once(human_plays_first):
    """
    Must play one round of the game. If the parameter
    is True, the human gets to play first, else the
    computer gets to play first.  When the round ends,
    the return value of the function is one of
    -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                    .format(human_plays_first, result))
    return result

# a. Write the main program which repeatedly calls this function to play the game, 
#   and after each round it announces the outcome as: 
#   “I win!”, “You win!”, or “Game drawn!”. 
#   It then asks the player “Do you want to play again?” 
#   and either plays again, or says “Goodbye”, and terminates.

# b. Keep score of how many wins each player has had, 
#   and how many draws there have been. After each round of play, 
#   also announce the scores.

# c. Add logic so that the players take turns to play first.

# d. Compute the percentage of wins for the human, out of all games played. 
#   Also announce this at the end of each round.

# e. Draw a flowchart of your logic.

def play_game():
    # score
    player_score = 0
    computer_score = 0
    count_draw = 0
    # win_percentage_for_human = 0.0

    while True:
        # Take turns to play first
        play_first = random.choice([True, False])
        result = play_once(play_first)

        if result == -1:
            player_score += 1
            print("You win!")
        elif result == 0:
            count_draw += 1
            print("Game drawn!")
        elif result == 1:
            computer_score += 1
            print("I win!")

        # show score
        print("Your score: {0}\tComputer's score: {1}\tGame Draws: {2}"
            .format(player_score, computer_score, count_draw))

        # percentage of wins for the human
        play_times = player_score + computer_score + count_draw
        win_percentage_for_human = player_score / play_times
        print("Your percentage of wins: {}".format(win_percentage_for_human))
        print("")

        # ask if player wants to continue
        is_continue = int(input("Do you want to play again?\n1. Yes\t2. No\n"))
        print("-----------------------")
        if is_continue == 1:
            continue
        else:
            print("Goodbye!")
            break

play_game()
