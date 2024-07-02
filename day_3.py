# Open file and read the calories and split them into items in list
input_file = open("day_3_input.txt", "r")
data = input_file.read()
data_map = data.split('\n')
data_map.pop()
checker = 0
part_holder = []
valid_part_number = []
gear_dict = {}
check_coords = []
invalid_part_number = []
gear_values = []

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
                    if data_map[y+i][x+j]=="*":
                        checker = 1
                        check_coords = [y+i,x+j]
        if not data_map[y][x].isdigit() and checker == 1:
            checker = 0
            if gear_dict.get(str(check_coords)):
                gear_values.append(int(gear_dict.get(str(check_coords)))*int(''.join(map(str,part_holder))))
            else:
                gear_dict.update({str(check_coords):int(''.join(map(str,part_holder)))})
            part_holder = []
            check_coords = []
        if not data_map[y][x].isdigit() and checker == 0:
            if part_holder != []:
                invalid_part_number.append(int(''.join(map(str,part_holder))))
            part_holder = []
try:
    print(sum(gear_values))
    print(gear_values)
except Exception as e:
    print(e)
