import argparse
import psycopg2
import pandas as pd
import numpy as np
import os
from sqlalchemy import create_engine

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ssl", help="Use SSL Mode", action="store_true")
    args = parser.parse_args()

    DATABASE_URL = os.environ['DATABASE_URL']
    if 'postgresql' not in DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace('postges', 'postgresql') 

    if args.ssl:
        conn = create_engine(DATABASE_URL, echo=False)
    else:
        conn = create_engine(DATABASE_URL, echo=False)

    df = pd.read_csv('./data/cp_tenants.csv', header=0, delimiter=';')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df['created_at'] = '2022-06-19 00:00:00'
    df['deleted_at'] = np.nan
    df['funding_confirmed_at'] = np.nan
    df['created_at'] = df['created_at'].astype('datetime64[ns]')
    df['updated_at'] = df['updated_at'].astype('datetime64[ns]')
    df['deleted_at'] = df['deleted_at'].astype('datetime64[ns]')
    df['funding_confirmed_at'] = df['funding_confirmed_at'].astype('datetime64[ns]')

    df.to_sql('unit', if_exists='replace', con=conn, index='id')