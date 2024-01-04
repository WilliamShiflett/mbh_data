'''
Given a list of zip files:
1.) Unzip them in memory
2.) Load into database
'''    
import logging
import io
import requests
import zipfile
import csv
import pandas as pd
from get_trip_zips import page_crawler, MAIN_URL

RAW_LIST_OF_CSVS = []
DIRTY_LIST_OF_CSVS = []
CLEAN_LIST_OF_CSVS = []


def data_frame_loader(zip_url_list:list) -> pd.DataFrame:

    for zip in zip_url_list:

        try:
            request_zip = requests.get(zip)
            zip_file = zipfile.ZipFile(io.BytesIO(request_zip.content))
            RAW_LIST_OF_CSVS.append(zip_file.namelist())

            # df = pd.read_csv(zip_file.open('202112-capitalbikeshare-tripdata.csv'))
            # print(df.to_markdown)
        except:
            logging.warning(f'{zip} is not a zip file. Ignoring...')

    for raw_element in RAW_LIST_OF_CSVS:
        DIRTY_LIST_OF_CSVS.extend(raw_element)

    for dirty_element in DIRTY_LIST_OF_CSVS:
        if not dirty_element.startswith('__MACOSX'):
            CLEAN_LIST_OF_CSVS.append(dirty_element)

    return CLEAN_LIST_OF_CSVS

def main():
    zip_url_elements = page_crawler(MAIN_URL)
    loaded_data_frame = data_frame_loader(zip_url_elements)

if __name__=='__main__':
    main()


