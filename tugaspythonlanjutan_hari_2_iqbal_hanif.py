!pip install openpyxl
from openpyxl import Workbook
from openpyxl.chart import BarChart, Series, Reference
import csv
import pandas as pd

!wget https://raw.githubusercontent.com/iqbalhanif/Sanberlearn/master/jumlah-penduduk-kota-bandung.csv
!wget https://raw.githubusercontent.com/iqbalhanif/Sanberlearn/master/luas-wilayah-menurut-kecamatan-di-kota-bandung-2017.csv

# agregasi
df1 = pd.read_csv("jumlah-penduduk-kota-bandung.csv")
df2 = pd.read_csv("luas-wilayah-menurut-kecamatan-di-kota-bandung-2017.csv")
df = df2.join(df1.set_index('Kecamatan  '), on='Nama Kecamatan')

df['Kepadatan Penduduk'] = df['Jumlah_Penduduk']/(df['Luas Wilayah (m2)']/100)
df_final = df[['Nama Kecamatan', 'Kepadatan Penduduk']]
df_final.head()
df_final.to_csv('namefile.csv')

# buat barchart
from openpyxl import Workbook
from openpyxl.chart import BarChart, Series, Reference
import csv

#inisiasi excel
wb = Workbook()
ws = wb.active

#open file
data = open('namefile.csv')
rows = csv.reader(data, delimiter=',')

index = 0
for row in rows:
    data_clean = []
    for i in row:
        try:
            i = float(i)
        except:
            pass
        data_clean.append(i)
    ws.append(data_clean)
    index +=1
len_row = len(data_clean)

chart1 = BarChart()
chart1.type = "col"
chart1.style = 5
chart1.title = "Kepadatan Penduduk"
chart1.y_axis.title = 'Kepadatan Penduduk per 100m2'
chart1.x_axis.title = 'Kecamatan'

data = Reference(ws, min_col=3, min_row=1, max_row=index, max_col=3)
cats = Reference(ws, min_col=2, min_row=2, max_row=index, max_col=2)
chart1.height = 10 # default is 7.5
chart1.width = 30 # default is 15
chart1.add_data(data, titles_from_data=True)
chart1.set_categories(cats)
ws.add_chart(chart1, "G2")

wb.save("iqbalhanif.xlsx")
