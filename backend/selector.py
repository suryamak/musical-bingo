from random import randint

lines = []
list = []
selected = []

with open('txt/cleaned_items.txt', 'r') as file:
    lines = file.readlines()
    
while len(selected) < 100:
    x = randint(0, len(lines))
    if x not in selected:
        list.append(lines[x])
        selected.append(x)

with open('txt/selected_items.txt', 'w') as file:
    file.writelines(list)