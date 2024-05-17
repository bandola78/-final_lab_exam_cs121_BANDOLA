from utils.dice_game import DiceGame
import datetime

def main_menu():
    print(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f"))
    print("Welcome to Dice Roll Game! \n")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice, or leave blank to cancel: ")
    game = DiceGame()

    if choice == '1':
        game.register()
    elif choice == '2':
        if game.login():
            game.menu()
    elif choice == '3':
        exit()
    elif choice == '':
        print("Operation canceled.\n")
    else:
        print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    while True:
        main_menu()