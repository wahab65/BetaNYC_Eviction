import csv
import sqlalchemy
import pandas as pd
import glob
import os
from dotenv import load_dotenv

load_dotenv()

engine = sqlalchemy.create_engine(os.getenv('NYCDB_DATABASE'))

for sql_file_name in glob.glob('*.sql'):
    print(f'Running {sql_file_name}')
    with open(sql_file_name, 'r') as file:
        query = file.read()

    df = pd.read_sql_query(query, con=engine)
    csv_file_name = sql_file_name.replace('.sql','.csv')
    df.to_csv(csv_file_name, index = False)
    print(f'Saved to {csv_file_name}\n')
