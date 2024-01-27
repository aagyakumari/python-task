def user_delete(pwfile):

     
    def delete_user(username, password_file=pwfile):
        '''function to delete the user account'''
        with open(password_file, 'rt') as file:
            lines = file.readlines()

        # Flag to track if the user is found and deleted
        found = False

        with open(password_file, 'w') as file:
            for line in lines:
                existing_username = line.split(':')[0]
                if existing_username != username:
                    file.write(line)
                else:
                    found = True

        
        if found:
            print("User Deleted.")
        else:
            print("User not found.")


    password_file = pwfile
    username = input("Enter username: ")

    # Calling function
    delete_user(username, password_file)


