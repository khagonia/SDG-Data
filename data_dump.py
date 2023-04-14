import data_extract_transform as data
import pandas as pd
import time
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import text

print('Script execution start.\n')
start = time.perf_counter()

DB_HOST = 'localhost:5432'
DB_NAME = 'sdg_data'
DB_USER = 'postgres'
DB_PASS = 'admin'

engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}', echo=False)

with engine.connect() as conn:
    print('Re-initializing tables...')
    conn.execute(text("CALL initialize_tables()"))
    conn.commit()
    print('Success!\n')

    print(f'Inserting {len(data.df.index)} rows to public.country_data on {DB_NAME}...')
    data.df.to_sql('overall_data', engine, if_exists='append', index=False, schema='public', chunksize=10000)
    print(f'Successfully inserted {len(data.df.index)} rows.\n')

    print(f'Inserting {len(data.def_df.index)} rows to public.country_data on {DB_NAME}...')
    data.def_df.to_sql('definitions', engine, if_exists='append', index=False, schema='public', chunksize=10000)
    print(f'Successfully inserted {len(data.def_df.index)} rows.\n')

    print(f'Inserting {len(data.df_goal.index)} rows to public.country_data on {DB_NAME}...')
    data.df_goal.to_sql('goal_data', engine, if_exists='append', index=False, schema='public', chunksize=10000)
    print(f'Successfully inserted {len(data.df_goal.index)} rows.\n')

end = data.end + time.perf_counter() - start
print(f'Sucessfully executed in {end:.2f} seconds')

