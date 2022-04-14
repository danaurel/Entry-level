import random
def RPS_game():
    games = 0
    wins = 0
    items = ['rock', 'paper', 'scissor']
    CPU_play = random.choice(items)

    while games < 3:
        play = input('Rock, Paper, Scissor...shoot! ').lower()
        if play == CPU_play:
            print ('Match! Go again')
            games = games-1
        elif play == items[0] and CPU_play == items[1]:
            print( 'You suck! Try again hehe')
            
            games = games+1
        elif play == items[0] and CPU_play == items[2]:
            print( 'Congrats! You beat me')
            
            games = games+1
            wins = wins +1
        elif play == items[1] and CPU_play == items[0]:
            print( 'Congrats! You beat me')
            
            games = games+1
            wins = wins +1
        elif play == items[1] and CPU_play == items[2]:
            print( 'You suck! Try again hehe')
            
            games = games+1
        elif play == items[2] and CPU_play == items[1]:
            print( 'Congrats! You beat me')
            
            games = games+1
            wins = wins +1
        elif play == items[2] and CPU_play == items[0]:
            print( 'You suck! Try again hehe')
            games = games+1

        else:
            print( 'Please enter rock, paper,or scissor')

    return ('You have won ' +str(wins)+ ' games out of ' + str(games))
