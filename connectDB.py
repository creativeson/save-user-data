import mysql.connector
import os

def connectDB(table, query, data=None):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="user_data"
    )
    cursor = conn.cursor()
    try:
        cursor.execute(query, data)
        conn.commit()
        print(f"table {table} created")
    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
    finally:
        cursor.close()
        conn.close()

if __name__ =="__main__":
    table = "user_tracking"
    create_table_query = f'''CREATE TABLE IF NOT EXISTS {table}
                                (id INT AUTO_INCREMENT PRIMARY KEY,
                                user_ip VARCHAR(255) NOT NULL,
                                user_agent VARCHAR(255) NOT NULL,
                                accepted_languages VARCHAR(255) NOT NULL,
                                url VARCHAR(255) ,
                                local_time VARCHAR(255) NOT NULL,
                                button_id VARCHAR(255) NOT NULL,
                                click_to_url VARCHAR(255) 
                                );'''
    connectDB(table, create_table_query)
    
