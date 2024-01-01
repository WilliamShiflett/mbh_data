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

r = requests.get('https://s3.amazonaws.com/capitalbikeshare-data/202112-capitalbikeshare-tripdata.zip')
z = zipfile.ZipFile(io.BytesIO(r.content))
df = pd.read_csv(z.open('202112-capitalbikeshare-tripdata.csv'))
print(df.to_markdown)

# print(z.namelist())
# print(z.infolist())

# with z as myzip:
#     with myzip.open('202112-capitalbikeshare-tripdata.csv') as myfile:
#         print(myfile.read())

# output = io.StringIO()
# output.write('First line.\n')
# print('Second line.', file=output)

# # Retrieve file contents -- this will be
# # 'First line.\nSecond line.\n'
# contents = output.getvalue()

# # Close object and discard memory buffer --
# # .getvalue() will now raise an exception.
# output.close()

# def unzip_zip_files():

# def main():
#     zip_url_list = page_crawler(URL)


# if __name__=='__main__':
#     main()


