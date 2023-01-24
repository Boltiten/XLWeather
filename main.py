
import requests
from datetime import datetime, date
import xlwt
from xlutils.copy import copy
import xlrd


url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.91601&lon=10.85363'

headers = {
    'User-Agent': 'My Agent 1.0',
    'From': 'morten.stavik.eggen@gmail.com'
}

response = requests.get(url, headers=headers)
print(response)

data = response.json()

print(data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"])



rb = xlrd.open_workbook("G:\My Drive\Personlige Prosjekt\Været\Weather.xls")
r_sheet = rb.sheet_by_index(0)
wb = copy(rb)
w_sheet = wb.get_sheet(0)

w_sheet.write(0,0,"Temperatur:")

cell_row = datetime.now().timetuple().tm_yday

w_sheet.write(cell_row-24, 1, data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"])

wb.save("G:\My Drive\Personlige Prosjekt\Været\Weather.xls")