name = input("Enter name: ")
MENU_STRING = "(H)ello\n(G)oodbye\n(Q)uit"
print(MENU_STRING)
choice = input("Enter your choice : ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello!", name)
    elif choice == "G":
        print("Goodbye!", name)
    else:
        print("Invalid")
    print(MENU_STRING)
    choice = input("Enter your choice : ").upper()
print("Program finished")
print()