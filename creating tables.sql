use centralised_canteen_system;
drop table if exists Employee;
drop table if exists Items;
drop table if exists Orders;
drop table if exists Customer;
drop table if exists Vendor;
drop table if exists Feedback;
-- Create tables
CREATE TABLE Employee (
  EmployeeID INT PRIMARY KEY,
  Name VARCHAR(255),
  Gender VARCHAR(50),
  Phone_Number VARCHAR(50),
  Address VARCHAR(255),
  Designation VARCHAR(255),
  Date_of_Birth DATE
);

CREATE TABLE Customer (
  CustomerID INT PRIMARY KEY,
  Name VARCHAR(255),
  Phone_Number VARCHAR(50),
  Address VARCHAR(255),
  Date_of_Birth DATE,
  Gender VARCHAR(50)
);

CREATE TABLE Vendor (
  VendorID INT PRIMARY KEY,
  Name VARCHAR(255),
  Address VARCHAR(255),
  Phone_Number VARCHAR(50),
  Store_Name VARCHAR(255)
);

CREATE TABLE Items (
  ItemID INT PRIMARY KEY,
  VendorID INT,
  Name VARCHAR(255),
  Price DECIMAL(10, 2),
  Quantity INT,
  Cooking_Time INT,
  FOREIGN KEY (VendorID) REFERENCES Vendor(VendorID)
);

CREATE TABLE Orders (
  OrderID INT PRIMARY KEY,
  CustomerID INT,
  ItemID INT,
  Cooking_Time INT,
  Price DECIMAL(10, 2),
  EmployeeID INT,
  FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
  FOREIGN KEY (ItemID) REFERENCES Items(ItemID),
  FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

CREATE TABLE Feedback (
  FeedbackID INT PRIMARY KEY,
  CustomerID INT,
  Comments TEXT,
  Quality_of_Service INT,
  Rating INT,
  OrderID INT,
  FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
  FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- Insert relationships and data here, if necessary.
INSERT INTO Employee (EmployeeID, Name, Gender, Phone_Number, Address, Designation, Date_of_Birth) VALUES 
(1, 'John Doe', 'Male', '123-456-7890', '123 Street, City', 'Chef', '1980-01-01'),
(2, 'Jane Smith', 'Female', '123-456-7891', '124 Street, City', 'Waiter', '1985-02-01'),
(3, 'Emily White', 'Female', '123-456-7892', '125 Street, City', 'Manager', '1975-05-15');

INSERT INTO Customer (CustomerID, Name, Phone_Number, Address, Date_of_Birth, Gender) VALUES 
(1, 'Alice Brown', '234-567-8901', '125 Street, City', '1990-03-01', 'Female'),
(2, 'Bob Johnson', '234-567-8902', '126 Street, City', '1992-04-01', 'Male'),
(3, 'Clara Adams', '234-567-8903', '127 Street, City', '1993-07-21', 'Female');

INSERT INTO Vendor (VendorID, Name, Address, Phone_Number, Store_Name) VALUES 
(1, 'Sarah Lee', '200 Market St, City', '345-678-9012', 'Sarah\'s Cafe'),
(2, 'Mike Davis', '201 Market St, City', '345-678-9013', 'Mike\'s Bakery'),
(3, 'Lucy Green', '202 Market St, City', '345-678-9014', 'Green Deli');


INSERT INTO Items (ItemID, VendorID, Name, Price, Quantity, Cooking_Time) VALUES 
(1, 1, 'Cappuccino', 3.50, 100, 5),
(2, 2, 'Croissant', 2.00, 50, 10),
(3, 3, 'Sandwich', 4.00, 40, 7),
(4, 1, 'Espresso', 2.50, 80, 3);


INSERT INTO Orders (OrderID, CustomerID, ItemID, Cooking_Time, Price, EmployeeID) VALUES 
(1, 1, 1, 5, 3.50, 1),
(2, 2, 2, 10, 2.00, 2),
(3, 1, 3, 7, 4.00, 1),
(4, 3, 4, 3, 2.50, 2);

INSERT INTO Feedback (FeedbackID, CustomerID, Comments, Quality_of_Service, Rating, OrderID) VALUES 
(1, 1, 'Great coffee!', 5, 4, 1),
(2, 2, 'Delicious croissant, but a bit too flaky.', 4, 3, 2),
(3, 3, 'The sandwich was okay.', 3, 3, 3);