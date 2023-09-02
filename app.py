# This program takes figure input from the user and saves to the database.

import sqlite3

#  Connect to the 'test.db' database and create it if it doesn't exist.
conn = sqlite3.connect('test.db')

print("Creating table if one doesn't exist.")
conn.execute("""CREATE TABLE if not exists FIGURE
            (ID INT PRIMARY KEY    NOT NULL,
            NAME       TEXT       NOT NULL,
            ST_ALIGN   TEXT    NOT NULL,
            END_ALIGN  TEXT    NOT NULL,
            STEPS      INT     NOT NULL,
            ST_FOOT        CHAR(5) NOT NULL,
            END_FOOT   CHAR(5) NOT NULL);""")

# If they choose to add, use their input to populate an insert query
final_row = conn.execute("SELECT * FROM FIGURE ORDER BY ID DESC LIMIT 1;").fetchone()

# Prompt the user for the action of their choice
command = input("""What would you like to do?
      *add* new figure,
      *show* all figures,
      *seed* the database,
      *choreo*graph a new routine \n""")


# If they choose the add command, create a new record from data inputs
if command == "add":
    figure_name = input("Figure Name: ")
    starting_alignment = input("Starting Alignment: ")
    ending_alignment = input("Ending Alignment: ")
    steps = input("Number of Steps: ")
    starting_foot = input("Starting Foot: ")
    ending_foot = input("Ending Foot: ")

    conn.execute("INSERT INTO FIGURE VALUES (?,?,?,?,?,?,?)", (final_row[0] + 1, figure_name, starting_alignment, ending_alignment, steps, starting_foot, ending_foot))
    conn.commit()
    print("Record created successfully.", conn.total_changes)
    conn.close()

# If they choose to show the table, print out all records
elif command == "show":
    curs = conn.execute("SELECT id, name, st_align, end_align, steps, st_foot, end_foot from FIGURE")
    for row in curs:
        print(f"ID: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Starting Alignment: {row[2]}   ---   Ending Alignment: {row[3]}")
        print(f"Starting Foot: {row[5]}   ---   Ending Foot: {row[6]}   ---   Steps: {row[4]}")
    print("Selection completed successfully.")
    conn.close()

# If they choose to seed the database, enter preset values
elif command == "seed":
    conn.execute(f"INSERT into FIGURE VALUES ({final_row[0] + 1},'Reverse Turn', 'DW', 'DC', 6, 'LF', 'RF')")
    conn.commit()
    print(conn.total_changes)

elif command == "choreo":
    curs = conn.execute("SELECT id, name, st_align, end_align, steps, st_foot, end_foot from FIGURE").fetchall()
    # Begin with the first figure
    # Append a new figure to the routine if the preceding figure's ending alignment is the same as the following figure's starting alignment
    # and the preceding ending foot is not the same as the following figure's starting foot
    precede = curs[2]
    print(f"Precede is {precede}")
    possible_follows = conn.execute(f"SELECT * from FIGURE WHERE ST_ALIGN = '{precede[3]}' AND NOT ST_FOOT = '{precede[6]}'").fetchall()
    print(f"Possible follows are - {possible_follows}")
else:
    conn.close()
    print("Sorry, please choose from the available options.")
exit()





    