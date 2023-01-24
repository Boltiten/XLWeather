
import requests
from datetime import datetime, date
import xlwt
from xlutils.copy import copy
import xlrd


url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.63333&lon=11.11667'

headers = {
    'User-Agent': 'My Agent 1.0',
    'From': 'morten.stavik.eggen@gmail.com'
}

response = requests.get(url, headers=headers)
print(response)

data = response.json()

print(data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"])


try:
    rb = xlrd.open_workbook("G:\My Drive\Personlige Prosjekt\Været\Weather.xls")
    r_sheet = rb.sheet_by_index(0)
    wb = copy(rb)
    w_sheet = wb.get_sheet(0)
except:
    wb = xlwt.Workbook()
    w_sheet = wb.add_sheet('sheet1')

style1 = xlwt.XFStyle()
style1.num_format_str = 'DD-MM-YY'
cell_row = datetime.now().timetuple().tm_yday
today = date.today()
print(today)
w_sheet.write(cell_row-23, 0, today, style1)
w_sheet.write(cell_row-23, 1, data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"])


wb.save("G:\My Drive\Personlige Prosjekt\Været\Weather.xls")