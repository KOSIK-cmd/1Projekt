import sqlite3
conn = sqlite3.connect("database.sqlite")
cursor = conn.cursor()

def addCustomer(firstName, lastName,email,phone):
    cursor.execute("INSERT INTO Customers (FirstName,Lastname,Email,Phone) VALUES (?,?,?,?)",
                (firstName, lastName, email, phone))
    new_id = cursor.lastrowid
    print(f"Nowe ID użytkownika: {new_id}")
    conn.commit()
    return new_id

def deleteCustomer(customerID):
    cursor.execute("DELETE FROM Customers WHERE CustomerID = ?",(customerID,))
    conn.commit()
    return

def selectCustomerByID(customerID):
    cursor.execute("SELECT * FROM Customers WHERE CustomerID = ?",(customerID,))
    return cursor.fetchall()

def selcetCustomerByFirstName(firstname):
    cursor.execute("SELECT * FROM Customers WHERE FirstName = ?",(firstname,))
    return cursor.fetchall()

def selectCustomerByLastName(lastname):
    cursor.execute("SELECT * FROM Customers WHERE LastName = ?",(lastname,))
    return cursor.fetchall()

def selectCustomerByEmail(email):
    cursor.execute("SELECT * FROM Customers WHERE Email = ?",(email,))
    return cursor.fetchall()

def selectCustomerByPhone(phone):
    cursor.execute("SELECT * FROM Customers WHERE Phone = ?",(phone,))
    return cursor.fetchall()

def selectAll():
    cursor.execute("SELECT * FROM Customers")
    return cursor.fetchall()




