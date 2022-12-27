
import requests

url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.91601&lon=10.85363'

headers = {
    'User-Agent': 'My Agent 1.0',
    'From': 'morten.stavik.eggen@gmail.com'
}

response = requests.get(url, headers=headers)
print(response)

data = response.json()

print(data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"])


import xlwt
wb = xlwt.Workbook()

sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0,0,"Temperatur:")
sheet1.write(0,1, data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"])

wb.save("Weather.xls")