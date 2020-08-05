import random
# Each player object must include a name, score, and guess
# 1) create a list of objects
players = [
    {'name': "Natalie",
    'score': 0,
    'guess': 9},
    {'name': "Pat",
    'score': 0,
    'guess': 8},
    {'name': "Dan",
    'score': 0,
    'guess': 5},
    {'name': "Adrian",
    'score': 0,
    'guess': 7},
    {'name': "Odion",
    'score': 0,
    'guess': 2},
]

# write a function that, given a list of player objects, returns the player with the highest score
# a random number between 1 and 10 is generated
# numbers greater than random number gain 10 points
# numbers less than random number gain 5 points
# numbers equal to random number gain 15 points

## Pseduocode
# declare a function and accept player list as paramater

# Then, generate a random number
rnd=round(random.random()*10)
print("our random number is",rnd)
# Next, a for loop should compare each guess to the rnd number and assign a score
def scoreit(list):
    highscorer=[]
    maxscore=0
    for player in list:
        if player['guess']>rnd:
            player['score']+=10
        elif player['guess']<rnd:
            player['score']+=5
        else:
            player['score']+=15
        if player['score']>maxscore:
            maxscore=player['score']
            highscorer=player['name']
    for player in list:
        print(player)
    print("And now, the final results:")
    return(highscorer,maxscore)

print(scoreit(players))