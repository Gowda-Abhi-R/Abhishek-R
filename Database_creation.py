import mysql.connector as connector

def make_connection():
    global con
    con=connector.connect(host='localhost',user='root',password='root')
    print("connection succesfull")



def create_database(db_name):
    query="CREATE DATABASE IF NOT EXISTS " + str(db_name)
    print("Create db query",query)
    cur=con.cursor()
    cur.execute(query)
    print(db_name,"Database created")

def use_database(db_name):
    query="use "+str(db_name)
    cur = con.cursor()
    cur.execute(query)
    print("we are using",db_name,"database")

def create_table(tb_name):
    query="create table " + str(tb_name) + "(emp_id INT(20),emp_name VARCHAR(20),salary INT(9),dept_id INT(10))"
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    print("table created")

def insert_into(tb_name,emp_id,emp_name,salary,dept_id):
    query="INSERT INTO {} (emp_id,emp_name,salary,dept_id) VALUES ({},'{}',{},{})".format(tb_name,emp_id,emp_name,salary,dept_id)
    print(query)
    cur=con.cursor()
    cur.execute(query)
    con.commit()
    print("item inserted")

def update(tb_name,emp_id,emp_name,salary,dept_id):
    query="UPDATE {} SET emp_name='{}',salary={},dept_id={} WHERE emp_id={}" .format(tb_name,emp_name,salary,dept_id,emp_id)
    print(query)
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    print("item updated")

def delete(tb_name):
    query='DELETE FROM ' + str(tb_name) + ' WHERE '+'emp_id=' + input("enter emp_id:")
    print(query)
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    print("Data deleted succesfully")

def fetch_all(tb_name):
    query="select * from " + str(tb_name) + " ORDER BY emp_id "
    cur=con.cursor()
    cur.execute(query)
    for x in cur:
        print(x)
    #con.commit()

def main():
    make_connection()
    print("Press any key:")
    while(True):
        print("1- To create database")
        print("2- To use database")
        print("3- To create table")
        print("4- To insert values")
        print("5- To display ")
        print("6-To update")
        print("7-To delete")
        print("8-To exit")
        key = int(input("enter the key :"))

        if key==1:
            db_name=input("Enter a database name:")
            create_database(db_name)
            use_database(db_name)
        elif key==2:
            db_name=input("enter database name:")
            use_database(db_name)
            print("using",db_name,"database")
        elif key==3:
            db_name=input("Enter a database name")
            use_database(db_name)
            tb_name=input("Enter a table name:")
            create_table(tb_name)
            print("table created")

        elif key==4:
            db_name=input("enter a database name:")
            use_database(db_name)
            tb_name=input("enter table name ")
            insert_into(tb_name, int(input("Enter a Id:")), input("Enter name:"), input("Enter salary:"),
                        int(input("Enter department_id:")))
            print("values inserted")


        elif key==5:
            db_name = input("enter database name:")
            tb_name=input("enter table name to display:")
            use_database(db_name)
            fetch_all(tb_name)


        elif key==6:
            db_name=input("enter database name:")
            tb_name=input("Enter table name for updation:")
            use_database(db_name)
            update(tb_name,input("Enter emp_id:"), input("Enter emp_name:"), input("Enter salary:"), input("Enter dept_id:"))
            print("updation succesfull")

        elif key==7:
            db_name = input("enter database name:")
            use_database(db_name)
            tb_name = input("enter table name:")
            delete(tb_name)
            print("Data deleted succesfully")

        elif key==8:
            break

        else:
            break

if __name__=="__main__":
    main()