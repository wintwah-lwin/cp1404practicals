"""emails.py
Estimate: 20 minutes
Time taken: 23 minutes"""

def main():
    email_to_name = {}
    email = input("Email(Press enter to stop): ")
    while email != "":
        email_name = get_name_from_email(email)

        confirm = input(f"Is your name {email_name}? (Y/n) ").lower()
        if confirm in ('', 'y', 'yes'):
            name = email_name
        else:
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email(Press enter to stop): ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")



def get_name_from_email(email):
    name = email.split("@")[0]
    name_parts = name.split(".")
    full_name = " ".join(name_parts).title()
    return full_name

main()