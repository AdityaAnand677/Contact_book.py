# Contact Book Application

contacts = []

while True:

    print("\n------ CONTACT BOOK MENU ------")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == '1':
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        contacts.append(contact)
        print("Contact added successfully!")

    # View Contacts
    elif choice == '2':
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for i, c in enumerate(contacts):
                print(f"{i+1}. {c['name']} - {c['phone']}")

    # Search Contact
    elif choice == '3':
        search = input("Enter name or phone to search: ")
        found = False

        for c in contacts:
            if search.lower() in c['name'].lower() or search in c['phone']:
                print("\nContact Found")
                print("Name:", c['name'])
                print("Phone:", c['phone'])
                print("Email:", c['email'])
                print("Address:", c['address'])
                found = True

        if not found:
            print("Contact not found")

    # Update Contact
    elif choice == '4':
        name = input("Enter contact name to update: ")

        for c in contacts:
            if c['name'].lower() == name.lower():
                c['phone'] = input("Enter new phone: ")
                c['email'] = input("Enter new email: ")
                c['address'] = input("Enter new address: ")
                print("Contact updated successfully!")
                break
        else:
            print("Contact not found")

    # Delete Contact
    elif choice == '5':
        name = input("Enter contact name to delete: ")

        for c in contacts:
            if c['name'].lower() == name.lower():
                contacts.remove(c)
                print("Contact deleted successfully!")
                break
        else:
            print("Contact not found")

    # Exit
    elif choice == '6':
        print("Closing Contact Book")
        break

    else:
        print("Invalid choice")
