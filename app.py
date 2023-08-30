# This program takes figure input from the user and saves to the database.

import sqlite3

#  Connect to the 'test.db' database and create it if it doesn't exist.
conn = sqlite3.connect('test.db')

conn.execute("""CREATE TABLE if not exists FIGURE
            (ID INT PRIMARY KEY    NOT NULL,
            NAME       TEXT       NOT NULL,
            ST_ALIGN   TEXT    NOT NULL,
            END_ALIGN  TEXT    NOT NULL,
            STEPS      INT     NOT NULL,
            ST_FOOT        CHAR(5) NOT NULL,
            END_FOOT   CHAR(5) NOT NULL);""")

command = input("""What would you like to do?
      CREATE new figure,
      SHOW all figures \n""")
if command == "CREATE":
    fig_id = input("Id: ")
    figure_name = input("Figure Name: ")
    starting_alignment = input("Starting Alignment: ")
    ending_alignment = input("Ending Alignment: ")
    steps = input("Number of Steps: ")
    starting_foot = input("Starting Foot: ")
    ending_foot = input("Ending Foot: ")

    conn.execute("INSERT INTO FIGURE VALUES (?,?,?,?,?,?,?)", (fig_id, figure_name, starting_alignment, ending_alignment, steps, starting_foot, ending_foot))
    conn.commit()
    print("Record created successfully.")
    conn.close()
elif command == "SHOW":
    curs = conn.execute("SELECT id, name, st_align from FIGURE")
    for row in curs:
        print(f"ID: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Starting Alignment: {row[2]}", "\n")
    print("Selection completed successfully.")
    conn.close()
else:
    print("Sorry, please choose from the available options.")
exit()





    