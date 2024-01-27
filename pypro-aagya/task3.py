import sys
import aduser
import deluser
import changepw2
import login
try:
    if len(sys.argv) > 2:
       print("Can only send one file at a time!")
    elif len(sys.argv) < 2:
         print("Missing command line argument!")
    else:
        text_file = sys.argv[1]

        while True:
            what_do = None #for avoiding unnecessary memory usage
            print("what do you want to do?")
            what_do = input("1. create account\n2. delete account\n3. change password\n4. log in\n\n-> ")
            
            # calling the modules
            if what_do == '1':
                aduser.user_add(text_file)
            elif what_do == '2':
                deluser.user_delete(text_file)
            elif what_do == '3':
                changepw2.pw_change(text_file)
            elif what_do == '4':
                login.access_user(text_file)
            elif what_do == '':
                continue
            else:
                print(f"{what_do} is not a valid option!")
            
            more = input("\ndo you want to continue?  (yes/no) -> ")
            if more.lower() != 'yes' and more.lower() != 'y':
                print("exiting...")
                break
                
except FileNotFoundError:
        print(f'Cannot open {sys.argv[1]}!')
