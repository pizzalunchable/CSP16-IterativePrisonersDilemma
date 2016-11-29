####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team Lunchable (GM, JM)' # Only 10 chars displayed.
strategy_name = 'The Spice n Dice'
strategy_description = 'This strategy accounts for score differences and the past histories of the opposing team'
    
def move(my_history, their_history, my_score, their_score):
    if my_score <= 0:
        return 'b'
    if (their_score) - (my_score) >= 500:
        return 'b'
    else:
        if their_history == 'b':
            return 'b'
        else:
            return 'c' 
    
           