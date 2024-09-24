import os
import time
from colorama import Fore, Style, init

init(autoreset=True)


names = []
numbers = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    
    print(f'''{Fore.CYAN}
          1. Add New Contact
          2. Update Contact
          3. Search Contact
          4. Delete Contact
          5. View All Contacts
          6. Exit''')

def add_contact():
    
    name = input(Fore.CYAN + "Enter contact name: ")
    number = input(Fore.CYAN + "Enter contact number: ")
    names.append(name)
    numbers.append(number)
    clear_screen()
    print(Fore.GREEN + "Contact saved successfully!")

def update_contact():
    
    print(f'''{Fore.YELLOW}
        1. Update Name
        2. Update Number''')
    choice = int(input(Fore.CYAN + "Enter your choice: "))
    
    if choice == 1:
        old_name = input(Fore.CYAN + "Enter the name to update: ")
        if old_name in names:
            new_name = input(Fore.CYAN + "Enter new name: ")
            names[names.index(old_name)] = new_name
            clear_screen()
            print(Fore.GREEN + "Name updated successfully!")
        else:
            print(Fore.RED + "Name not found!")
    elif choice == 2:
        old_number = input(Fore.CYAN + "Enter the number to update: ")
        if old_number in numbers:
            new_number = input(Fore.CYAN + "Enter new number: ")
            numbers[numbers.index(old_number)] = new_number
            clear_screen()
            print(Fore.GREEN + "Number updated successfully!")
        else:
            print(Fore.RED + "Number not found!")
    else:
        print(Fore.RED + "Invalid choice!")

def search_contact():
    """Search for a contact by name"""
    search_name = input(Fore.CYAN + "Enter the name to search: ")
    if search_name in names:
        print(Fore.GREEN + "Contact found!")
        print(f"{Fore.YELLOW}Name: {Fore.GREEN}{search_name}")
        print(f"{Fore.YELLOW}Number: {Fore.GREEN}{numbers[names.index(search_name)]}")
    else:
        print(Fore.RED + "Contact not found!")

def delete_contact():
    """Delete a contact by name or number"""
    print(f'''{Fore.YELLOW}
             1. Delete by Name
             2. Delete by Number''')
    
    choice = int(input(Fore.CYAN + "Enter your choice: "))
    
    if choice == 1:
        delete_name = input(Fore.CYAN + "Enter the name to delete: ")
        if delete_name in names:
            index = names.index(delete_name)
            del names[index]
            del numbers[index]
            clear_screen()
            print(Fore.GREEN + "Contact deleted successfully!")
        else:
            print(Fore.RED + "Name not found!")
    
    elif choice == 2:
        delete_number = input(Fore.CYAN + "Enter the number to delete: ")
        if delete_number in numbers:
            index = numbers.index(delete_number)
            del names[index]
            del numbers[index]
            clear_screen()
            print(Fore.GREEN + "Contact deleted successfully!")
        else:
            print(Fore.RED + "Number not found!")
    else:
        print(Fore.RED + "Invalid choice!")

def view_all_contacts():
    """Display all contacts in the list"""
    if not names and not numbers:
        print(Fore.RED + "Contact list is empty!")
    else:
        clear_screen()
        print(Fore.CYAN + "Contact List:")
        for name, number in zip(names, numbers):
            print(f"{Fore.YELLOW}{name} -- {Fore.GREEN}{number}")
            time.sleep(1)  

def main():
    """Main program loop to display the menu and handle user input"""
    while True:
        display_menu()
        choice = int(input(Fore.CYAN + "Enter your choice: "))
        
        if choice == 1:
            clear_screen()
            add_contact()
        elif choice == 2:
            clear_screen()
            update_contact()
        elif choice == 3:
            clear_screen()
            search_contact()
        elif choice == 4:
            clear_screen()
            delete_contact()
        elif choice == 5:
            clear_screen()
            view_all_contacts()
        elif choice == 6:
            clear_screen() 
            print(Fore.CYAN + "Exiting program. Goodbye!")
            break
        else:
            clear_screen()
            print(Fore.RED + "Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
