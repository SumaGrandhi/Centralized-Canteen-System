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
