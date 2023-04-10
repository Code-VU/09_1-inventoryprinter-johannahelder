import pytest
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    for item in inventory:
        print(inventory[item], item)

    item_cnt = sum(inventory[item] for item in inventory)
    print(f"Total number of items: {item_cnt}")


if __name__ == "__main__":
    displayInventory(stuff)
