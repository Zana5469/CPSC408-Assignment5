import mysql.connector


class db_operations():

    # Constructor: Connect to MySQL database
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="CPSC408",
            database="Rideshare"
        )

        self.cursor = self.connection.cursor()
        print("MySQL connection made...")

    # Execute DDL or DML query without parameters
    def modify_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    # Execute DDL or DML query with parameters
    def modify_query_params(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        self.connection.commit()

    # Execute DQL query without parameters
    def select_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    # Execute DQL query with parameters
    def select_query_params(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        return self.cursor.fetchall()

    # Return first attribute of first record
    def single_record(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] if result else None

    # Return first attribute of first record with parameters
    def single_record_params(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        result = self.cursor.fetchone()
        return result[0] if result else None

    # Create Driver, Rider, and Ride tables
    def create_rideshare_tables(self):

        create_driver_table = '''
        CREATE TABLE IF NOT EXISTS Driver (
            DriverID INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(20) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            mode TINYINT(1) NOT NULL DEFAULT 0
        );
        '''

        create_rider_table = '''
        CREATE TABLE IF NOT EXISTS Rider (
            RiderID INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(20) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        );
        '''

        create_ride_table = '''
        CREATE TABLE IF NOT EXISTS Ride (
            RideID INT AUTO_INCREMENT PRIMARY KEY,
            DriverID INT NOT NULL,
            RiderID INT NOT NULL,
            Rating FLOAT NULL,
            Origin VARCHAR(100) NOT NULL,
            Destination VARCHAR(100) NOT NULL,
            RideDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (DriverID) REFERENCES Driver(DriverID),
            FOREIGN KEY (RiderID) REFERENCES Rider(RiderID)
        );
        '''

        self.modify_query(create_driver_table)
        self.modify_query(create_rider_table)
        self.modify_query(create_ride_table)

        print("Rideshare tables created successfully!")

    def create_driver(self, username, password):

        query = '''
        INSERT INTO Driver (username, password)
        VALUES (%(username)s, %(password)s)
        '''

        self.cursor.execute(query, {
            "username": username,
            "password": password
        })

        self.connection.commit()

        return self.cursor.lastrowid

    # Create a new rider account
    def create_rider(self, username, password):

        query = '''
        INSERT INTO Rider (username, password)
        VALUES (%(username)s, %(password)s)
        '''

        self.cursor.execute(query, {
            "username": username,
            "password": password
        })

        self.connection.commit()

        return self.cursor.lastrowid

    # Find a driver account during login
    def get_driver_login(self, username, password):

        query = '''
        SELECT DriverID, username
        FROM Driver
        WHERE username = %(username)s
        AND password = %(password)s
        '''

        return self.select_query_params(query, {
            "username": username,
            "password": password
        })

    # Find a rider account during login
    def get_rider_login(self, username, password):

        query = '''
        SELECT RiderID, username
        FROM Rider
        WHERE username = %(username)s
        AND password = %(password)s
        '''

        return self.select_query_params(query, {
            "username": username,
            "password": password
        })

    # Calculate the average rating of a driver
    def get_driver_rating(self, driver_id):

        query = '''
        SELECT AVG(Rating)
        FROM Ride
        WHERE DriverID = %(driver_id)s
        '''

        return self.single_record_params(query, {
            "driver_id": driver_id
        })

    # Retrieve all rides completed by a driver
    def get_driver_rides(self, driver_id):

        query = '''
        SELECT RideID, RiderID, Origin, Destination, Rating, RideDate
        FROM Ride
        WHERE DriverID = %(driver_id)s
        ORDER BY RideDate DESC
        '''

        return self.select_query_params(query, {
            "driver_id": driver_id
        })

    # Activate or deactivate driver mode
    def update_driver_mode(self, driver_id, new_mode):

        query = '''
        UPDATE Driver
        SET mode = %(mode)s
        WHERE DriverID = %(driver_id)s
        '''

        self.modify_query_params(query, {
            "mode": new_mode,
            "driver_id": driver_id
        })

    # Retrieve all rides taken by a rider
    def get_rider_rides(self, rider_id):

        query = '''
        SELECT RideID, DriverID, Origin, Destination, Rating, RideDate
        FROM Ride
        WHERE RiderID = %(rider_id)s
        ORDER BY RideDate DESC
        '''

        return self.select_query_params(query, {
            "rider_id": rider_id
        })

    # Find drivers who are currently accepting rides
    def get_active_drivers(self):

        query = '''
        SELECT DriverID, username
        FROM Driver
        WHERE mode = 1
        '''

        return self.select_query(query)

    # Create a new ride
    def create_ride(self, driver_id, rider_id, origin, destination):

        query = '''
        INSERT INTO Ride (DriverID, RiderID, Origin, Destination)
        VALUES (
            %(driver_id)s,
            %(rider_id)s,
            %(origin)s,
            %(destination)s
        )
        '''

        self.cursor.execute(query, {
            "driver_id": driver_id,
            "rider_id": rider_id,
            "origin": origin,
            "destination": destination
        })

        self.connection.commit()

        return self.cursor.lastrowid
   
    # Retrieve a rider's most recent ride
    def get_recent_ride(self, rider_id):

        query = '''
        SELECT RideID, DriverID, RiderID, Origin, Destination, Rating, RideDate
        FROM Ride
        WHERE RiderID = %(rider_id)s
        ORDER BY RideDate DESC, RideID DESC
        LIMIT 1
        '''

        return self.select_query_params(query, {
            "rider_id": rider_id
        })

    # Retrieve a specific ride belonging to a rider
    def get_ride_by_id(self, ride_id, rider_id):

        query = '''
        SELECT RideID, DriverID, RiderID, Origin, Destination, Rating, RideDate
        FROM Ride
        WHERE RideID = %(ride_id)s
        AND RiderID = %(rider_id)s
        '''

        return self.select_query_params(query, {
            "ride_id": ride_id,
            "rider_id": rider_id
        })

    # Store a rider's rating for a ride
    def rate_ride(self, ride_id, rider_id, rating):

        query = '''
        UPDATE Ride
        SET Rating = %(rating)s
        WHERE RideID = %(ride_id)s
        AND RiderID = %(rider_id)s
        AND Rating IS NULL
        '''

        self.modify_query_params(query, {
            "rating": rating,
            "ride_id": ride_id,
            "rider_id": rider_id
        })

        return self.cursor.rowcount

    # Close MySQL connection
    def destructor(self):

        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()

        print("MySQL connection closed.")

    # canary
