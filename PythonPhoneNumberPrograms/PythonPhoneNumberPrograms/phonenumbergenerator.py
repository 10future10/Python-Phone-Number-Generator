import random
import os
from area_codes import area_codes

name = """    
.____                     __________          __  .__                   
|    |    __ _______      \______   \___.__._/  |_|  |__   ____   ____  
|    |   |  |  \__  \      |     ___<   |  |\   __\  |  \ /  _ \ /    \ 
|    |___|  |  // __ \_    |    |    \___  | |  | |   Y  (  <_> )   |  \
|_______ \____/(____  /____|____|    / ____| |__| |___|  /\____/|___|  /
        \/          \/_____/         \/                \/            \/ 
"""

try:
    import webbrowser
except ImportError:
    try:
        import pip
        pip.main(["install", "webbrowser"])
        import webbrowser
    except ImportError:
        print("Failed to install 'webbrowser'. Please install it manually using 'pip'.")
        exit(1)

# Clear screen function
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    clear_screen()
    print(name)
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
    print("6. Imported Librarys")
    print()
    choice = input("What is your choice??: ")

    if choice == "1":
        clear_screen()
        print(area_codes)
        leave = input("Press enter to leave!")
        clear_screen()
        
    elif choice == "2":
        clear_screen()
        amount_of_numbers = int(input("How many phone numbers do you want to generate?: "))
        country_code = int(input("What is the country code?: "))
        first_digits = int(input("What is the area code for the number?: "))

        for i in range(amount_of_numbers):
            second_digits = random.randint(100, 999)
            third_digits = random.randint(1000, 9999)
            print(f"+{country_code}", first_digits, second_digits, third_digits)
            
        print()
        print(f"Done! Generated :  {amount_of_numbers} phone numbers!")
        leave = input("Press Enter to leave!")
        clear_screen()
        
    elif choice == "3":
        clear_screen()
        print("Made by @ToughLuck5562, @lua_python, & 10future10")
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
        webbrowser.open('https://github.com/10future10/Python-Phone-Number-Generator/tree/main/PythonPhoneNumberPrograms')
        
    elif choice == "6":
        clear_screen()
        print("Imported Python Librarys")
        print()
        print("1. webbrowser")
        print("2. os")
        print("3. Random")
        print('4. area_codes')
        print()
        leave = input("Press Enter to leave!")