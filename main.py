from database import save_data_to_db
from rest import get_json_data

companies_list = ('PD', 'ZUO', 'PINS', 'ZM', 'PVTL', 'DOCU', 'CLDR', 'RUN')

if __name__ == '__main__':
    print("\033[33mParse and save data to database...")
    save_data_to_db(companies_list)
    print("\033[32mAll data saved success.\n")

    print("\033[33mJSON with the saved data:")
    print(get_json_data('PD'))
