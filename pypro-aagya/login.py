def access_user(pwfile):   
    import getpass  
    import codecs   

    # Function for login
    def login(username, password, password_file):
        with open(password_file, 'rt') as file:
            for line in file:
                existing_username, _, existing_password = line.strip().split(':')
                
                # Checking if username and password match
                if existing_username == username and existing_password == password:
                    print("Access granted.\n")
                    return  
        print("Access denied.\n")

    password_file = pwfile
    username = input("User: ")
    password = getpass.getpass("Password: ") # hiding the password
    password = codecs.encode(password, "rot_13") # encryption method

    # Calling function
    login(username, password, password_file)


