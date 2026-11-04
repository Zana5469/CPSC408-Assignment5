from rideshareops import db_operations
db_ops = db_operations()
db_ops.create_rideshare_tables()

def StartScreen():
    print("Welcome to the RideShare App")
    print("Do you have an account? (y/n)")

    account_choice = input("Enter your choice: ").lower()

    if account_choice.lower() not in ["y", "n"]:
        print("Invalid choice. Please enter 'y' or 'n'.")
        return
    elif account_choice in ["n", "no"]:
        CreateAccount()
    else:
        Login()

def CreateAccount():
    print("\n=== Create an Account ===")

    username = input("Enter a username: ")
    password = input("Enter a password: ")

    query = '''
    INSERT INTO Users (username, password)
    VALUES (%(username)s, %(password)s)
    '''

    db_ops.modify_query_params(query, {
        "username": username,
        "password": password
    })

    print("Account successfully created!")
    Login()

def Login():
    print("\n=== User Login ===")

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    query = '''
    SELECT * FROM Users 
    WHERE username = %(username)s 
    AND password = %(password)s
    '''

    user = db_ops.select_query_params(query, {
        "username": username,
        "password": password
    })

    if not user:
        print("Invalid username or password. Please try again.")
        return

    print(f"\nWelcome back, {username}!")

    print("Are you a driver or a rider?")
    if input("Enter 'driver' or 'rider': ").lower() == "driver":
        Driver()
    else:
        Rider()

def Driver():
    print("Driver Menu")
    print("\n1. View Rating")
    print("\n2. View Rides")  
    print("\n3. Update Mode")
    driver_choice = input("Enter your choice: ")

    if driver_choice == "1":
        driver_id = input("Enter your driver ID: ")
        query = '''SELECT DriverRating FROM Driver WHERE DriverID = %(driver_id)s'''
        DriverRating = db_ops.single_record_params(query, {"driver_id": driver_id})
        print(f"Your rating is: {DriverRating}")

    elif driver_choice == "2":
        driver_id = input("Enter your driver ID: ")
        query = "SELECT * FROM Rides WHERE driver_id = %s"
        rides = db_ops.select_query_params(query, {"driver_id": driver_id})
        for ride in rides:
            print(ride)

    elif driver_choice == "3":
        driver_id = input("Enter your driver ID: ")
        new_mode = input("Enter new mode (0 for inactive, 1 for active): ")
        query = "UPDATE Drivers SET mode = %s WHERE driver_id = %s"
        db_ops.cursor.execute(query, (new_mode, driver_id))
        db_ops.connection.commit()
        print("Mode updated successfully.")

def Rider():
    print ("Rider Menu")
    print("\n1. View Rides")
    print("\n2. Find a Driver")

    if input("Enter your choice: ") == "1":
        rider_id = input("Enter your rider ID: ")
        query = "SELECT * FROM Rides WHERE rider_id = %s"
        rides = db_ops.select_query_params(query, {"rider_id": rider_id})
        for ride in rides:
            print(ride)
    else:
        Find_Driver()


def Find_Driver():
    origin = input("Enter Your Pick Up Location: ")
    destination = input("Enter Your Drop Off Location: ")
    ride = {
        "origin": origin,
        "destination": destination
    }  
    
    query = '''
    INSERT INTO Rides (origin, destination)
    VALUES (%(origin)s, %(destination)s)
    '''
    db_ops.modify_query_params(query, ride)


def Rate_Driver():

StartScreen()

while True:
    if 