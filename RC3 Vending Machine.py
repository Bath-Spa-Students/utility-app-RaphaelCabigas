import random  # used for randomization of stocks
import fontstyle  # used for styling texts
import winsound  # used for audio cues for will run only for Windows
import time  # used for transition between texts

'''IMPORTANT!!! BEFORE RUNNING THE CODE: The winsound module is only available for Windows. 
   And you need to have PIP installed which is used for installing the fontstyle module 
   in order to use the following commands for fontstyle since it is not in the standard Python library.
   click the following links to learn more about PIP and fontstyle:
    PIP installation tutorial video: https://www.youtube.com/watch?v=fJKdIf11GcI
    PIP installation web page: https://pip.pypa.io/en/stable/installation/
    Reference of fontstyle module and its commands: https://www.geeksforgeeks.org/fontstyle-module-in-python/'''

# a vending_items list storing multiple dictionaries with their corresponding code, item, price, and stock
# I have implemented the random.randint(a,b) function for the stockage to choose a random number from 1 to 5 whenever the program runs
vending_items = [
    {"Code": "0", "Item": "Water",
     "Price": 1.00, "Stock": random.randint(1, 5)},
    {"Code": "1", "Item": "Fresh Milk", "Price": 2.20,
     "Stock": random.randint(1, 5)},
    {"Code": "2", "Item": "Orange Juice", "Price": 3.00,
     "Stock": random.randint(1, 5)},
    {"Code": "3", "Item": "Sports Drink", "Price": 4.50,
     "Stock": random.randint(1, 5)},
    {"Code": "4", "Item": "Rice Water", "Price": 1.30,
     "Stock": random.randint(1, 5)},
    {"Code": "5", "Item": "Garlic Bread",
     "Price": 2.25, "Stock": random.randint(1, 5)},
    {"Code": "6", "Item": "Dark Choco", "Price": 4.30,
     "Stock": random.randint(1, 5)},
    {"Code": "7", "Item": "Trail Mix", "Price": 1.20,
     "Stock": random.randint(1, 5)},
    {"Code": "8", "Item": "Cheesy Chips", "Price": 3.25,
     "Stock": random.randint(1, 5)},
    {"Code": "9", "Item": "Granola Bar", "Price": 5.35,
     "Stock": random.randint(1, 5)},
    {"Code": "10", "Item": "Chicken Soup", "Price": 2.30,
     "Stock": random.randint(1, 5)},
    {"Code": "11", "Item": "Cup Noodles", "Price": 2.00,
     "Stock": random.randint(1, 5)},
    {"Code": "12", "Item": "Fruit Salad", "Price": 3.25,
     "Stock": random.randint(1, 5)},
    {"Code": "13", "Item": "Beef Jerky", "Price": 6.40,
     "Stock": random.randint(1, 5)},
    {"Code": "14", "Item": "Sandwich", "Price": 4.30,
     "Stock": random.randint(1, 5)}
]

'''REMINDER: f strings, and \n (line breaks) are used through out the program so that certain print statements are neatly displayed. 
    And since vending_items and dictionaries are mutable objects, I can modify and access the contents of it inside of a function without setting it as a parameter
    so when changes are made, the list will be updated throughout the whole program'''


def error_audio():  # used to play a melody when error occur
    # winsound.beep function is used for playing a beep sound with which is set to the desired pitch and duration in milliseconds
    winsound.Beep(800, 150)
    winsound.Beep(500, 150)


def next_audio():  # used to play a melody when next input or display occur
    winsound.Beep(500, 125)
    winsound.Beep(800, 125)


