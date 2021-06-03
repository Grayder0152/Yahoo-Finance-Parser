import datetime
import requests

BASE_URL = f'https://query1.finance.yahoo.com/v7/finance/download/'
date_now = datetime.datetime.today().date().strftime("%s")


def parse_data(company: str) -> requests.models.Response:
    filters = f'{company}?period1=0&period2={date_now}&interval=1d&events=history&includeAdjustedClose=true'
    return requests.get(BASE_URL + filters)
