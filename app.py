
# This program takes figure input from the user and saves to the database.

import sqlite3

#  Connect to the 'test.db' database and create it if it doesn't exist.
conn = sqlite3.connect('test.db')
print("Opened database successfully.")

# conn.execute("""CREATE TABLE FIGURE
#              (ID INT PRIMARY KEY    NOT NULL,
#              NAME       TEXT       NOT NULL,
#              ST_ALIGN   TEXT    NOT NULL,
#              END_ALIGN  TEXT    NOT NULL,
#              STEPS      INT     NOT NULL,
#              ST_FOOT        CHAR(5) NOT NULL,
#              END_FOOT   CHAR(5) NOT NULL);""")
# print("Created the Figures table.")
# conn.close()

# conn.execute("INSERT INTO FIGURE (ID,NAME,ST_ALIGN,END_ALIGN,STEPS,ST_FOOT,END_FOOT) \
#              VALUES (1, 'Reverse Turn', 'DC', 'DW',6,'LF','RF')")
# conn.commit()
# print("Record created successfully.")
# conn.close()

curs = conn.execute("SELECT id, name, st_align from FIGURE")
for row in curs:
    print(f"ID: {row[0]}")
    print(f"Name: {row[1]}")
    print(f"Starting Alignment: {row[2]}", "\n")
print("Selection completed successfully.")
conn.close()
    