def display_machine():
    '''for displaying the whole vending machine with a welcome message, categories, and items'''

    # fontstyle.apply(text,color/background color/style) function basically adds the desired color, background color, and text style to the desired text
    print("\n╔══════════════════════════════════════════════════╗")
    print(f'║{fontstyle.apply("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░","BLUE/BOLD")}║')
    print("╠══════════════════════════════════════════════════╣")
    print("║▓▓▓  ╔══════════════════════════════════════╗  ▓▓▓║")
    print(
        f'║▓▓   ║{fontstyle.apply("             Welcome To The           ","WHITE/BLUE_BG/BOLD")}║   ▓▓║')
    print(
        f'║▓    ║{fontstyle.apply("          RC3 Vending Machine!        ","WHITE/BLUE_BG/BOLD")}║    ▓║')
    print("║     ╠════════════╤════════════╤════════════╣     ║")
    print(
        f'║ ▬▬▬ ║{fontstyle.apply("  Drinks 🥛 ","WHITE/BLUE_BG/BOLD")}│{fontstyle.apply("  Snacks 🍫 ","WHITE/BLUE_BG/BOLD")}│{fontstyle.apply("  Others 🥪 ","WHITE/BLUE_BG/BOLD")}║ ①②③ ║')
    print("║ ↑↑↑ ╠══════╤═════╧═════════╤══╧════╤═══════╣ ④⑤⑥ ║")
    print(
        f'║ AED ║{fontstyle.apply(" Code ","WHITE_BG/BOLD")}│{fontstyle.apply(" Item          ","WHITE_BG/BOLD")}│{fontstyle.apply(" Price ","WHITE_BG/BOLD")}│{fontstyle.apply(" Stock ","WHITE_BG/BOLD")}║ ⑦⑧⑨ ║')
    print("║     ╠══════╪═══════════════╪═══════╪═══════╣  ⓪  ║")
    for item in vending_items:  # for loop iterates through each dictionary inside of the vending_items list
        # item["Code"] is used for accessing the value from each key in the dictionaries to be displayed
        # :<5 left alignment format specifier is used for left aligning the text which is set within the given width since the item code and name have different number of spacings
        # :.2f percision format specifier which is used for formatting the price to a float
        #   and specifiying the number of decimal places which is two decimals when displayed in the f string.
        #   Its also useful for prices like 2.00, when displayed in a string it will display it with the decimal points.
        print(
            f'║     ║ {item["Code"]:<5}│ {item["Item"]:<14}│ {item["Price"]:.2f}  │ {item["Stock"]}     ║     ║')

    print("║     ╚══════╧═══════════════╧═══════╧═══════╝     ║")
    print(f'║▓    ╔══════════════════════════════════════╗    ▓║')
    print(
        f'║▓▓   ║{fontstyle.apply("         ► Get Your Item Here ◄       ","WHITE/BLUE_BG/ITALIC/BOLD")}║   ▓▓║')
    print(f'║▓▓▓  ╚══════════════════════════════════════╝  ▓▓▓║')
    print("╠══════════════════════════════════════════════════╣")
    print(f'║{fontstyle.apply("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░","BLUE/BOLD")}║')
    print("╚══╦═══╦════════════════════════════════════╦═══╦══╝")
    print("   ║   ║                                    ║   ║   ")
    print("   ╚═══╝                                    ╚═══╝   ")


def input_money():
    '''for the money input'''
    while True:
        next_audio()
        try:  # try is used input that might raise an error and crash the program
            # money input that asks the user for the amount of money and converts it to float
            money = float(
                input("\nEnter amount of money (AED only): "))
        # except with the type of exception: ValueError, which is used for when the money input cannot be converted to a float like a string the except block executes
        except ValueError:  # display an invalid input message and repeat the loop
            error_audio()
            print(
                f'\n{fontstyle.apply("⚠  INVALID INPUT. PLEASE ENTER VALID AMOUNT OF MONEY ⚠ ","RED_BG/BOLD")}')
            # time.sleep(seconds) function adds a transition between texts, delaying the next code execution
            time.sleep(1)
        else:  # if no errors occur, the code below will execute
            if money > 0:  # If money is greater than 0, return the money value and exit the loop
                return money
            else:  # when money input is 0 or a negative number, display invalid number and repeat the loop
                error_audio()
                print(
                    f'\n{fontstyle.apply("⚠  INVALID NUMBER. PLEASE ENTER VALID AMOUNT OF MONEY ⚠ ","RED_BG/BOLD")}')
                time.sleep(1)

    # The implementation of a while loop here supports in error handling. So, when the else statement or except block executes it will then repeat the money input
    # try and except basically prevents the program from crashing and helps with error-handling


def choose_category():
    '''for the category input'''
    while True:
        next_audio()
        # category input that asks the user to choose a category (Drinks, Snacks, Others) or to quit
        # with an upper method that is helpful for whenever a user inputted with small letters or mixed with capital letters, the input will format to all capital letters
        category = input(
            "\nEnter a category (Drinks or Snacks or Others) or Enter 'N' to quit: ").upper()
        # return the category value and exit the loop
        if category == "DRINKS" or category == "SNACKS" or category == "OTHERS":
            return category
        elif category == "N":  # will return False which ends the program
            return False
        else:  # display an invalid input message and repeat the loop
            error_audio()
            print(
                f'\n{fontstyle.apply("⚠  INVALID INPUT. PLEASE ENTER VALID CATEGORY: Drinks or Snacks or Others ⚠ ","RED_BG/BOLD")}')
            time.sleep(1)

    # The implementation of a while loop here supports in error handling as well. When the else statement executes it will then repeat the category input


