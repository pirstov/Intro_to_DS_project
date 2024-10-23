import sqlitecloud
import pandas as pd
from keys import DB_CONNECTION_STRING


columns = [
    'Aika',                        # Timestamp
    'Hinta_snt_per_kWh',            # Price in cents per kWh
    'Keskituulen_nopeus_m_per_s',   # Average wind speed in m/s
    'Lampotilan_keskiarvo_C',       # Average temperature in Celsius
    'Kulutus_kWh_per_h',            # Energy consumption in kWh per hour
    'Tuotanto_kW',                  # Production in kW
    'is_holiday'                    # Holiday flag (1 if holiday, 0 if not)
]

def get_last_n_rows(n):

    conn = sqlitecloud.connect(DB_CONNECTION_STRING)

    query = f'SELECT * FROM PRICES ORDER BY Aika DESC LIMIT {n};'
    
    print(query)

    cursor = conn.execute(query)
    result = cursor.fetchall()

    df = pd.DataFrame(result,columns=columns)
    df['Aika'] = pd.to_datetime(df['Aika'])
    conn.close()
    return df

def get_data_from_db():

    conn = sqlitecloud.connect(DB_CONNECTION_STRING)

    cursor = conn.execute("SELECT * FROM PRICES")
    result = cursor.fetchall()

    df = pd.DataFrame(result,columns=columns)

    conn.close()
    return df

df = get_last_n_rows(7*24)
print(df.shape)

"""
data = pd.read_csv('./.data/data.csv')
data = data.rename(columns={
    'Aika': 'Aika',  # Keep the same
    'Hinta (snt/kWh)': 'Hinta_snt_per_kWh',
    'Keskituulen nopeus [m/s]': 'Keskituulen_nopeus_m_per_s',
    'Lämpötilan keskiarvo [°C]': 'Lampotilan_keskiarvo_C',
    'Kulutus (kWh/h)': 'Kulutus_kWh_per_h',
    'Tuotanto (kW)': 'Tuotanto_kW',
    'is_holiday': 'is_holiday'  
})

data['Aika'] = pd.to_datetime(data['Aika'])
data = data[data['Aika'] >= '2024-01-01']
conn = sqlitecloud.connect(DB_CONNECTION_STRING)
data.to_sql('PRICES', conn, if_exists='append', index=False)
conn.close()
"""