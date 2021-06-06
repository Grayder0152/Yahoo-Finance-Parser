import datetime
from database import save_data_to_db

BASE_URL = f'https://query1.finance.yahoo.com/v7/finance/download/'


async def parse_data(company, session):
    date_now = datetime.datetime.today().date().strftime("%s")
    url = BASE_URL + f'{company}?period1=0&period2={date_now}&interval=1d&events=history&includeAdjustedClose=true'

    async with session.get(url) as response:
        if response.status == 200:
            data = await response.text()
            save_data_to_db(company, data)
        else:
            print(f"\033[31mCompany '{company}' don`t have information.")
