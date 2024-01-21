import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'add_data_py'
}

conn = mysql.connector.connect(**db_config)

cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    occupation VARCHAR(255),
    salary DECIMAL(10, 2)
)
'''
cursor.execute(create_table_query)

name = input("name : ")
occupation = input("position : ")
salary = float(input("salary : "))

insert_data_query = '''
INSERT INTO employees (name, occupation, salary) VALUES (%s, %s, %s)
'''
data = (name, occupation, salary)
cursor.execute(insert_data_query, data)

conn.commit()

cursor.close()
conn.close()