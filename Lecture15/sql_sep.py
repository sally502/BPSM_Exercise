#realized that it should be two seperated functions

import os
import MySQLdb

# Function 1: Let the user choose a table
def get_table_choice(host, user, password, database):
    """
    Display all available tables and let the user select one.
    Return the selected table name, or None if exit/error.
    """
    connection = None
    cursor = None

    try:
        connection = MySQLdb.connect(
            host=host,
            user=user,
            passwd=password,
            db=database
        )

        cursor = connection.cursor()

        # Fetch all tables
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]

        if not tables:
            print("No tables found in this database.")
            return None

        # Display available tables
        print("\nAvailable Tables:")
        print("-" * 30)

        for index, table_name in enumerate(tables, 1):
            print(f"[{index}] {table_name}")

        print("-" * 30)

        # Ask the user to choose a table
        while True:
            try:
                choice = input(
                    f"Pick a table number (1-{len(tables)}) or 'q' to quit: "
                ).strip()

                if choice.lower() == 'q':
                    return None

                choice_num = int(choice)

                if 1 <= choice_num <= len(tables):
                    return tables[choice_num - 1]
                else:
                    print(f"Invalid number. Choose 1-{len(tables)}.")

            except ValueError:
                print("Please enter a valid number or 'q'.")

    except MySQLdb.Error as e:
        print(f"Database error: {e}")
        return None

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


# Function 2: Show the structure of the selected table
def show_table_structure(host, user, password, database, table_name):
    """
    Display the structure of the selected database table.
    """
    connection = None
    cursor = None

    try:
        connection = MySQLdb.connect(
            host=host,
            user=user,
            passwd=password,
            db=database
        )

        cursor = connection.cursor()

        # Validate the table name against existing tables
        cursor.execute("SHOW TABLES")
        valid_tables = [row[0] for row in cursor.fetchall()]

        if table_name not in valid_tables:
            print("Invalid table name.")
            return

        # Get the table structure
        cursor.execute(f"DESCRIBE `{table_name}`")
        columns = cursor.fetchall()

        # Display the structure
        print(f"\nStructure for table: '{table_name}'")
        print("~" * 60)
        print(f"{'Field Name':<20} | {'Type':<15} | {'Null Allowed?':<13} | {'Key'}")
        print("~" * 60)

        for col in columns:
            print(f"{col[0]:<20} | {col[1]:<15} | {col[2]:<13} | {col[3]}")

        print("-" * 60)

    except MySQLdb.Error as e:
        print(f"Database error: {e}")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()


# Main program: Connect the two functions
host = "127.0.0.1"
user = os.environ["USER"]
password = os.environ["MYSQL_PASSWORD"]
database = user + "_exercises"

selected_table = get_table_choice(host, user, password, database)

if selected_table is not None:
    show_table_structure(host, user, password, database, selected_table)

