stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    for item in stuff:
        print(stuff[item], item)

    item_cnt = sum(stuff[item] for item in stuff)
    print(f"Total number if items: {item_cnt}")


if __name__ == "__main__":
    displayInventory(stuff)
