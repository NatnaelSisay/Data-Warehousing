
import pandas as pd
import psycopg2


richard_columns = ["timestamp","flow1","occupancy1","flow2","occupancy2","flow3","occupancy3","totalflow","weekday","hour","minute","second"]
richards_table_query = '''CREATE TABLE richards_sensors(
        timestamp TIMESTAMP,
        flow1 FLOAT,
        occupancy1 FLOAT,
        flow2 FLOAT,
        occupancy2 FLOAT,
        flow3 FLOAT,
        occupancy3 FLOAT,
        totalflow FLOAT,
        weekday INTEGER,
        hour INTEGER,
        minute INTEGER,
        second INTEGER
)'''

RICHARD_TABLE_NAME = 'richards_sensors'
DATA_SOURCE_ADDRES = '/Users/java/Desktop/python-check/sample_richards.csv'
DATABASE_BEZ = 'bez'
DATABASE_DEV = 'development'

USER = 'java'

def get_db_connection(database=DATABASE_DEV):
    try:
        print('Trying to connect to Database')
        connection = psycopg2.connect(user = USER,
                                  password = "",
                                  host = "localhost",
                                  port = "5432",
                                  database = database)
        print('Connected.')
        return connection

    except:
        print("[ ERROR ] coudn't connect to databse")
        return None


def create_table(database, query):
    conn = get_db_connection(database)
    try:
        print('Creating A Table')
        
        cursor = conn.cursor()
        cursor.execute(query)    
        conn.commit()

        print('Table Created')
    except:
        print("[ ERROR ] can't exicute the query")
        return None
    
    finally:
        if(conn):
            conn.close()


def add_to_table(database, table_name, values):
    conn = get_db_connection(database)
    try:
        print(f"Adding New Data To {table_name} Table")

        cursor = conn.cursor()
        placeholder = ("%s, " * len(values))[:-2]
        cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholder})", values)    
        conn.commit()

        print('New Data Added.')
    
    except Exception as e:
        print("[ ERROR ] couldn't add to the table")
        print(e)
    
    finally:
        if(conn):
            conn.close()


def drop_table(database, table_name):
    conn = get_db_connection(database)
    try:
        cursor = conn.cursor()
        cursor.execute(f'DROP TABLE {table_name}')
    except Exception as e:
        print(f'Failed to drop {table_name}')
        print(e)


def clear_table(database, table_name):
    conn = get_db_connection(database)
    try:
        print('Clearning Table')
        
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM {table_name}')
        conn.commit()

        print('Table Cleared')
        
    except Exception as e:
        print(f"[ ERROR ] couldn't clear {table_name} table")
        print(e)
    

def add_to_table_from_dataset(source_path, table_name):
    
    conn = get_db_connection(DATABASE_DEV)
    cursor = conn.cursor()

    print("Setting up dataframe ...")
    df = pd.read_csv(source_path, sep=',',quotechar='\"', encoding='utf-8')
    tuples = [tuple(x) for x in df.to_numpy()]
    cols = ','.join(list(df.columns))

    print("Generating query string from the data ...")
    placeholder = ("%%s, " * len(df.columns))[:-2]
    query  = ("INSERT INTO %s(%s) VALUES("+placeholder+")" )% (table_name, cols)
    
    try:
        print("Exicuting Querys")
        
        cursor.executemany(query, tuples)
        conn.commit()
        conn.close()

        print('Finished Exicuting Queries')

    except Exception as e:
        print(f'[ ERROR ] Failed to add data to {table_name} table')
        print(e)


# if __name__ == '__main__':
# i need to run thus files in the dag.

def main():
    create_table(DATABASE_DEV, richards_table_query)
    clear_table(DATABASE_DEV, RICHARD_TABLE_NAME)
    add_to_table_from_dataset(DATA_SOURCE_ADDRES,RICHARD_TABLE_NAME)

# Function to check the proper insertion of data
def read_from_table(database, table):
    conn =get_db_connection(database)
    cursor = conn.cursor()
    cursor.execute(f'Select * from {table}')
    result = cursor.fetchall()

    print(result)
    conn.close()
# read_from_table(DATABASE_DEV, RICHARD_TABLE_NAME)