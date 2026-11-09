# Kirill Kaminskyi M12P3.py 11/04/2026

#array
last_name = ["Smith", "Brown", "Johnson", "Kam"]
score = [85, 92, 78, 95]

#process
high_var = 0
high_index = 0

for count in range(len(score)):
    if score[count] > high_var:
        high_var = score[count]
        high_index = count

low_var = 999
low_index = 0

for count in range(len(score)):
    if score[count] < low_var:
        low_var = score[count]
        low_index = count

#outputs
print("Highest score")
print(high_var, last_name[high_index])
print()
print("Lowest score")
print(low_var, last_name[low_index])