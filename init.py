from db import *
q1 = "CREATE DATABASE web_db;"
q2 = "CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(255));"
q3 = "INSERT INTO users VALUES (1,'Muhammad Usman');"

con = connecting_to_server()
create_database(con,q1)
con_to_db = create_db_connection()
execute_query(con_to_db,q2)
execute_query(con_to_db,q3)