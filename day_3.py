# Open file and read the calories and split them into items in list
input_file = open("day_3_input.txt", "r")
data = input_file.read()
data_map = data.split('\n')
data_map.pop()
checker = 0
part_holder = []
valid_part_number = []
invalid_part_number = []

yrange = range(-1,2)
xrange = range(-1,2)

for y in range(0,len(data_map)):
    for x in range(0,len(data_map[y])):
        if data_map[y][x].isdigit():
            part_holder.append(data_map[y][x])
            if y == 0:
                yrange = range(0,2)
            elif y == len(data_map)-1:
                yrange = range(-1,1)
            else:
                yrange = range(-1,2)
            if x == 0:
                xrange = range(0,2)
            elif x == len(data_map[y])-1:
                xrange = range(-1,1)
            else:
                xrange = range(-1,2)
            for i in yrange:
                for j in xrange:
                    try:
                        if data_map[y+i][x+j].isdigit() == False and data_map[y+i][x+j] != ".":
                            checker = 1
                    except Exception as e:
                        print(e)
                        print("x = ",x)
                        print("y = ",y)
                        print("xrange = ",xrange)
                        print("yrange = ",yrange)
                        print("xlen = ",len(data_map[y]))
                        print("ylen = ",len(data_map))
        if not data_map[y][x].isdigit() and checker == 1:
            checker = 0
            valid_part_number.append(int(''.join(map(str,part_holder))))
            part_holder = []
        if not data_map[y][x].isdigit() and checker == 0:
            if part_holder != []:
                invalid_part_number.append(int(''.join(map(str,part_holder))))
            part_holder = []
try:
    print(sum(valid_part_number))
    print(valid_part_number)
except Exception as e:
    print(e)
#stars = []
#part_number = []
#part_coordinates = []
#
#for y in range(0,len(data_map)):
#    for x in range(0,len(data_map[y])):
#        if data_map[y][x].isdigit() == False and data_map[y][x] != ".":
#            stars.append([x,y])
#
#for star in stars:
#    x = star[0]-1
#    y = star[1]-1
#    for i in range(4):
#        try:
#            if data_map[y][x].isdigit():
#                part_coordinates.append([x,y])
#            else:
#                if i%2 == 0:
#                    x += 1
#                if i%2 == 1:
#                    y += 1
#        except:
#            continue
#
#for part_coord in part_coordinates:
#    x = part_coord[0]
#    y = part_coord[1]
#    number = str(data_map[y][x])
#    while(1):
#        if data_map[y][x-1].isdigit():
#            number = data_map[y][x-1] + number
#            x = x-1
#        else:
#            break
#    x = part_coord[0]
#    while(1):
#        if data_map[y][x+1].isdigit():
#            number = number.append(data_map[y][x+1])
#            x = x+1
#        else:
#            break
#    part_number = part_number.append(number)
#
#print(sum(part_number))
