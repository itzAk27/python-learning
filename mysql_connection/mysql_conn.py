import mysql.connector


def get_conn():
    try:
        mydb = mysql.connector.connect(
            host="localhost",  # Or the IP address/hostname of your MySQL server
            user="root",
            password="password",
            database="my_new_db" # Optional: specify a database to connect to directly
        )

        print("Connection established successfully!")

        return mydb
    
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")

conn = get_conn()
# print(dir(conn))

# print(conn.is_connected())
# print(locals())
# help(conn.is_connected())

if 'conn' in locals() and conn.is_connected():
    mycursor = conn.cursor()
    print(mycursor)

if 'mycursor' in locals():
    mycursor.execute("SELECT * FROM info")

if 'mycursor' in locals():
    myresult = mycursor.fetchall()
    print(myresult)

    for row in myresult:
        print(row)

if 'mycursor' in locals():
    mycursor.close()

if 'conn' in locals() and conn.is_connected():
    conn.close()
    print("Connection closed.")