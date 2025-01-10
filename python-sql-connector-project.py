from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="****",database="python_db")  #Enter the database created in Mysql

def insert(name,age,city):
    res=con.cursor()
    sql="insert into users (name,age,city) values(%s,%s,%s)"
    user=(name,age,city)
    res.execute(sql,user)
    con.commit()
    print("Data Insert Success")


def update(name, age, city, id):
    res=con.cursor()
    sql="update users set name=%s,age=%s,city=%s where id=%s"
    user=(name,age,city,id)                                        
    res.execute(sql,user)
    con.commit()
    print("Data Update Success")


def select():
    res=con.cursor() ##it is a connector between python and sql
    sql="SELECT ID,NAME,AGE,CITY from users"
    res.execute(sql)
   # result=res.fetchone(); it will return top most result(only one)
   # result=res.fetchmany(2); it will resturn what we provided
    result =res.fetchall();   #it will return all the data
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))  #we intalled tabulate
    
def delete(id):
    res=con.cursor()
    sql="delete from users where id=%s"
    user=(id,)                                        
    res.execute(sql,user)
    con.commit()
    print("Data Delete Success")

while True:
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Select Data")
    print("4. Delete Data")
    print("5. Exit")
    
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        name=input("Enter Name: ")
        age=input("Enter Age: ")
        city=input("Enter City ")
        insert(name, age, city)
        
    elif choice==2:
        id=input("Enter the ID You Want to Update: ")
        name=input("Enter Name: ")
        age=input("Enter Age: ")
        city=input("Enter City: ")
        update(name, age, city, id)
        
    elif choice==3:
        select()
        
    elif choice==4:
        id=input("Enter the ID to Delete: ")
        delete(id)
        
    elif choice==5:
        exit()
        
    else:
        print("Invalid Selection, Please Try Again!")
    
        
        
        
        
        
