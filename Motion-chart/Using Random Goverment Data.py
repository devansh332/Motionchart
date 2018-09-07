import pandas as pd
from motionchart.motionchart import MotionChart
#Acknowlegement as asked  in Task 2 this data is fetch from Data.gov.au
df=pd.read_csv(r"Data\Bluetooth_travel_time_links.csv")
mc=MotionChart(
    df=df,
    x='site_origin',
    y='site_destination',
    color='direction',
    category='description')
mc.to_browser()
