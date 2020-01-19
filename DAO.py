from DTO import Employee , Supplier , Activity , Coffee_stand , Product

class Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Employee):
        self._conn.execute("""
               INSERT INTO Employees (id, name,salary,coffee_stand) VALUES (?, ?, ? ,?)
           """, [Employee.id, Employee.name , Employee.salary , Employee.coffee_stand])



class Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Supplier):
        self._conn.execute("""
               INSERT INTO Suppliers (id, name,contact_information) VALUES (?, ? ,?)
           """, [Supplier.id, Supplier.name , Supplier.contact_information])




class Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Product):
        self._conn.execute("""
               INSERT INTO Products (id, description,price,quantity) VALUES (?, ?, ? ,?)
           """, [Product.id, Product.description , Product.price , Product.quantity])

    def find(self, product_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT  *FROM Products WHERE id = ?
        """, [product_id])

        return Product(*c.fetchone())

    def update(self, product):
        self._conn.execute("""
               UPDATE Products SET quantity=(?) WHERE id=(?)
           """, [product.quantity, product.id])




class Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Coffee_stand):
        self._conn.execute("""
               INSERT INTO Coffee_stands (id, location,number_of_employees) VALUES (?, ? ,?)
           """, [Coffee_stand.id, Coffee_stand.location , Coffee_stand.number_of_employees])



class Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, Activity):
        self._conn.execute("""
               INSERT INTO Activities (product_id, quantity,activator_id,date) VALUES (?, ?, ? ,?)
           """, [Activity.product_id, Activity.quantity , Activity.activator_id , Activity.date])


