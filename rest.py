from database import connection_to_db
from pydantic import BaseModel


class CompanyFinancialData(BaseModel):
    date: str
    open: float
    high: float
    low: float
    close: float
    adj_close: float
    volume: float


@connection_to_db
def get_json_data(company: str, db_cursor) -> list:
    keys = CompanyFinancialData.__fields__.keys()
    data = db_cursor.execute(f"SELECT * FROM {company} ORDER BY date DESC").fetchall()
    return [CompanyFinancialData(**dict(zip(keys, values))).dict() for values in data]


@connection_to_db
def get_all_json_data(db_cursor) -> dict:
    companies = db_cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'").fetchall()
    json_data = {}
    for company in companies:
        json_data[company[0]] = get_json_data(company[0])
    return json_data
