import sqlite3

DB_NAME = 'companies_financial_data.db'


def connection_to_db(func):
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        result = func(*args, db_cursor=cursor, **kwargs)

        cursor.close()
        connection.commit()
        connection.close()
        return result
    return wrapper


@connection_to_db
def save_data_to_db(company, data, db_cursor):
    db_cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {company} ("
        "date DATE,"
        "open INTEGER,"
        "high INTEGER,"
        "low INTEGER,"
        "close INTEGER, "
        "adj_close INTEGER,"
        "volume INTEGER)"
    )
    for row in data.split('\n')[1:]:
        db_cursor.execute("INSERT INTO {} VALUES ('{}',{},{},{},{},{},{})".format(company, *row.split(',')))
