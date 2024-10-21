"""
Emails
Estimate: 25 minutes
Actual: 19 minutes
"""


def main():
    """Confirm a users email and name and display it side by side"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is this your name: {name}? (Y/N) ").upper()
        if confirmation != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Get name from email prefix"""
    prefix = email.split("@")[0]
    parts = prefix.split(".")
    name = " ".join(parts).title()
    return name


main()
