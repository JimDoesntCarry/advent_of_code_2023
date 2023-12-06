# Open file and read the calories and split them into items in list
input_file = open("day_1_input.txt", "r")
data = input_file.read()
data_map = data.split('\n')

stars = []
part_number = []
part_coordinates = []
for y in range(0,len(data_map)):
    for x in range(0,len(data_map[y])):
        if data_map[y][x].isdigit() == False and data_map[y][x] != ".":
            stars.append([x,y])

for star in stars:
    x = star[0]-1
    y = star[1]-1
    for i in range(4):
        try:
            if data_map[y][x].isdigit():
                part_coordinates.append([x,y])
            else:
                if i%2 == 0:
                    x += 1
                if i%2 == 1:
                    y += 1
        except:
            continue

for part_coord in part_coordinates:
    x = part_coord[0]
    y = part_coord[1]
    number = str(data_map[y][x])
    while(1):
        if data_map[y][x-1].isdigit():
            number = data_map[y][x-1] + number
            x = x-1
        else:
            break
    x = part_coord[0]
    while(1):
        if data_map[y][x+1].isdigit():
            number = number.append(data_map[y][x+1])
            x = x+1
        else:
            break
    part_number = part_number.append(number)

print(sum(part_number))
