# Open file and read the calories and split them into items in list
input_file = open("day_1_input.txt", "r")
coordinates = input_file.read()
splitted_coordinates = coordinates.split('\n')

# Sum of coordinates 
summe = 0
numbers = [["one","1"],["two","2"],["three","3"],["four","4"],["five","5"],["six","6"],["seven","7"],["eight","8"],["nine","9"]]


for i in splitted_coordinates:
    print(i)
    for x in numbers:
        if x[0] in i:
           i = i.replace(x[0],str(x[0]+x[1]+x[0]))
    print(i)
    for j in i:
        try:
            j = int(j)
        except:
            j = j
        if j in range(0,10):
            print(j*10)
            summe += j*10
            break;
    for j in reversed(i):
        try:
            j = int(j)
        except:
            j = j
        if j in range(0,10):
            print(j)
            summe += j
            break;

print(summe)
