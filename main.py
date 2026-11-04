def option_1():
    print("You selected Option 1.")

def option_2():
    print("You selected Option 2.")

def option_3():
    print("You selected Option 3.")

def option_4():
    print("You selected Option 4.")

def option_5():
    print("You selected Option 5.")

def option_6():
    print("You selected Option 6.")

def option_7():
    print("You selected Option 7.")

def option_8():
    print("You selected Option 8.")

def option_9():
    print("You selected Option 9.")

def option_10():
    print("You selected Option 10.")

def main_menu():
    print("========== TOURNAMENT MANAGER ==========")
    print("1. Add team")
    print("2. Show all teams")
    print("3. Add match result")
    print("4. Show standings")
    print("5. Show leading team")
    print("6. Show best attacking team")
    print("7. Show team success rate")
    print("8. Show teams without wins")
    print("9. Show tournament summary")
    print("10. Check championship potential")
    print("0. Exit")
    print("Choose an option: ")

    while True:
        choice = input("\nEnter your choice (0-10): ")

        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            option_3()
        elif choice == "4":
            option_4()
        elif choice == "5":
            option_5()
        elif choice == "6":
            option_6()
        elif choice == "7":
            option_7()
        elif choice == "8":
            option_8()
        elif choice == "9":
            option_9()
        elif choice == "10":
            option_10()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()