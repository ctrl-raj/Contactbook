


#Contact Book CLI Source Code
print("-----Contact Book-----")
user = input("Username: ")
print(f"--- Welcome {user.title()} ----")
try:
    while True:
        print("""
        -- Functions Codes --
        1 -> Add a new contact
        2 -> Review all contacts
        3 -> Search contacts
        4 -> Edit a contact
        5 -> Delete a contact
        x -> Exit program
        """)
        function_cmd = input("Function Code Number: ")


        if function_cmd == "1":
            with open("ContactBook-Database.txt", "a") as f:
                contact_input = input(f"Intput Name and Phone Number: ")
                identity = contact_input.split(" ")
                f.write(f"""
{identity[0].title()} - {identity[1]}""")
                print(f"{identity[0].title()} was saved in contacts")
            pass

        elif function_cmd == "2":
            with open("ContactBook-Database.txt", "r") as f:
                print("All Contacts")
                print(f.read())
            pass

        elif function_cmd == "3":
            search_word = input("Search by either Name or Phone Number: ")
            with open("ContactBook-Database.txt", "r") as f:
                lines = f.readlines()

                for line in lines:
                    words = line.strip().split()
                    if search_word.title() in words:
                        print(f"""
        Here's you search result based on '{search_word.title()}'
        {line.strip()}
        """)
            pass
        elif function_cmd == "4":
            search_word = input("Search by either name or phone of contact: ")
            with open("ContactBook-Database.txt", "r") as f:
                lines = f.readlines()
                update_lines = []
                edited = False
                for line in lines:
                    if search_word.title() in line:
                        print(f"Found : {line.strip().title()}")
                        new_entry = input("Enter new entry like, ('name' 'phone'): ")
                        identity = new_entry.split(" ")
                        update_lines.append(f"{identity[0].title()} - {identity[1]}")
                        edited = True
                    else:
                        update_lines.append(line)
                with open("ContactBook-Database.txt", "w") as f:
                    f.writelines(update_lines)
                if edited:
                    print("Contact has been successfully edited")
                else:
                    print("Sorry, the contact was not edited")
            pass
        elif function_cmd == "5":
            search_word = input("Search by either Name or Phone Number: ")
            with open("ContactBook-Database.txt", "r") as f:
                lines = f.readlines()

                for line in lines:
                    words = line.split()
                    if search_word.title() in words:
                        print(f"""
                                    Here's you search result based on '{search_word.title()}'
                                {line.strip()}
                                    """)

                        delete_request = input("Enter name and phone to delete: ")
                        with open("ContactBook-Database.txt", "r") as f:
                            lines = f.readlines()

                            update_lines = []  # list
                            for line in lines:  # line is a data in the list, lines
                                if delete_request.title() not in line:
                                    update_lines.append(line)
                            with open("ContactBook-Database.txt", "w") as f:
                                f.writelines(update_lines)
                                print(f"{delete_request} was removed from the contacts")
                    else:
                        print(f"{search_word.title()} was not found...")
            pass
        elif function_cmd == "x":
            break
        else:
            print("Please Enter a valid Function Code")
            pass
except ValueError:
    print("Please enter a Valid Function Code")