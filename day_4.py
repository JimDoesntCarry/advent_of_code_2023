input_file = open("day_4_input.txt", "r")
data_raw = input_file.read()
data_matrix = data_raw.split('\n')
data_matrix.pop()
tickets = []
punktzahl = 0
cards = 0
y=0
for ticket in data_matrix:
    ticket = ticket + " | 0"
    ticket = ticket.split(": ")[1].split(" | ")
    ticket = [nr.split(" ") for nr in ticket]
    for i in range(len(ticket)):
        ticket[i] = list(filter(None, ticket[i]))
    for i in range(len(ticket)):
        for j in range(len(ticket[i])):
            ticket[i][j] = int(ticket[i][j])
    tickets.append(ticket)

for ticket in tickets:
    y += 1
    for iteration in range(int(ticket[2][0])+1):
        cards += 1
        counter = 0
        for tipp in ticket[1]:
            if tipp in ticket[0]:
                counter += 1
        for x in range(counter):
            try:
                tickets[x+y][2][0] += 1
            except Exception as e:
                print(e)
                print(x,y)
    
print(cards)
