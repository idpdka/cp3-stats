import psycopg2
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine('postgresql://nedkrs@localhost/cp3_stats', echo=False)

if __name__ == "__main__":
    df = pd.read_csv('./data/cp_subcomplex.csv', header=0, delimiter=';')
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df['created_at'] = df['created_at'].astype('datetime64[ns]')
    df['updated_at'] = df['updated_at'].astype('datetime64[ns]')
    df['deleted_at'] = df['deleted_at'].astype('datetime64[ns]')

    df.to_sql('subcomplex', if_exists='replace', con=engine)