# Open file and read the calories and split them into items in list
input_file = open("day_2_input.txt", "r")
file = input_file.read()
games = file.split('\n')
id_sum = 0
for game in games:
    game = game.split(":")
    gameid = game[0].replace("Game ","")
    rlim = 0 
    glim = 0
    blim = 0 
    try:
        game = game[1].split(";")
    except:
        continue  
    for gset in game:
        gset = gset.split(",")        
        for dice in gset:
            if "red" in dice:
                dice = dice.replace(" red","")
                if int(dice) > rlim:
                    rlim = int(dice)
            if "green" in dice:
                dice = dice.replace(" green","")
                if int(dice) > glim:
                    glim = int(dice)
            if "blue" in dice:
                dice = dice.replace(" blue","")
                if int(dice) > blim:
                    blim = int(dice)
    id_sum += rlim * glim * blim 
print(id_sum)
        
#        rsum = 0
#        gsum = 0
#        bsum = 0
#        rlim = 12
#        glim = 13
#        blim = 14
#        for dice in gset:
#            if "red" in dice:
#                dice = dice.replace(" red","")
#                rsum += int(dice)
#            if "blue" in dice:
#                dice = dice.replace(" blue","")
#                bsum += int(dice)
#            if "green" in dice:
#                dice = dice.replace(" green","")
#                gsum += int(dice)
#        if rsum <= rlim and gsum <= glim and bsum <= blim:
#           set_check += 1
#    if set_check == len(game):
#       id_sum += int(gameid)
#print(id_sum)
