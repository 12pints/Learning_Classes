myInventory = {"sprockets" : 5, "widgets" : 11, "cogs" : 3, "gizmos": 15}


def orderMore(inventory,goal):
    result=[]
    for item in inventory:
        value = inventory[item]
        if value < goal:
           result.append(item)

    return result

print("You are short on the following items:", orderMore(myInventory, 7))