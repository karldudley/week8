#========The beginning of the class==========
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f'''
Country: {self.country}
Code: {self.code}
Name: {self.product}
Cost: {self.cost}
Quantity: {self.quantity}
        '''
#=============Shoe list===========
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    shoe_list.clear()
    try:
        # read the shoes file
        file = open("inventory.txt", "r")
        print("\nData found. Reading...\n")
        all_shoes = file.read()
        
        # create a list of shoes
        shoe_line = all_shoes.split("\n")

        # loop through list of shoes and print to screen
        for pos, shoe in enumerate(shoe_line, 1):
            # split shoe into each seperate detail
            deets = shoe.split(',')

            # skip first line of the file
            if pos == 1:
                continue
            
            # break for loop if we reached the last line of the file
            if len(deets) <= 1:
                break

            # create shoe object and append to shoes list
            new_shoe = Shoe(deets[0], deets[1], deets[2], int(deets[3]), int(deets[4]))
            shoe_list.append(new_shoe)

    except FileNotFoundError as error:
        print("The file was not found")
        print(error)

    finally:
        # close the file
        if file is not None:
            file.close()

def write_shoes_data():
    # write the updated shoe list to file
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for shoe in shoe_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

def capture_shoes():
    # get user input
    print()
    country = input("Please enter country:\t")
    code = input("Please enter code:\t")
    name = input("Please enter name:\t")
    cost = int(input("Please enter cost:\t"))
    quantity = int(input("Please enter quantity:\t"))
    print()
    # create shoe object and append to shoes list
    new_shoe = Shoe(country, code, name, cost, quantity)
    shoe_list.append(new_shoe)

    # update file with captured data
    write_shoes_data()

def view_all():
    for pos, shoe in enumerate(shoe_list):
        print(f"------------------Line {pos}------------------")
        print(shoe)

def re_stock():
    # find the lowest stock in the shoe list
    lowest = shoe_list[0]
    index = 0
    for pos, shoe in enumerate(shoe_list,0):
        if shoe.quantity < lowest.quantity:
            lowest = shoe
            index = pos

    # show the lowest stock
    print("\nLowest Stock")
    print(lowest)

    # ask how much to restock by
    while (True):
        try:
            restock = int(input("How much would you like to restock?\t"))
            break
        except ValueError:
            print("Oops! That was not a valid number. Try again...")

    # print restock details and update the correct shoe in the list
    print(f"\nAdding {restock} to stock\n")
    shoe_list[index].quantity += restock

    # update file with restock
    write_shoes_data()

def search_by_id():
    # ask how much to restock by
    shoe_id = input("\nEnter the shoe ID:\t")
    if (search_shoe(shoe_id)):
        print("\nShoe found...")
        print(search_shoe(shoe_id))
    else:
        print("\nShoe not found...\n")

def search_shoe(id):
    for shoe in shoe_list:
        if shoe.code == id:
            return shoe
    # return false if no match
    return False

def value_per_item():
    print("Total value per shoe line. Printing...\n")

    # loop though shoe list and print the shoe details and total value
    for pos, shoe in enumerate(shoe_list,1):
        print(f"------------------Line {pos}------------------")
        print(shoe)
        print(f"Total value: {shoe.quantity} x {shoe.cost} = {shoe.quantity*shoe.cost}\n")

def highest_qty():
    # set highest to the first shoe in the list
    highest = shoe_list[0]

    # find the highest stock in the shoe list
    for shoe in shoe_list:
        if shoe.quantity > highest.quantity:
            highest = shoe

    # show the highest stock
    print("\nHighest Stock")
    print(highest)


#==========Main Menu=============
# read shoe file and store in list
read_shoes_data()

print("Welcome to Inventory Manager\n")

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following options below:

r  - Read shoe data from file
m  - Manually add shoe data
va - View all shoe lines
vh - View highest stock
vv - View value of each stock line
u  - Update lowest stock
s  - Search by ID
e  - Exit
: ''').lower()

    if menu == 'r':
        read_shoes_data()
    elif menu == 'm':
        capture_shoes()
    elif menu == 'va':
        view_all()
    elif menu == 'u':
        re_stock()
    elif menu == 'vh':
        highest_qty()
    elif menu == 'vv':
        value_per_item()
    elif menu == 's':
        search_by_id()
    elif menu == 'e':
        print('\nGoodbye!!!\n')
        exit()
    else:
        print("\nYou have made a wrong choice. Please try again...\n")
