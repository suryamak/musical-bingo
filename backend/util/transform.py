sortedItems = []

with open('txt/items.txt', 'r') as file:
    items = file.readlines()
    for i, item in enumerate(items):
        dashPos = item.index('-')
        sortedItems.append(item[dashPos+2:-1] + ' - ' + item[:dashPos-1] + '\n')

sortedItems.sort()

with open('txt/cleaned_items.txt', 'w') as file:
    file.writelines(sortedItems)