import json

FILE_NAME = "contacts.json"

# Load contacts from file
try:
    with open(FILE_NAME, "r") as file:
        contacts = json.load(file)
except:
    contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Save Contacts")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        contacts[name] = {
            "Phone": phone,
            "Email": email
        }

        print("Contact Added Successfully!")

    elif choice == "2":
        if contacts:
            print("\n--- Contact List ---")
            for name, details in contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {details['Phone']}")
                print(f"Email: {details['Email']}")
        else:
            print("No Contacts Found!")

    elif choice == "3":
        name = input("Enter Name to Search: ")

        if name in contacts:
            print("\nContact Found:")
            print(f"Phone: {contacts[name]['Phone']}")
            print(f"Email: {contacts[name]['Email']}")
        else:
            print("Contact Not Found!")

    elif choice == "4":
        name = input("Enter Name to Update: ")

        if name in contacts:
            new_phone = input("Enter New Phone Number: ")
            new_email = input("Enter New Email: ")

            contacts[name]["Phone"] = new_phone
            contacts[name]["Email"] = new_email

            print("Contact Updated Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "5":
        name = input("Enter Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "6":
        with open(FILE_NAME, "w") as file:
            json.dump(contacts, file, indent=4)

        print("Contacts Saved Successfully!")

    elif choice == "7":
        with open(FILE_NAME, "w") as file:
            json.dump(contacts, file, indent=4)

        print("Contacts Saved. Exiting Program...")
        break

    else:
        print("Invalid Choice! Please Try Again.")