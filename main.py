from rest import get_json_data
from parser import parse_data

import asyncio
import aiohttp

companies_list = ('PD', 'ZUO', 'PINS', 'ZM', 'PVTL', 'DOCU', 'CLDR', 'RUN')


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for country in companies_list:
            tasks.append(asyncio.create_task(parse_data(country, session)))
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
    print("\033[33mJSON with the saved data:")
    print(get_json_data('PD'))
