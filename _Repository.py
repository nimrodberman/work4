import atexit
import sqlite3
import os.path
from DAO import Employees, Suppliers , Products , Coffee_stands , Activities
from DTO import Employees_report ,ActivitiesTable




class _Repository:
    def __init__(self):
        self.isExist = os.path.isfile('moncafe.db')
        self._conn = sqlite3.connect('moncafe.db')
        self.Employees = Employees(self._conn)
        self.Suppliers = Suppliers(self._conn)
        self.Products = Products(self._conn)
        self.Coffee_stands = Coffee_stands(self._conn)
        self.Activities = Activities(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def print(self):
        cursor = self._conn.cursor()
        cursor.execute("SELECT * FROM Activities")
        print("Activities")
        for line in cursor.fetchall(): print(line)

        cursor.execute("SELECT * FROM Coffee_stands")
        print("Coffee_stands")
        for line in cursor.fetchall(): print(line)

        cursor.execute("SELECT * FROM Employees")
        print("Employees")
        for line in cursor.fetchall(): print(line)

        cursor.execute("SELECT * FROM Products")
        print("Products")
        for line in cursor.fetchall(): print(line)

        cursor.execute("SELECT * FROM Suppliers")
        print("Suppliers")
        for line in cursor.fetchall(): print(line)

        print()
        cursor.execute("""SELECT Employees.name, Employees.salary,
         Coffee_stands.location, coalesce(ABS(SUM(Products.price * Activities.quantity)),0)
            FROM Employees
            JOIN Coffee_stands ON Employees.coffee_stand = Coffee_stands.id
            LEFT JOIN Activities ON Employees.id = Activities.activator_id
            LEFT JOIN Products ON Activities.product_id = Products.id
            GROUP BY Employees.id ORDER BY Employees.name 
        """) # todo: check the name order !
        print("Employees Report") # todo: print it as needed!
        for line in cursor.fetchall():print(Employees_report(*line).toString())

        print()
        cursor.execute("""SELECT Activities.date, Products.description, Activities.quantity,
            Employees.name, Suppliers.name
            FROM Activities
            JOIN Products ON Activities.product_id = Products.id
            LEFT JOIN Employees ON Activities.activator_id = Employees.id
            LEFT JOIN Suppliers ON Activities.activator_id = Suppliers.id
            ORDER BY Activities.date
        """)
        print("Activities") # todo: print it as needed!
        for line in cursor.fetchall(): print(line)





    def create_tables(self):

        if self.isExist:
            self._conn.executescript("""DROP  TABLE Employees""")
            self._conn.executescript("""DROP  TABLE Suppliers""")
            self._conn.executescript("""DROP  TABLE Products""")
            self._conn.executescript("""DROP  TABLE Coffee_stands""")
            self._conn.executescript("""DROP  TABLE Activities""")


        self._conn.executescript(""" 
        CREATE TABLE Employees (
                id      INTEGER         PRIMARY KEY,
                name    TEXT        NOT NULL,
                salary    REAL        NOT NULL,
                coffee_stand INTEGER REFERENCES Coffee_stand(id)
            );
    
        CREATE TABLE Suppliers (
                id  INTEGER     PRIMARY KEY,
                name TEXT NOT NULL,
                contact_information TEXT
            );
    
        CREATE TABLE Products (
                id      INTEGER     PRIMARY KEY,
                description TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL    
            );
            
        CREATE TABLE Coffee_stands (
                id      INTEGER     PRIMARY KEY,
                location TEXT NOT NULL,
                number_of_employees INTEGER    
            );
        
        CREATE TABLE Activities (
                product_id     INTEGER INTEGER REFERENCES Product(id),
                quantity    INTEGER    NOT NULL,
                activator_id    INTEGER    NOT NULL,
                date    DATE    NOT NULL          
             );
    """)




# the repository singleton
repo = _Repository()
atexit.register(repo._close)