def add_menu(menu, item):
 
    if item not in menu:
        menu.append(item)
    else:
        print(f"'{item}' is already on the menu.")


def remove_menu(menu, item):
   
    if item in menu:
        menu.remove(item)
    else:
        print(f"'{item}' is not in the menu.")


def check_menu(menu, item):
   
    if item in menu:
        return f"{item} is available."
    else:
        return f"{item} is not available."


initial_menu = input("Enter the initial menu items separated by commas: ").split(",")
initial_menu = [item.strip() for item in initial_menu]
add_item_name = input("Enter the item to add: ")
remove_item_name = input("Enter the item to remove: ")
check_item_name = input("Enter the item to check: ")

add_menu(initial_menu, add_item_name)
remove_menu(initial_menu, remove_item_name)
availability = check_menu(initial_menu, check_item_name)

print("Updated menu:", initial_menu)
print("Availability:", availability)
