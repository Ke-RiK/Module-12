# Kirill Kaminskyi M12P1.py 11/04/2026

#array
last_name = ["Name1", "Name2", "Name3", "Name4", "Name5", "Name6", "Name7", "Name8", "Name9", "Name10" ]

#functions
def display_names ():
    for count in range(10):
        print(last_name[count])

def display_reverse ():
    for name in reversed(last_name):
        print(name)

#outputs
display_names()

display_reverse()