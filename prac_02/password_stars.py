password = input("Enter Password: ")
while len(password) < 5:
    print("Password is too short.")
    password = input("Enter Password: ")
for i in range(1, len(password) + 1):
    print("*", end="")
print()
