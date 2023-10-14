import random
from area_codes import area_codes
import os
import webbrowser

# Clear screen function!
def clear_screen():
    # Check if the operating system is Windows or not
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


os.system('cls')
while True:

    clear_screen()
    print("Welcome to the Ultimate Python Phone Number Generator!")
    print()
    print("1. View Area Codes")
    print()
    print("2. Generate a Phone Number")
    print()
    print("3. Credits")
    print()
    print("4. Information")
    print()
    print("5. Github")
    print()
    choice = input("What would you like to do?: ")

    if choice == "1":

        clear_screen()
        print(area_codes)

        leave = input("Press enter to leave!")

        clear_screen()
        
    elif choice == "2":

        clear_screen()
        amount_of_numbers = int(input("How many phone numbers do you want to generate?: "))
        first_digits = int(input("What is the area code for the number?: "))

        for i in range(amount_of_numbers):
            second_digits = random.randint(100, 999)
            third_digits = random.randint(1000, 9999)
            print("+1", first_digits, second_digits, third_digits)

        leave = input("Press Enter to leave!")
        clear_screen()
        
    elif choice == "3":
    
        clear_screen()
        print("Made by @ToughLuck5562, @lua_python")
        print()
        leave = input("Press Enter to leave!")
        clear_screen()
    elif choice == "4":
        
        clear_screen()
        print("Phone number generator!")
        print()
        leave = input("Press Enter to leave!")
        clear_screen()
    elif choice == "5":
        
        clear_screen()
        webbrowser.open('https://github.com')
