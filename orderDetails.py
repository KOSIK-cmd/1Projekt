import sqlite3
conn = sqlite3.connect("database.sqlite")
cursor = conn.cursor()

def addOrder(OrderDetailID,OrderID,ItemID,Quantity,Subtotal):
    cursor.execute("INSERT INTO Customers (OrderDetailID,OrderID,ItemID,Quantity,Subtotal) VALUES (?,?,?,?,?)",
 (OrderDetailID,OrderID,ItemID,Quantity,Subtotal))

def deleteOrderID(OrderDetailID): cursor.execute("DELETE FROM Order WHERE OrderDetailID = ?",
(OrderDetailID,))
    conn.commit()
    return

def selectOrder(OrderDetailID):
    cursor.execute("SELECT * FROM Order WHERE OrderID = ?", (OrderID,))
    return cursor.fetchall()

def selecetItem(ItemID):
    cursor.execute("SELECT * FROM Order WHERE ItemID = ?", (ItemID,))
    return cursor.fetchall()

def selectQuantity(Quantity):
    cursor.execute("SELECT * FROM Order WHERE Quantity = ?", (Quantity,))
    return cursor.fetchall()

def selectSubtotal(Subtotal)
    cursor.execute("SELECT * FROM Order WHERE Subtotal = ?", (Subtotal,))
