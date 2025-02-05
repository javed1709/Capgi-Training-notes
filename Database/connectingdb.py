import mysql.connector

# Establish a connection to the MySQL server
def connect_to_server():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Javedrix@8'
    )
    return conn

# Create the database if it doesn't exist
def create_database():
    conn = connect_to_server()
    cursor = conn.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS test_db')
    conn.close()


# Establish a connection to the MySQL database
def connect_to_db():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Javedrix@8',
        database='test_db'
    )
    return conn

# Create the users table if it doesn't exist
def create_users_table():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT
        )
    ''')
    conn.close()


# Create a new record
def create_user(name, age):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, age) VALUES (%s, %s)', (name, age))
    conn.commit()
    conn.close()

# Read all records
def read_users():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Update a record
def update_user(user_id, name, age):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET name = %s, age = %s WHERE id = %s', (name, age, user_id))
    conn.commit()
    conn.close()

# Delete a record
def delete_user(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
    conn.commit()
    conn.close()

create_database()
create_users_table()
# Create a new user
create_user('Alice', 30)
create_user('Bob', 25)

# Read and print all users
print("Users after creation:")
users = read_users()
for user in users:
    print(user)

# Update a user
update_user(1, 'Alice', 31)
print("Users after update:")
users = read_users()
for user in users:
    print(user)

# Delete a user
delete_user(2)
print("Users after deletion:")
users = read_users()
for user in users:
    print(user)