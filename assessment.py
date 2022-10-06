'''
Well, this took me way longer than it should have. I couldn't get the nested dictionaries working the way I wanted to so I ended up
redoing everything and creating this crazy thing relying on a conditional right after the string split. I hope this is okay!!
'''
user_info = {}
infile = open("data.txt", "r").readlines()
# -------------------------------------------------
def load_file(username_input, password_input):
    '''
    Opens and reads data.txt then splits string into substrings. After each split, it'll check if the user input
    is equal to the username and password in that loop.
    '''
    for line in infile:
        split_list = line.rstrip().split(",")
        if username_input == split_list[0] and password_input == split_list[1]:
            user_info['username'] = split_list[0]
            user_info['password'] = split_list[1]
            user_info['name'] = split_list[2]
            user_info['balance']= split_list[3]
            return
        else:
            print("\nUsername and password not found, please try again\n")
            quit()
    
# -------------------------------------------------
def user_information():
    '''
    Fetches and displays user information
    '''
    print(f"Name: {user_info['name']}")
    print(f"Balance: {user_info['balance']}")

# -------------------------------------------------
def login():
    '''
    Main loop that also gets user input
    '''
    username_input = input("Enter Username: ")
    password_input = input("Enter Password: ")  
    load_file(username_input, password_input)
    user_information()

# -------------------------------------------------
login()
infile.close()
