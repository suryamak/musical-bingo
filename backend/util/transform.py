items = []

with open('txt/items.txt', 'r') as file:
    items = file.readlines()

items.sort()

with open('txt/cleaned_items.txt', 'w') as file:
    file.writelines(items)