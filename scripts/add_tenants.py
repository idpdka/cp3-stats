import psycopg2
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

DATABASE_URL = os.environ['DATABASE_URL']
engine = create_engine(DATABASE_URL, echo=False)

if __name__ == "__main__":
    df = pd.read_csv('./data/cp_tenants.csv', header=0, delimiter=';')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df['created_at'] = '2022-06-19 00:00:00'
    df['deleted_at'] = np.nan
    df['funding_confirmed_at'] = np.nan
    df['created_at'] = df['created_at'].astype('datetime64[ns]')
    df['updated_at'] = df['updated_at'].astype('datetime64[ns]')
    df['deleted_at'] = df['deleted_at'].astype('datetime64[ns]')
    df['funding_confirmed_at'] = df['funding_confirmed_at'].astype('datetime64[ns]')

    df.to_sql('unit', if_exists='replace', con=engine, index='id')