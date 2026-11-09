# Kirill Kaminskyi M12P5.py 11/09/2026

#array + process
file = open("M12P4", "r")

last_name = []
batting_average =[]

count = 0

for line in file:
    line = line.strip()

    if line == "":
        continue

    if count % 2 == 0:
        last_name.append(line)
    else:
        batting_average.append(float(line))

    count = count + 1

#function
def display_players():
    for count in range(len(last_name)):
        print(last_name[count], batting_average[count])

#function
def search_player(search_name):
    for count in range(len(last_name)):
        if last_name[count] == search_name:
            print(last_name[count])
            print(batting_average[count])
            break
    else:
        print("Name not found")

#inputs
do_program = input("Do you want to search for a player? ").lower()
if do_program == "yes":
    display_players()

while do_program == "yes":
    search_name = input("Enter player's last name: ")
    search_player(search_name)

    do_program = input("Do you want to search for another player? ").lower()