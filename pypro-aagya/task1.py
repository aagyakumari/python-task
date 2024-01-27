def pos_int(num):
    '''function to take a positive integer'''
    while True:
        try:
            value = int(input(num))
            if value > 0:
                return value
            elif value == 0:
                print("You cannot order nothing!")
            elif value < 0:
                print("Please, enter the positive integer!")
        except:
            print("Please enter a valid value!")

def user_input(inp):
    while True:
        response = input(inp).lower()
        if response == 'y' or response == 'yes':
            return 'y'
        elif response == 'n' or response == 'no':
            return 'n'
        else:
            print('Please answer "Y" or "N"!')

def display_menu():
    print("Menu:")
    print("1. Margherita pizza - £12")
    print("2. Greek pizza - £12")
    print("3. Pepperoni pizza - £12")
    print("4. Roman Pizaa - £12")
    print("5. Sicilian  - £12")

def get_pizza_choice():
    
    while True:
        try:
            choice = int(input("Enter the number of the pizza you want: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please enter a valid pizza number (1-5)!")
        except ValueError:
            print("Please enter a valid integer value!")

def calculate_cost(total_orders, requires_delivery, is_tuesday, used_app):
    # Constants given in the question
    pizza_price = 12
    if num_pizzas < 5 and requires_delivery == 'y':
        delivery_cost = 2.50
    else:
        delivery_cost = 0

    if is_tuesday == 'y':
        tuesday_discount = 0.5
    else:
        tuesday_discount = 0

    if used_app == 'y':
        app_discount = 0.25
    else:
        app_discount = 0

    total_cost = total_orders * pizza_price + delivery_cost

    # Applying required discounts
    
    discounted_tues = total_cost*(1-tuesday_discount)
    discounted_app = discounted_tues*(1-app_discount)
    final_cost = discounted_app
    final_tues = total_cost - discounted_tues
    final_app = discounted_tues - discounted_app
    
    
    return total_cost, final_cost, delivery_cost, tuesday_discount, app_discount, final_tues, final_app

def generate_bill(requires_delivery, total_cost, final_cost, delivery_cost, final_tues, final_app,orders_list, pizza_choice_list):
    '''function to generate a bill'''
    pizza_price = 12
    print("\n----------------- BPP Pizza Bill ---------------------\n")
    if requires_delivery == 'y':
        print(f"Delivery Cost £{delivery_cost:.2f} added\n")
    for i in range(len(orders_list)):
        print(f"{pizza_choice_list[i]} ({orders_list[i]}):  {('+ £'+ str(orders_list[i]*pizza_price)):>{30 - len(pizza_choice_list[i]) - len(str(orders_list[i]))}} ")
    
    print(f"Base Cost:                       £{total_cost:.2f}\n")
    print(f"Tuesday Discount:              - £{final_tues}\n")
    print(f"App Discount:                  - £{final_app}\n")
    print("----------------------------------------------------------")
    print("----------------------------------------------------------")
    print(f"Total Price:                     £{final_cost:.2f}.")
        
    

       
# Main program
print("BPP Pizza Price Calculator")
print("GET UPTO 50% DISCOUNT ON TUESDAY'S!!!!\n")

# Display menu and get user's pizza choice
orders_list = []
pizza_choice_list = []
while True:
    display_menu()
    pizza_choice = get_pizza_choice()
    num_pizzas = pos_int("How many pizzas of this type would you like to order? ")
    orders_list.append(num_pizzas)
     # Get the name of the selected pizza
    pizza_menu_names = ["Margherita pizza","Greek pizza","Pepperoni pizza", "Roman pizza", "Sicilian pizza"]
    pizza_name = pizza_menu_names[pizza_choice - 1]
    pizza_choice_list.append(pizza_name)
    more = user_input("Do you want to order anything else? (Y/N)")
    if more == 'y':
        continue
    
    

    requires_delivery = user_input("Is delivery required? (Y/N) ")
    is_tuesday = user_input("Is it Tuesday? (Y/N) ")
    used_app = user_input("Did the customer use the app? (Y/N) ")
    
    break


total_orders = sum(orders_list) 
   
# Calculate costs
total_cost, final_cost, delivery_cost, tuesday_discount, app_discount, final_tues, final_app = calculate_cost(total_orders, requires_delivery, is_tuesday, used_app)
# Display the bill
generate_bill(requires_delivery, total_cost, final_cost, delivery_cost, final_tues, final_app, orders_list, pizza_choice_list)
   
        
    

    
    
        
