users_name = input("Enter name: ")
print("(H)ello\n(G)oodbye\n(Q)uit")
users_choice = input(">>> ").upper()
while users_choice != "Q":
    if users_choice == "H":
        print(f"Hello {users_name}")
    elif users_choice == "G":
        print(f"Goodbye {users_name}")
    else:
        print("Invalid choice")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    users_choice = input(">>> ").upper()
print("Finished.")
