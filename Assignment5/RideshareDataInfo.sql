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