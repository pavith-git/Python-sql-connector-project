from tabulate import tabulate
import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="****",
            database="python_db"
        )
        self.cursor = self.con.cursor()

    def insert(self, name, age, city):
        sql = "INSERT INTO users (name, age, city) VALUES (%s, %s, %s)"
        self.cursor.execute(sql, (name, age, city))
        self.con.commit()
        print("Data Insert Success")

    def update(self, id, name, age, city):
        sql = "UPDATE users SET name=%s, age=%s, city=%s WHERE id=%s"
        self.cursor.execute(sql, (name, age, city, id))
        self.con.commit()
        print("Data Update Success")

    def select(self):
        sql = "SELECT ID, NAME, AGE, CITY FROM users"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        print(tabulate(result, headers=["ID", "NAME", "AGE", "CITY"]))

    def delete(self, id):
        sql = "DELETE FROM users WHERE id=%s"
        self.cursor.execute(sql, (id,))
        self.con.commit()
        print("Data Delete Success")

# Using the class
db = Database(host="localhost", user="root", password="6669", database="python_db")

while True:
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Select Data")
    print("4. Delete Data")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        city = input("Enter City: ")
        db.insert(name, age, city)

    elif choice == 2:
        id = input("Enter the ID You Want to Update: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        city = input("Enter City: ")
        db.update(id, name, age, city)

    elif choice == 3:
        db.select()

    elif choice == 4:
        id = input("Enter the ID to Delete: ")
        db.delete(id)

    elif choice == 5:
        exit()

    else:
        print("Invalid Selection, Please Try Again!")

        
        
        
        
        