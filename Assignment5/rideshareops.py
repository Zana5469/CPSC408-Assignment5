
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

    # Return a single attribute for all records
    def single_attribute(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return [i[0] for i in results if i[0] is not None]

    # Return a single attribute for all records with parameters
    def single_attribute_params(self, query, dictionary):
        self.cursor.execute(query, dictionary)
        results = self.cursor.fetchall()
        return [i[0] for i in results if i[0] is not None]

    # Bulk insert multiple records
    def bulk_insert(self, query, data):
        self.cursor.executemany(query, data)
        self.connection.commit()

    # Create Driver, Rider, and Ride tables
    def create_rideshare_tables(self):

        create_driver_table = '''
        CREATE TABLE IF NOT EXISTS Driver (
            DriverID VARCHAR(20) NOT NULL PRIMARY KEY,
            DriverRating FLOAT NOT NULL,
            username VARCHAR(20) NOT NULL,
            password VARCHAR(30) NOT NULL,
            mode TINYINT(1) NOT NULL
        );
        '''

        create_rider_table = '''
        CREATE TABLE IF NOT EXISTS Rider (
            RiderID VARCHAR(20) NOT NULL PRIMARY KEY,
            username VARCHAR(20) NOT NULL,
            password VARCHAR(30) NOT NULL
        );
        '''

        create_ride_table = '''
        CREATE TABLE IF NOT EXISTS Ride (
            RideID VARCHAR(20) NOT NULL PRIMARY KEY,
            DriverID VARCHAR(20) NOT NULL,
            RiderID VARCHAR(20) NOT NULL,
            Rating FLOAT NOT NULL,
            ORIGIN VARCHAR(50) NOT NULL,
            DESTINATION VARCHAR(50) NOT NULL,

            FOREIGN KEY (DriverID) REFERENCES Driver(DriverID),
            FOREIGN KEY (RiderID) REFERENCES Rider(RiderID)
        );
        '''

        self.modify_query(create_driver_table)
        self.modify_query(create_rider_table)
        self.modify_query(create_ride_table)

        print("Rideshare tables created successfully!")

    # Check whether Driver table is empty
    def is_driver_empty(self):
        query = "SELECT COUNT(*) FROM Driver;"
        return self.single_record(query) == 0

    # Check whether Rider table is empty
    def is_rider_empty(self):
        query = "SELECT COUNT(*) FROM Rider;"
        return self.single_record(query) == 0

    # Check whether Ride table is empty
    def is_ride_empty(self):
        query = "SELECT COUNT(*) FROM Ride;"
        return self.single_record(query) == 0

    # Close MySQL connection
    def destructor(self):
        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()

        print("MySQL connection closed.")
