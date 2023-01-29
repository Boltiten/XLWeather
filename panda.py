import requests
from datetime import datetime, date
import pandas as pd



url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.63333&lon=11.11667'

headers = {
    'User-Agent': 'My Agent 1.0',
    'From': 'morten.stavik.eggen@gmail.com'
}

response = requests.get(url, headers=headers)
print(response)

data = response.json()

print(data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"])

df = pd.read_excel('G:\My Drive\Personlige Prosjekt\Været\Strømanalyse2023-1.xlsx', sheet_name='Ute Temp')
print(df)
writer = pd.ExcelWriter('G:\My Drive\Personlige Prosjekt\Været\Strømanalyse2023-1.xlsx', engine='openpyxl')
df.to_excel(writer, sheet_name='Ute Temp2')

writer.save()