'''REMINDER: the following functions below has parameters of expected money and target category 
    which is used for when any changes are made to the money and category value those values are displayed, returned, and updated correctly
    throughout the whole program, within the scope of other functions and outside of the scope as well.'''


def display_category(expected_money, target_category):
    '''for displaying the selected category menu. The parameters of expected money and target category are used 
    to display the selected category with its categorized items and updated money'''

    # Since the returned category value is all capital letters, capitalize() method is used to neatly display proper capitalization of the category
    print("\n╔══════════════════════════════════════════════════╗")
    print(
        f'║{fontstyle.apply("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░","BLUE/BOLD")}║')
    print("╠══════════════════════════════════════════════════╣")
    print("║     ╔══════════════════════════════════════╗     ║")
    print(f'║     ║{fontstyle.apply("                 ","BLUE_BG")}{fontstyle.apply(target_category.capitalize(),"BLUE_BG/BOLD")}{fontstyle.apply("               ","BLUE_BG")}║ ①②③ ║')
    print("║     ╠══════╤═══════════════╤═══════╤═══════╣ ④⑤⑥ ║")
    print(
        f'║     ║{fontstyle.apply(" Code ","WHITE_BG/BOLD")}│{fontstyle.apply(" Item          ","WHITE_BG/BOLD")}│{fontstyle.apply(" Price ","WHITE_BG/BOLD")}│{fontstyle.apply(" Stock ","WHITE_BG/BOLD")}║ ⑦⑧⑨ ║')
    print("║     ╠══════╪═══════════════╪═══════╪═══════╣  ⓪  ║")
    if target_category == "DRINKS":
        # slices starting from 0 and 4 of the dictionaries inside of the vending_items list and display them (5 items)
        for item in vending_items[:5]:
            print(
                f'║     ║ {item["Code"]:<5}│ {item["Item"]:<14}│ {item["Price"]:.2f}  │ {item["Stock"]}     ║     ║')
    elif target_category == "SNACKS":
        # slices starting from 5 and 9
        for item in vending_items[5:10]:
            print(
                f'║     ║ {item["Code"]:<5}│ {item["Item"]:<14}│ {item["Price"]:.2f}  │ {item["Stock"]}     ║     ║')
    elif target_category == "OTHERS":
        # slices starting from 10 until the remaining dictionaries
        for item in vending_items[10:]:
            print(
                f'║     ║ {item["Code"]:<5}│ {item["Item"]:<14}│ {item["Price"]:.2f}  │ {item["Stock"]}     ║     ║')
    print("║     ╚══════╧═══════════════╧═══════╧═══════╝     ║")
    print(f'║▓    ╔══════════════════════════════════════╗    ▓║')
    print(
        f'║▓▓   ║{fontstyle.apply("         ► Get Your Item Here ◄       ","WHITE/BLUE_BG/ITALIC/BOLD")}║   ▓▓║')
    print(f'║▓▓▓  ╚══════════════════════════════════════╝  ▓▓▓║')
    print("╠══════════════════════════════════════════════════╣")
    print(
        f'║{fontstyle.apply("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░","BLUE/BOLD")}║')
    print("╚══════════════════════════════════════════════════╝")
    print(
        f'\n{fontstyle.apply(f"Current Balance: {expected_money:.2f} AED","WHITE_BG/BOLD")}')


def new_money(expected_money):
    '''for when the user needs to add more money in the vending machine with an expected_money parameter'''

    # call the input money function and the value from it is stored in the add_more variable
    add_more = input_money()
    # expected_money stores the sum of from adding it and the add_more value
    expected_money += add_more
    # displays the updated money and return the expected_money value
    next_audio()
    print(
        f'\n{fontstyle.apply(f"Your Balance is now: {expected_money:.2f} AED","BLUE_BG/ITALIC/BOLD")}')
    time.sleep(1)
    return expected_money


