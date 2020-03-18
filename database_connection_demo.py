import sqlite3
import csv


def printDB():
    try:
        result = theCursor.execute(
            "SELECT id, FName, LName, Age, Address, Salary, HireDate FROM Employees")
        for row in result:
            print("ID :", row[0])
            print("FName :", row[1])
            print("LName :", row[2])
            print("Age :", row[3])
            print("Address :", row[4])
            print("Salary :", row[5])
            print("HireDate :", row[6])

    except sqlite3.OperationalError:
        print("The table doesn't exist")
    except:
        print("Couldn't get data")


db_conn = sqlite3.connect('test.db')
print("Database created")
theCursor = db_conn.cursor()

try:
    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, Age INT NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")
    db_conn.commit()
    print("Table Created")
except sqlite3.OperationalError:
    print("Table Not Created")


db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate)"
                "VALUES ('Derek', 'Banas', 41, '123 Main St', '500,000', date('now'))")
db_conn.commit()
printDB()
db_conn.close()
