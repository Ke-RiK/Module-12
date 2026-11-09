# Kirill Kaminskyi M12P2.py 11/04/2026

#array
last_name = ["Name1", "Name2", "Name3", "Name4", "Name5", "Name6", "Name7", "Name8", "Name9", "Name10"]
exam_score = [10, 30, 78, 90, 70, 88, 55, 65, 99, 73]
#functions
def display_names ():
    for count in range(10):
        print(last_name[count], exam_score[count])


def display_reverse ():
    for name in reversed(last_name):
        print(name, exam_score[last_name.index(name)])

#outputs
display_names()

display_reverse()