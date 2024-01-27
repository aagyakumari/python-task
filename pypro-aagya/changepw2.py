def pw_change(pwfile):
    import getpass
    import codecs
        
    def change_password(username, current_password, new_password, password_file):
        '''function to change password'''
        
        with open(password_file, 'rt') as file:
            lines = file.readlines()
    
        with open(password_file, 'w') as file:
        
            for line in lines:
                data = line.strip().split(':')
                existing_username,real_name,existing_password = data #data unpacking
                if existing_username == username and existing_password == current_password:
                    file.write(f"{existing_username}:{real_name}:{new_password}\n")
                    print("Password changed.")
                else:
                    file.write(line)
                    
    # declaring variables
    password_file = pwfile
    username = input("User: ")
    current_password = getpass.getpass("Current Password: ")
    current_password = codecs.encode(current_password,"rot_13")
    new_password = getpass.getpass("new password:")
    new_password = codecs.encode(new_password, "rot_13")
    confirm_password = getpass.getpass("confirm password:")
    confirm_password = codecs.encode(confirm_password, "rot_13")
    
    # reading file and comparing passwords
    with open(pwfile, "rt") as file:
        lines = file.readlines()
        for line in lines:
            name = line.strip().split(':')[0]
            if name == username:
                current_password_1 = line.strip().split(':')[2]
                if current_password_1 == current_password:
                    if current_password != new_password:
                        if new_password == confirm_password:
                          change_password(username, current_password, new_password, password_file)
                        else:
                            print("Passwords do not match.")
                    else: 
                        print("you cannot use the existing password!")
                else:
                    print("wrong password! can't allow to change password!")
                
        

            
