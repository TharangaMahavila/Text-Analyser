import main_menu
import importlib

importlib.reload(main_menu)

mainMenu = main_menu.MainMenu()

attempts = 0

print("Welcome to the Text Analyser!\nThis programme analyses text files and provides statistical insights.")
while True:
    if attempts == 5:
        print("It seems you have entered five consecutive invalid attempts. Come back again later!")
        break
    mainMenu.display_menu()
    try:  
        choice = int(input("Enter your choice (1-9):"))
        print()
        if 1 <= choice <= 9:
            mainMenu.select_menu(choice)
            if choice == 9:
                break
        else:
            raise ValueError()
    except ValueError:
        attempts += 1
        print("Something wrong! You need to give a number between 1-9\n")
