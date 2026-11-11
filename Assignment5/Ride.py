from rideshareops import db_operations
from rs_helper import helper

db_ops = db_operations()
db_ops.create_rideshare_tables()


#Start Screen function to display the main menu and handle user input
def StartScreen():

    while True:
        print("\nWelcome to the RideShare App")
        print("1. Create an Account")
        print("2. Login")
        print("3. Exit")

        choice = helper.get_choice([1, 2, 3])

        if choice == 1:
            CreateAccount()

        elif choice == 2:
            Login()

        elif choice == 3:
            print("Thank you for using RideShare!")
            exit()

#Function to create a new account for either a driver or a rider
def CreateAccount():

    print("1. Driver")
    print("2. Rider")

    account_type = helper.get_choice([1, 2])

    username = input("Create a username: ").strip()
    password = input("Create a password: ").strip()

    # Validate username and password and ensure they are not empty nor are already taken
    if not username or not password:
        print("Username and password cannot be empty.")
        return

    try:
        #driver account creation
        if account_type == 1:

            driver_id = db_ops.create_driver(username, password)

            print("\nDriver account successfully created!")
            print(f"Your Driver ID is: {driver_id}")

        #rider account creation
        elif account_type == 2:

            rider_id = db_ops.create_rider(username, password)

            print("\nRider account successfully created!")
            print(f"Your Rider ID is: {rider_id}")

        print("\nPlease log in to your new account.")
        Login()

    #throw an exception if the account creation fails, likely due to a duplicate username. This should not print! 
    except Exception as e:

        print("Unable to create account.")
        print("The username may already exist.")

#Function to handle user login for either a driver or a rider with an already existing account. 
def Login():

    print("\nLogin to Your Account:")
    print("1. Driver")
    print("2. Rider")

    account_type = helper.get_choice([1, 2])

    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    # Ensures that username and password are not empty. 
    if not username or not password:
        print("Username and password cannot be empty.")
        return

    try:

        # Driver Login
        if account_type == 1:
            user = db_ops.get_driver_login(username, password) # checks if the driver exists in the database
            if user:                                            # if the driver exists, it retrieves the driver ID and welcomes the user back
                driver_id = user[0][0] 
                print(f"\nWelcome back, {username}!")
                Driver(driver_id)
            else:
                print("Invalid username or password.")

        # Rider Login
        elif account_type == 2:
            user = db_ops.get_rider_login(username, password)   #if the rider exists, it retrieves the rider ID and welcomes the user back
            if user:
                rider_id = user[0][0]
                print(f"\nWelcome back, {username}!")
                Rider(rider_id)
            else:
                print("Invalid username or password.")

    except Exception as e:
        print("Unable to log in.")                              #throws an exception if the login fails, likely due to incorrect credentials. 


#Function for options that will print when driver logs in. 
def Driver(driver_id):

    while True:

        print("\nWELCOME TO THE DRIVER MENU")
        print("1. View Rating")
        print("2. View Rides")
        print("3. Edit Driver Mode")
        print("4. Logout")

        driver_choice = helper.get_choice([1, 2, 3, 4])

        # View Rating
        if driver_choice == 1:

            rating = db_ops.get_driver_rating(driver_id)
            if rating is None:
                print("You do not have any ratings yet.") #error handlings for if the driver has not received any ratings yet.
            else:
                print(f"Your average rating is: {rating:.2f}/5")

        # View Rides
        elif driver_choice == 2:
            rides = db_ops.get_driver_rides(driver_id)
            if not rides:
                print("You have not completed any rides yet.")
            else:
                print("\nCOMPLETED RIDES:")

                for ride in rides:
                    print(f"\nRide ID: {ride[0]}")
                    print(f"Rider ID: {ride[1]}")
                    print(f"Pickup: {ride[2]}")
                    print(f"Destination: {ride[3]}")
                    print(f"Rating: {ride[4]}")
                    print(f"Date: {ride[5]}")
                    print("-----------------------------")

        # Edit Driver  Mode
        elif driver_choice == 3:

            print("\n1. Activate Driver Mode")
            print("2. Deactivate Driver Mode")

            mode_choice = helper.get_choice([1, 2])
            if mode_choice == 1:
                db_ops.update_driver_mode(driver_id, 1)
                print("Driver mode activated!")
            else:
                db_ops.update_driver_mode(driver_id, 0)
                print("Driver mode deactivated!")

        #Logout
        elif driver_choice == 4:
            print("Logging out...")
            return

