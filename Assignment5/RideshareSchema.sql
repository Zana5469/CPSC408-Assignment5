DROP DATABASE IF EXISTS Rideshare;
CREATE DATABASE Rideshare;
USE Rideshare;

CREATE TABLE Driver (
    DriverID INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    mode TINYINT(1) NOT NULL DEFAULT 0
);

CREATE TABLE Rider (
    RiderID INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE Ride (
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

-- Sample Data
INSERT INTO Driver (username, password, mode) VALUES
                                                  ('bossbaby', 'people', 1),
                                                  ('party2000', 'livinlife', 0),
                                                  ('hanginaround', 'dawg', 1);


INSERT INTO Rider (username, password) VALUES
                                           ('rapunzel', 'frying_pan'),
                                           ('moana', 'boat_snack'),
                                           ('pocahontas', 'colors');

INSERT INTO Ride (DriverID, RiderID, Rating, Origin, Destination) VALUES
                                                                                (1, 1, 5.0, 'San Clemente', 'Irvine'),
                                                                                (2, 2, 4.8, 'Orange', 'SC'),
                                                                                (1, 2, 4.6, 'Fallbrook', 'Temecula'),
                                                                                (3, 3, NULL, 'California', 'Texas');