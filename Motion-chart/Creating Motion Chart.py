import operator
import datetime
import pandas as pd
from motionchart.motionchart import MotionChart
#main program start from here

df=pd.read_csv(r'Data\ERP_by state and gender.csv')
cf=pd.read_csv(r'Data\House Price Index.csv')
ff=pd.read_excel(r'Data\\SA4 Time Series - October 2016.xls',sheet_name='Time Series')
states1=(ff.iloc[:,0])
states=(ff.iloc[:,0]).unique()
unim=ff.iloc[:,3]
date=ff.iloc[:,1]
date=date.apply(lambda x : datetime.datetime.strftime(x,'%Y-%m-%d'))
date1=df.iloc[:,0]
final=[]
population=df.iloc[:,19:len(df.columns)]
hpi=cf.iloc[:,1:]
for i in range(len(date1)):
    for j in range(len(date)):
        if(date1[i]==date[j]):
            c=[date1[i],states1[j],unim[j]]
            final.append(c)
u=[]
h=[]
t=[]
c=0
for i in range(len(date)):
    for j in range(len(cf)):
        if(date[i]==df.loc[j][0]):
            for k in range(9):
                l=cf.loc[j][k]
                u.append(l)
chunk=[u[x:x+9]for x in range(0,len(u),9)]
for i in range(len(date)):
    for j in range(len(df)):
        if(date[i]==df.loc[j][0]):
            for k in range(9):
                l=df.loc[j][k]
                h.append(l)
chunk1=[h[x:x+9]for x in range(0,len(h),9)]
final.sort(key=operator.itemgetter(0))
chunk.sort(key=operator.itemgetter(0))
chunk1.sort(key=operator.itemgetter(0))
output=[]
for y in chunk1:
    if y not in output:
        output.append(y)
ss=[]
for y in chunk:
    if y not in ss:
        ss.append(y)
ekor=[]
for i in range (len(output)):
    t=1
    for j in range(len(final)):
        if(final[j][0]==output[i][0]):
            d=[final[j][0],final[j][1],output[i][t]]
            if d not in ekor:
                ekor.append(d)
                t+=1
ekor1=[]
for i in range (len(output)):
    t=1
    for j in range(len(final)):
        if(final[j][0]==ss[i][0]):
            d=[final[j][0],final[j][1],ss[i][t]]
            if d not in ekor:
                ekor1.append(d)
                t+=1
for i in range(len(final)):
    for k in range(len(ekor)):
        if(final[i][0]==ekor[k][0] and final[i][1]==ekor[k][1] ):
            final[i].append(ekor[k][2])
for i in range(len(final)):
    for k in range(len(ekor1)):
        if(final[i][0]==ekor1[k][0] and final[i][1]==ekor1[k][1] ):
            final[i].append(ekor1[k][2])
fruitdf = pd.DataFrame(final)
fruitdf.columns = [ 'date','states', 'unemployment', 'population', 'housepriceindex']
fruitdf['date'] =  pd.to_datetime(fruitdf['date'])
mChart = MotionChart(
              df = fruitdf,
              url = "http://socr.ucla.edu/htmls/HTML5/MotionChart",
              key = 'date',
              x = 'housepriceindex',
              y = 'unemployment',
              size = 'population',
              color = 'states',
              category='states')
mChart.to_browser()