#Function for options that will print when rider logs in.     
def Rider(rider_id):

    while True:

        print("\nRIDER MENU")
        print("1. View Rides")
        print("2. Find a Driver")
        print("3. Rate My Driver")
        print("4. Logout")

        rider_choice = helper.get_choice([1, 2, 3, 4])

        # View Rides
        if rider_choice == 1:
            rides = db_ops.get_rider_rides(rider_id)
            if not rides:
                print("You have not taken any rides yet.")
            else:
                print("\nCOMPLETED RIDES:")
                for ride in rides:

                    print(f"\nRide ID: {ride[0]}")
                    print(f"Driver ID: {ride[1]}")
                    print(f"Pickup: {ride[2]}")
                    print(f"Destination: {ride[3]}")
                    print(f"Rating: {ride[4]}")
                    print(f"Date: {ride[5]}")
                    print("-----------------------------")
        # Find a Driver
        elif rider_choice == 2:
            Find_Driver(rider_id)

        # Rate My Driver
        elif rider_choice == 3:
            Rate_Driver(rider_id)

        # Logout
        elif rider_choice == 4:
            print("Logging out...")
            return

#Function the rider can use to find a driver. 
def Find_Driver(rider_id):

    print("\nFIND A DRIVER")
    origin = input("Enter your pickup location: ").strip()
    destination = input("Enter your drop-off location: ").strip()

    # Validate locations
    if not origin or not destination:
        print("Pickup and drop-off locations cannot be empty.")
        return

    # Retrieve available drivers
    drivers = db_ops.get_active_drivers()
    if not drivers:
        print("\nSorry, there are no available drivers.")
        return

    print("\nLIST OF AVAILABLE DRIVERS:")

    # Display available drivers with selection numbers
    for i, driver in enumerate(drivers, start=1):
        print(f"{i}. Username: {driver[1]}")

    # Let rider select a driver
    choices = list(range(1, len(drivers) + 1))
    choice = helper.get_choice(choices)

    # Retrieve selected driver
    selected_driver = drivers[choice - 1]

    # Confirm driver selection
    print("\nRIDE CONFIRMATION DETAILS:")
    print(f"Driver: {selected_driver[1]}")
    print(f"Pickup: {origin}")
    print(f"Destination: {destination}")

     #input must be y/n to confirm the ride. If the input is not y/n, 
     #it will print "Ride request cancelled." and return to the previous menu.
    confirm = input("\nConfirm this ride? (y/n): ").strip().lower()

    if confirm != "y":
        print("Ride request cancelled.")
        return

    # Create ride
    try:
        ride_id = db_ops.create_ride(
            selected_driver[0],
            rider_id,
            origin,
            destination
        )
        print("\nRIDE CONFIRMED!")
        print(f"Ride ID: {ride_id}")
        print(f"Driver: {selected_driver[1]}")
        print("Your ride has been successfully created!")

    except Exception as e:
        print("Unable to create ride.")


#Function for the rider to rate their driver after a ride.
def Rate_Driver(rider_id):
    print("\nDRIVER RATING")

    # Retrieve the rider's most recent ride
    rides = db_ops.get_recent_ride(rider_id)

    if not rides:
        print("You do not have any rides to rate.")
        return
    ride = rides[0]

    # Display most recent ride
    print("\nYour most recent ride:")
    print(f"Ride ID: {ride[0]}")
    print(f"Driver ID: {ride[1]}")
    print(f"Pickup: {ride[3]}")
    print(f"Destination: {ride[4]}")
    print(f"Date: {ride[6]}")

    confirmation = input(
        "\nIs this the ride you want to rate? (y/n): "
    ).strip().lower()

    # If rider wants to rate a different ride
    if confirmation == "n":
        ride_id = input("Enter the Ride ID you want to rate: ").strip()
        if not ride_id.isdigit():
            print("Invalid Ride ID.")
            return
        selected_rides = db_ops.get_ride_by_id(
            int(ride_id),
            rider_id
        )
        if not selected_rides:

            print("Ride not found or it does not belong to you.")
            return

        ride = selected_rides[0]

        # Display selected ride
        print("\nSELECTED RIDE DETAILS:")
        print(f"Ride ID: {ride[0]}")
        print(f"Driver ID: {ride[1]}")
        print(f"Pickup: {ride[3]}")
        print(f"Destination: {ride[4]}")
        print(f"Date: {ride[6]}")

        confirmation = input(
            "\nIs this the correct ride? (y/n): "
        ).strip().lower()

        if confirmation != "y":
            print("Rating cancelled.")
            return

    elif confirmation != "y":

        print("Invalid choice. Rating cancelled.")
        return

    # Check if ride has already been rated
    if ride[5] is not None:
        print("You have already rated this ride.")
        return

    # Collect rating
    rating = input("\nEnter your rating (1-5): ")

    while not rating.isdigit() or int(rating) < 1 or int(rating) > 5:
        print("Please enter a rating between 1 and 5.")
        rating = input("Enter your rating (1-5): ")

    # Store rating in database
    result = db_ops.rate_ride(
        ride[0],
        rider_id,
        int(rating)
    )

    if result:
        print("Thank you! Your rating has been submitted!")

    else:
        print("Unable to submit rating.")

StartScreen()
db_ops.destructor()