def display_again(expected_money, target_category):
    '''for when the user wants to buy again or not with parameters of expected_money and target_category'''
    next_audio()
    # again input asking the user to buy again or quit with an upper method
    again = input(
        "\nEnter any key to buy again or Enter 'N' to quit: ").upper()
    if again == "N":
        # store False value to target_category and return expected_money and target_category values
        target_category = False
        return expected_money, target_category
    else:
        display_machine()
        # If expected_money is less than 1, display the user doesn’t have enough money to buy an item and call the new_money function
        if expected_money < 1:
            print(
                f'\n{fontstyle.apply("You do not have enough money to buy an item. To continue, please add more money.","YELLOW_BG/BOLD")}')
            print(
                f'\n{fontstyle.apply(f"Current Balance: {expected_money:.2f} AED","YELLOW_BG/BOLD")}')
            winsound.Beep(1000, 500)
            winsound.Beep(1000, 500)
            time.sleep(1)
            expected_money = new_money(expected_money)
        else:  # expected_money is greater than 1, display the user's money
            print(
                f'\n{fontstyle.apply(f"Current Balance: {expected_money:.2f} AED","WHITE_BG/BOLD")}')
        # call choose_category function and the value from it is stored in target_category which is then returned with expected_money
        target_category = choose_category()
        return expected_money, target_category


def process_item(expected_money, target_category):
    '''for storing the selected_item conditions when processing the item with parameters of expected_money and target_category'''

    if selected_item["Stock"] == 0:  # selected item has no stock
        # store the following messages to warning and options_text
        warning = f'{selected_item["Item"]} is out of stock. Please try another item/category or come back again later.'
        options_text = "Enter 'Y' to choose another category or 'A' to choose another item from the same category"
    # user has insufficient funds for selected item
    elif expected_money < selected_item["Price"]:
        warning = f'You do not have enough money to buy {selected_item["Item"]}. Please try another item/category.'
        options_text = "Enter 'Q' to add more money or 'Y' to choose another category or 'A' to choose another item from the same category"
    # if any of these two conditions are valid it will execute the code below
    if selected_item["Stock"] == 0 or expected_money < selected_item["Price"]:
        # print the approriate warning for the condition
        print(f'\n{fontstyle.apply(warning, "YELLOW_BG/BOLD")}')
        winsound.Beep(1000, 500)
        winsound.Beep(1000, 500)
        time.sleep(1)
        # options input displays the approriate message with upper method
        next_audio()
        options = input(
            f'\n{options_text} or Enter any key to quit: ').upper()
        if options == 'Y':
            # call choose_category function and the value from it is stored in target_category which is then returned with expected_money
            target_category = choose_category()
            return expected_money, target_category
        elif options == 'A':
            # return the values of expected_money and target_category
            return expected_money, target_category
        elif options == 'Q' and expected_money < selected_item["Price"]:
            # call new_money function and the value from it is stored in expected_money which is then returned with target_category
            expected_money = new_money(expected_money)
            return expected_money, target_category
        else:  # store False value to target_category and return expected_money and target_category values
            target_category = False
            return expected_money, target_category
    else:  # when the selected_item is available and the user has sufficient funds
        # the selected item's stock will be subtracted by one
        selected_item["Stock"] -= 1
        # the expected_money will be subtracted as well by the selected_item's price
        expected_money -= selected_item["Price"]
        # Displays the updated selected item stock, remaining balance, dispensing item, and a message that user has dispensed the item
        next_audio()
        print(
            f'\n{fontstyle.apply(f"Your Balance is now: {expected_money:.2f} AED","BLUE_BG/ITALIC/BOLD")}\n')
        time.sleep(1.2)
        next_audio()
        print(fontstyle.apply(f'{selected_item["Item"]} Stock: ', 'WHITE_BG/ITALIC/BOLD') +
              fontstyle.apply(f'{selected_item["Stock"]} remaining', 'WHITE_BG/ITALIC/BOLD') + "\n")
        time.sleep(1.2)
        print(fontstyle.apply(
            f'Please wait for {selected_item["Item"]} is currently dispensing...', 'BLACK_BG/BOLD') + "\n")
        winsound.Beep(900, 250)
        winsound.Beep(1000, 250)
        winsound.Beep(1200, 250)
        winsound.Beep(900, 200)
        winsound.Beep(1000, 200)
        winsound.Beep(1200, 200)
        winsound.Beep(900, 200)
        winsound.Beep(1000, 250)
        winsound.Beep(1200, 900)
        time.sleep(2)
        print(fontstyle.apply(
            f'Here is your {selected_item["Item"]}! \(^-^)/', 'BLUE_BG/BOLD'))
        winsound.Beep(1000, 500)
        winsound.Beep(1300, 300)
        winsound.Beep(1400, 900)
        time.sleep(1)
        # call and return display_again function indicating that the purchase has ended
        return display_again(expected_money, target_category)


def end_program(expected_money):
    '''for displaying the end message when the program ends with an expected_money parameter'''
    winsound.Beep(1000, 800)
    winsound.Beep(800, 800)
    winsound.Beep(600, 1000)
    print(f'\n{fontstyle.apply(f"Here is your change: {expected_money:.2f} AED","WHITE_BG/BOLD")}')
    print(
        f'\n{fontstyle.apply("Thank you for buying at RC3 Vending Machine! We hope to see you again! (^-^)/","BLUE_BG/BOLD")}')


