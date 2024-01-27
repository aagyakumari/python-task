def user_add(pwfile):
    import getpass  
    import codecs  
     

    def add_user(username, real_name, password):
        with open(pwfile, "a") as file:
            file.write(f"{username}:{real_name}:{password}\n")
            
        with open(pwfile, "r+") as file:
        
            lines = file.readlines()
            existing_username_list = []
            for line in lines:
                data = line.strip().split(':')
                existing_username,real_name,_= data
                existing_username_list.append(existing_username)
            existing_username_set = set(existing_username_list)
            if len(lines) == len(existing_username_set):
                print("\nUser Created. \n")
            else:
                lines.pop()
                print("\nThis Username already exists\n")  
            file.seek(0)
            file.writelines(lines)
            file.truncate()
                
    # ask user for input until they provide it.
    while True:
        username = input("\nEnter new username: ")
        if username:
            break
    while True:    
        real_name = input("\nEnter real name: ")
        if real_name:
            break
    while True:
        password = getpass.getpass("\nEnter password: ")  
        password = codecs.encode(password, "rot_13")
        if password:
            break
               
    add_user(username, real_name, password)
            
                
        
    