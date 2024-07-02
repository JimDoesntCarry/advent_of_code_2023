input_file = open("day_4_input.txt", "r")
data_raw = input_file.read()
data_matrix = data_raw.split('\n')

punktzahl = 0

for ticket in data_matrix:
    try:
        ticket = ticket.split(": ")[1].split(" | ")
    except Exception as e:
        print(e)
        print(ticket)
    ticket = [nr.split(" ") for nr in ticket]
    counter = 0
    for i in range(len(ticket)):
        ticket[i] = list(filter(None, ticket[i]))
    try:
        for tipp in ticket[1]:
            if tipp in ticket[0]:
                counter += 1
    except Exception as e:
        print(e)
        print(ticket)
    if counter == 1:
        punktzahl += 1
    elif counter > 1:
        punktzahl += 2**(counter-1)
print(punktzahl)