'''initializing the start of the vending machine program by calling the display_machine function, 
    calling the input_money function and the value returned from it is stored in current_money, 
    and calling the choose_category function and the value returned from it is stored in valid_category.'''

display_machine()
winsound.Beep(600, 725)
winsound.Beep(800, 725)
winsound.Beep(1000, 725)
winsound.Beep(600, 800)
winsound.Beep(800, 900)
current_money = input_money()
print(
    f'\n{fontstyle.apply(f"Current Balance: {current_money:.2f} AED","WHITE_BG/BOLD")}')
valid_category = choose_category()

'''The following code below will be under a while loop which is used for looping through the whole process of the vending machine program 
and parameters of expected_money and target_category for each function have been set to arguments of current_money and valid_category.'''

while True:
    if valid_category == False:
        # call end_program function and break the while loop
        end_program(current_money)
        break

    # This if statement occurs first in the while loop to check the value returned in valid_category from the previous line
    # and from the functions that will be called later on, giving the user a way to quit '''

    display_category(current_money, valid_category)
    next_audio()
    # an item_code input that asks the user to enter the corresponding code for the item from the displayed category or quit with an upper method.
    item_code = input(
        "\nEnter the corresponding code for the item that you would like to buy or 'Y' to choose another category or 'N' to quit: ").upper()
    if item_code == "Y":  # call the choose_category function and store it in the valid_category and repeat the while loop
        valid_category = choose_category()
    elif item_code == "N":  # display end message and break the while loop, ending the program
        end_program(current_money)
        break
    # REMINDER: when the user enters a string that is not 'Y' or 'N' it will just run the except block and repeat the while loop
    else:
        try:
            # converts the item_code to integer and store it in valid_code
            valid_code = int(item_code)
        except ValueError:  # when the item_code input cannot be converted to an integer like a float or string
            # displays invalid input message and repeat the while loop
            error_audio()
            if valid_category == "DRINKS":
                print(
                    f'\n{fontstyle.apply("⚠  INVALID INPUT. PLEASE ENTER A VALID CODE BETWEEN 0 AND 4 ⚠ ","RED_BG/BOLD")}')
            elif valid_category == "SNACKS":
                print(
                    f'\n{fontstyle.apply("⚠  INVALID INPUT. PLEASE ENTER A VALID CODE BETWEEN 5 AND 9 ⚠ ","RED_BG/BOLD")}')
            elif valid_category == "OTHERS":
                print(
                    f'\n{fontstyle.apply("⚠  INVALID INPUT. PLEASE ENTER A VALID CODE BETWEEN 10 AND 14 ⚠ ","RED_BG/BOLD")}')
            time.sleep(1)
        else:  # if no errors occur, the code below will execute
            if valid_category == "DRINKS":
                if valid_code in range(0, 5):  # when valid_code is from 0 to 4
                    # selected_item variable that stores the vending_items with a corresponding number for the item which we get from valid_code
                    selected_item = vending_items[valid_code]
                    # call process_item function and stores the values returned to current_money and valid_category
                    current_money, valid_category = process_item(
                        current_money, valid_category)
                else:  # when the input is not from 0 to 4 and repeat the loop
                    error_audio()
                    print(
                        f'\n{fontstyle.apply("⚠  INVALID CODE. PLEASE ENTER A VALID CODE BETWEEN 0 AND 4 ⚠ ","RED_BG/BOLD")}')
                    time.sleep(1)
            elif valid_category == "SNACKS":
                if valid_code in range(5, 10):
                    selected_item = vending_items[valid_code]
                    current_money, valid_category = process_item(
                        current_money, valid_category)
                else:
                    error_audio()
                    print(
                        f'\n{fontstyle.apply("⚠  INVALID CODE. PLEASE ENTER A VALID CODE BETWEEN 5 AND 9 ⚠ ","RED_BG/BOLD")}')
                    time.sleep(1)
            elif valid_category == "OTHERS":
                if valid_code in range(10, 15):
                    selected_item = vending_items[valid_code]
                    current_money, valid_category = process_item(
                        current_money, valid_category)
                else:
                    error_audio()
                    print(
                        f'\n{fontstyle.apply("⚠  INVALID CODE. PLEASE ENTER A VALID CODE BETWEEN 10 AND 14 ⚠ ","RED_BG/BOLD")}')
                    time.sleep(1)
