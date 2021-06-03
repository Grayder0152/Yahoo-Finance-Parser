from parser import parse_data

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
def save_data_to_db(companies: (list, tuple, set), db_cursor: sqlite3.Cursor) -> None:
    for company in companies:
        data = parse_data(company)
        if data:
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

            rows = data.text.split('\n')[1:]
            for row in rows:
                row = row.split(',')
                db_cursor.execute("INSERT INTO {} VALUES ('{}',{},{},{},{},{},{})".format(company, *row))
        else:
            print(f"\033[31mCompany '{company}' don`t have information.")
