# Open file and read the calories and split them into items in list
input_file = open("day_1_input.txt", "r")
data = input_file.read()
rows = data.split('\n')

stars = []
for y in rows:
    for x in y:
        if x != int and x != char  :
            stars.append([x,y])
for y in rows:
    for x in y:
        if int(x):

