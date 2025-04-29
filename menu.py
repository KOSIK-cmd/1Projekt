import sqlite3
conn = sqlite3.connect("database.sqlite")
cursor = conn.cursor()
def addmenuItems(ItemID,Name,Price,Category)
    cursor.execute("INSERT INTO MenuItems (ItemID,Name,Price,Category) VALUES (?,?,?,?)",)
    (ItemID,Name,Price,Category)
    new_id = cursor.lastrowid
    return new_id

def selectmenuItems(ItemID):
    cursor.execute("SELECT * FROM MenuItems WHERE ItemID = ?",(ItemID,))
    return cursor.fetchall()

def selectName(Name):
    cursor.execute("SELECT * FROM MenuItems WHERE Name = ?",(Name,))
    return cursor.fetchall()

def selectPrice(Price):
    cursor.execute("SELECT * FROM MenuItems WHERE Price = ?",(Price,))
    return cursor.fetchall()

def selectCategory(Category):
    cursor.execute("SELECT * FROM MenuItems WHERE Category = ?",(Category,))
    return cursor.fetchall()

def deletemenuItem(ItemID):
    cursor.execute("DELETE FROM MenuItems WHERE ItemID = ?",(ItemID,))
    conn.commit()
    return
