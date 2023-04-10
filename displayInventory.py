stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(Inventory):
    # your code goes here
    print('Inventory: ')
    for item in Inventory:
        print(Inventory[item], item)

    item_cnt = sum(Inventory[item] for item in Inventory)
    print(f"Total number of items: {item_cnt}")


if __name__ == "__main__":
    displayInventory(stuff)
